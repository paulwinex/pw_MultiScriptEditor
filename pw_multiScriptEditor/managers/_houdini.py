import os, sys, re
# import hou
main = __import__('__main__')
hou = main.__dict__['hou']
import hqt
reload (hqt)
from managers.completeWidget import contextCompleterClass

path = os.path.join(os.path.dirname(__file__), 'houdini')

main = __import__('__main__')
ns = main.__dict__
for mod in [os.path.splitext(x)[0] for x in os.listdir(path)]:
    if not mod in ns:
        try:
            exec 'import ' + mod in ns
        except:
            pass

if not path in sys.path:
    sys.path.insert(0, path)

from pw_multiScriptEditor import scriptEditor
reload(scriptEditor)


def show(*args, **kwargs):
    hqt.show(scriptEditor.scriptEditorClass, *args, **kwargs)



# EXAMPLE SHELF BUTTON
# H13
# path = 'path/to/MultiScriptEditor_module'
# # example c:/houdini/python/lib
# if not path in sys.path:
#     sys.path.append(path)
# import pw_multiScriptEditor
# reload(pw_multiScriptEditor)
# pw_multiScriptEditor.showHoudini(ontop=1)

# H14
#import sys
# path = 'path/to/MultiScriptEditor_module'
# # example c:/houdini/python/lib
# if not path in sys.path:
#     sys.path.append(path)
# import pw_multiScriptEditor
# reload(pw_multiScriptEditor)
# pw_multiScriptEditor.showHoudini(name='Multi Script Editor',replacePyPanel=1, hideTitleMenu=0)




###################### CONTEXT FUNCTIONS

# def saveToNode(code, node):
#     definition = node.type().definition()
#     definition.sections()["PythonCook"].setContents(code)
# saveToNode('import hou',hou.selectedNodes()[0])

def getAllDifinitions():
    names = []
    for key in hou.nodeTypeCategories().keys():
        names += hou.nodeTypeCategories()[key].nodeTypes().keys()
    names = list(set(names))
    return names

roots = ['obj', 'shop', 'ch', 'vex', 'img', 'out']
nodes = list(set(getAllDifinitions()))

def completer(line, ns):
    # node types
    func = ['createNode', 'createInputNode', 'createOutputNode']
    for f in func:
        p = r"\.%s\(.*['\"](\w*)$" % f
        m = re.search(p, line)
        if m:
            name = m.group(1)
            if name:
                auto = [x for x in nodes if x.lower().startswith(name.lower())]
            else:
                auto = nodes
            l = len(name)
            return [contextCompleterClass(x, x[l:], True) for x in auto], None
    # absolute path
    p = r"(?<=['\"]{1})(/[\w/]*)$"
    m = re.search(p, line)
    if m:
        name = m.group(0)
        auto, add = getChildrenFromPath(name)
        if auto or add:
            return auto, add
    return None, None

def getChildrenFromPath(path):
    sp = path.rsplit('/', 1)
    if not sp[0]: # rootOnly
        if sp[1]:
            nodes = [contextCompleterClass(x, x[len(sp[1]):]) for x in roots if x.startswith(sp[1])]
            return nodes, None
        else:
            nodes = [contextCompleterClass(x, x) for x in roots]
            return nodes, None
    # add parms
    else:
        node = hou.node(sp[0][1:])
        if node:
            nd = list(set([x.name() for x in node.children()]))
            nodes = [contextCompleterClass(x, x[len(sp[1]):]) for x in sorted(nd) if x.startswith(sp[1])]
            ch = list(set([x.name() for x in node.parms()] + [x.name() for x in node.parmTuples()]))
            channels = [contextCompleterClass(x, x[len(sp[1]):]) for x in sorted(ch) if x.startswith(sp[1])]
            return nodes, channels
    return None, None

def contextMenu(parent):
    m = houdiniMenuClass(parent)
    return m

class houdiniMenuClass(hqt.QMenu):
    def __init__(self, parent):
        super(houdiniMenuClass, self).__init__('Houdini', parent)
        self.par = parent
        self.setTearOffEnabled(1)
        self.setWindowTitle('MSE %s Houdini' % self.par.ver)
        self.addAction(hqt.QAction('Read From Node', parent, triggered=self.readFromNode))
        self.addAction(hqt.QAction('Save To Node', parent, triggered=self.saveToNode))
        self.addSeparator()
        self.addAction(hqt.QAction('Read from hou.session Sourse', parent, triggered=self.readFromSession))
        self.addAction(hqt.QAction('Save to hou.session', parent, triggered=self.saveToSession))



    def readFromNode(self):
        sel = hou.selectedNodes()
        if sel:
            res = self.getSectionsFromNode(sel[0])
            if not res:
                hou.ui.displayMessage('Sections not found1')
                return
            keys = res.keys()
            s = hou.ui.selectFromList(keys, exclusive=1)
            if s:
                source = res[keys[s[0]]]
                text = '#Empty'
                if isinstance(source, hou.Parm):
                    text = source.eval()
                elif isinstance(source, hou.HDASection):
                    text = source.contents()
                self.par.tab.addNewTab(sel[0].name()+'|'+source.name(), text)
        else:
            hou.ui.displayMessage('Select One Node')

    def saveToNode(self):
        sel = hou.selectedNodes()
        if sel:
            res = self.getSectionsFromNode(sel[0])
            if res:
                text = self.par.tab.getCurrentText()
                curr = self.par.tab.currentTabName()
                section = curr.split('|')[-1]
                keys = res.keys()
                if section in keys:
                    d = (keys.index(section),)
                else:
                    d = ()
                s = hou.ui.selectFromList(keys,  default_choices=d,exclusive=1)
                if s:
                    source = res[keys[s[0]]]
                    if isinstance(source, hou.Parm):
                        source.set(text)
                    elif isinstance(source, hou.HDASection):
                        source.setContents(text.strip())
            else:
                hou.ui.displayMessage('Sections not found')
                return
        else:
            hou.ui.displayMessage('Select One Node')

    def getSectionsFromNode(self, node):
        default = ['Help', 'TypePropertiesOptions', 'ExtraFileOptions',  'Tools.shelf', 'InternalFileOptions', 'Contents.gz', 'CreateScript', 'DialogScript']
        res = {}
        Def = node.type().definition()
        if Def:
            sections = Def.sections()
            for s in sections:
                if not sections[s].name() in default:
                    res[s] = sections[s]
        pySop = hou.parm(node.path() + '/python')
        if pySop:
            res['PythonSOP'] = pySop
        return res

    def readFromSession(self):
        source = hou.sessionModuleSource()
        self.par.tab.addNewTab('hou.session', source)

    def saveToSession(self):
        text = self.par.tab.getCurrentText()
        hou.setSessionModuleSource(text)



def wrapDroppedText(namespace, text, event):
    if event.keyboardModifiers() == hqt.Qt.AltModifier:
        syntax = []
        #node
        for node_parm in text.split(','):
            node = hou.node(node_parm)
            if node:
                syntax.append('hou.node("%s")' % node_parm)

        #parmTuple
        spl = text.split(',')
        if len(list(set([x[:-1] for x in spl]))) == 1:
            parmTuple = hou.parmTuple(spl[0][:-1])
            if parmTuple:
                syntax.append('hou.parmTuple("%s")' % spl[0][:-1])
        # parm
        if not syntax:
            for node_parm in text.split(','):
                parm = hou.parm(node_parm)
                if parm:
                    syntax.append('hou.parm("%s")' % node_parm)
        if syntax:
            return '\n'.join(syntax)

    return text

