from PySide.QtGui import *
from PySide.QtCore import *
import maya.OpenMayaUI as omui
from shiboken import wrapInstance as wrp
import os, sys

def getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
    if ptr is not None:
        return wrp(long(ptr), QMainWindow)

def show():
    # jedi completion
    compPath = os.path.join(os.environ['MAYA_LOCATION'],'devkit/other/pymel/extras/completion/py').replace('\\','/')
    if compPath in sys.path:
        sys.path.remove(compPath)
    sys.path.insert(0, compPath)

    from .. import scriptEditor
    reload(scriptEditor)

    editor = scriptEditor.scriptEditorClass(parent=getMayaWindow())
    editor.show()

