from PySide.QtGui import *
from PySide.QtCore import *
import maya.OpenMayaUI as omui
from shiboken import wrapInstance as wrp
import os, sys, re
from managers.completeWidget import contextCompleterClass

main = __import__('__main__')
ns = main.__dict__
exec 'import pymel.core as pm' in ns
pm = main.__dict__['pm']

# jedi completion path
compPath = os.path.join(os.environ['MAYA_LOCATION'],'devkit/other/pymel/extras/completion/py').replace('\\','/')
if compPath in sys.path:
    sys.path.remove(compPath)
sys.path.insert(0, compPath)

def getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
    if ptr is not None:
        return wrp(long(ptr), QMainWindow)

def show(dock=False):
    if dock:
        showDickControl()
    else:
        showWindow()

def showWindow():
    from pw_multiScriptEditor import scriptEditor
    reload(scriptEditor)

    editor = scriptEditor.scriptEditorClass(parent=getMayaWindow())
    editor.show()



def showDickControl():
    name = 'pw_scriptEditor'
    if pm.window(name, q=1, ex=1):
        pm.deleteUI(name)
    from pw_multiScriptEditor import scriptEditor
    reload(scriptEditor)
    editor = scriptEditor.scriptEditorClass(parent=getMayaWindow())

    name = 'pw_scriptEditor'
    dockName = 'pw_scriptEditorDock'

    if pm.dockControl(dockName, q=1, ex=1):
        pm.deleteUI(dockName)


    pm.dockControl(dockName, area='left',
                 content=editor.objectName(),
                 width=700,
                 label='Multi Script Editor',
                 allowedArea=['right', 'left'])


# Shelf button example
# import sys
# path = 'path/to/MultiScriptEditor_module'
# # example c:/maya/python/lib
# if not path in sys.path:
#     sys.path.append(path)
# import pw_multiScriptEditor
# reload(pw_multiScriptEditor)
# pw_multiScriptEditor.showMaya(dock=True)


nodes = pm.allNodeTypes()

def completer(line):
    # create node
    p = r"createNode\(['\"](\w*)$"
    m = re.search(p, line)
    if m:
        name = m.group(1)
        if name:
            auto = [x for x in nodes if x.lower().startswith(name.lower())]
            l = len(name)
            return [contextCompleterClass(x, x[l:], True) for x in auto], None
    # exists nodes
    p = r"PyNode\(['\"](\w*)$"
    m = re.search(p, line)
    if m:
        name = m.group(1)
        existsNodes = sorted(pm.cmds.ls())
        l = len(name)
        if name:
            auto = [x for x in existsNodes if x.lower().startswith(name.lower())]
            return [contextCompleterClass(x, x[l:], True) for x in auto], None
        else:
            return [contextCompleterClass(x, x, True) for x in existsNodes], None
    return None, None

# drop event

def wrapDroppedText(namespace, text, event):
    if event.keyboardModifiers() == Qt.AltModifier:
        # pymel with namespace
        for k, m in namespace.items():
            if hasattr(m, '__name__'):
                if m.__name__ == 'pymel.core' and not k == 'm':
                    syntax = []
                    for node in text.split():
                        if namespace[k].objExists(node):
                            syntax.append(k+'.PyNode("%s")' % node)
                        else:
                            syntax.append(node)
                    return '\n'.join(syntax)
        # pymel no namespace
        if 'PyNode' in namespace.keys():
            syntax = []
            for node in text.split():
                if namespace['objExists'](node):
                    syntax.append('PyNode("%s")' % node)
                else:
                    syntax.append(node)
            return '\n'.join(syntax)
                # return 'PyNode("%s")' % text

        # cmds with namespace
        for k, m in namespace.items():
            if hasattr(m, '__name__'):
                if m.__name__ == 'maya.cmds' and not k == 'm':
                    syntax = []
                    for node in text.split():
                        if namespace[k].objExists(node):
                            syntax.append('"%s"' % node)
                        else:
                            syntax.append(node)
                    return '\n'.join(syntax)
        # cmds without namespace
        if 'about' in namespace.keys():
            try:
                syntax = []
                for node in text.split():
                    if namespace['objExists'](node):
                        syntax.append('"%s"' % node)
                    else:
                        syntax.append(node)
                return '\n'.join(syntax)
            except:
                pass
    return text


