from PySide.QtGui import *
from PySide.QtCore import *
from .. import scriptEditor
reload(scriptEditor)
import os, sys
import nuke
import nukescripts

p = os.path.dirname(__file__)
if not p in sys.path:
    sys.path.insert(0, p)

qApp = QApplication.instance()

def getMainWindow():
    for widget in qApp.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget
qNuke = getMainWindow()

def show(panel=False):
    if panel:
        import pw_multiScriptEditor.scriptEditor
        nukescripts.panels.registerWidgetAsPanel("pw_multiScriptEditor.scriptEditor.scriptEditorClass", "Multi Script Editor", "pw_multi_script_editor")
    else:
        showWindow()


def showWindow():
    se = scriptEditor.scriptEditorClass(qNuke)
    se.runCommand('import nuke')
    se.show()


# add to menu.py
# Add to menu.py
# menubar = nuke.menu("Nuke")
# toolMenu = menubar.addMenu('&Tools')
# path = 'path/to/MultiScriptEditor_module'
# # example c:/nuke/python/lib
# if not path in sys.path:
#     sys.path.append(path)
#
# import pw_multiScriptEditor
# # add to menu
# toolMenu.addCommand("Multi Script Editor", "pw_multiScriptEditor.showNuke()")
# # create new pane
# pw_multiScriptEditor.showNuke(panel=True)

