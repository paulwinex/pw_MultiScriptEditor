main = __import__('__main__')
import platform, re


# context completer
class contextCompleterClass(object):
    def __init__(self, name, complete):
        self.name = name
        self.complete = complete

############################################################################
# NUKE

def nukeCompleter(line):
    # print( nuke.tprint(line))
    p1 = r"nuke\.createNode\(['\"](\w*)$"
    p2 = r"nuke\.nodes\.(\w*)$"
    m = re.search(p1, line) or re.search(p2, line)
    if m:
        name = m.group(1)
        if name:
            auto = [x for x in nodes if x.lower().startswith(name.lower())]
            l = len(name)
            return [contextCompleterClass(x, x[l:]) for x in auto]
############################################################################
# HOUDINI

def getAllDifinitions():
    names = []
    for key in hou.nodeTypeCategories().keys():
        names += hou.nodeTypeCategories()[key].nodeTypes().keys()
    names = list(set(names))
    return names

def houdiniCompleter(line):
    func = ['createNode', 'createInputNode', 'createOutputNode']
    for f in func:
        p = r"\.%s\(['\"](\w*)$" % f
        m = re.search(p, line)
        if m:
            name = m.group(1)
            if name:
                auto = [x for x in nodes if x.lower().startswith(name.lower())]
                l = len(name)
                return [contextCompleterClass(x, x[l:]) for x in auto]



#####################################################################
# MAYA
def mayaCompleter(line):
    p = r"createNode\(['\"](\w*)$"
    m = re.search(p, line)
    if m:
        name = m.group(1)
        if name:
            auto = [x for x in nodes if x.lower().startswith(name.lower())]
            l = len(name)
            return [contextCompleterClass(x, x[l:]) for x in auto]


###################################################################


contextCompleters = dict(
    nuke=nukeCompleter,
    hou=houdiniCompleter,
    maya=mayaCompleter
)

context = None
if 'hou' in main.__dict__:
    context = 'hou'
    hou = main.__dict__['hou']
    nodes = list(set(getAllDifinitions()))
elif 'cmds' in main.__dict__:
    context = 'maya'
    main = __import__('__main__')
    ns = main.__dict__
    exec 'import pymel.core as pm' in ns
    pm = main.__dict__['pm']
    nodes = pm.allNodeTypes()
elif 'nuke' in main.__dict__:
    context = 'nuke'
    nuke = main.__dict__['nuke']
    from managers.nuke import nodes
    nodes = dir(nodes)




if platform.system().lower() == 'windows':
    _s = 'w'
elif platform.system().lower() == 'darwin':
    _s = 'x'
else:
    _s = 'l'