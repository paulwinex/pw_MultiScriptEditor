from PySide.QtGui import *
from PySide.QtCore import *
import maya.OpenMayaUI as omui
from shiboken import wrapInstance as wrp
import os, sys


main = __import__('__main__')
ns = main.__dict__
exec 'import pymel.core as pm'
# jedi completion path
compPath = os.path.join(os.environ['MAYA_LOCATION'],'devkit/other/pymel/extras/completion/py').replace('\\','/')
if compPath in sys.path:
    sys.path.remove(compPath)
sys.path.insert(0, compPath)

def getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
    if ptr is not None:
        return wrp(long(ptr), QMainWindow)

def show():

    from .. import scriptEditor
    reload(scriptEditor)

    editor = scriptEditor.scriptEditorClass(parent=getMayaWindow())
    editor.show()

# Shelf button example
# import sys
# path = 'path/to/MultiScriptEditor_module'
# # example c:/maya/python/lib
# if not path in sys.path:
#     sys.path.append(path)
# import pw_multiScriptEditor
# reload(pw_multiScriptEditor)
# pw_multiScriptEditor.showMaya()