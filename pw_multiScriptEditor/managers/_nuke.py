from PySide.QtGui import *
from PySide.QtCore import *
from .. import scriptEditor
reload(scriptEditor)
import os, sys
p = os.path.dirname(__file__)
if not p in sys.path:
    sys.path.insert(0, p)

import nuke
import nukescripts

qApp = QApplication.instance()

def getMainWindow():
    for widget in qApp.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget
qNuke = getMainWindow()

def show(panel=False):
    if panel:
        import pw_scriptEditor.scriptEditor
        nukescripts.panels.registerWidgetAsPanel("pw_scriptEditor.scriptEditor.scriptEditorClass", "Multi Script Editor", "pw_multi_script_editor")
    else:
        showWindow()


def showWindow():
    se = scriptEditor.scriptEditorClass(qNuke)
    se.runCommand('import nuke')
    se.show()

#panel

class ScriptEditorKnob():
  def makeUI(self):
    self.webWidget = scriptEditor.scriptEditorClass()
    return self.webWidget

class WebBrowserPanel(nukescripts.PythonPanel):
  def __init__(self):
    super(WebBrowserPanel, self).__init__("Multi Script Editor", "uk.co.thefoundry.ScriptEditorPanel")
    # self.webBrowserKnob = nuke.PyCustom_Knob( "tool", "", "pw_scriptEditor.managers._nuke.ScriptEditorKnob()" )
    self.webBrowserKnob = nuke.PyCustom_Knob( "pw_scriptEditor.managers._nuke.ScriptEditorKnob()" )
    self.addKnob( self.webBrowserKnob )

def addPanel():
  return WebBrowserPanel().addToPane()


### Example for menu.py
# menubar = nuke.menu("Nuke") # Access the main menu bar
# toolMenu = menubar.addMenu('&Tools')
# path = 'path/to/package'
# if not path in sys.path:
#     sys.path.append(path)
#
# import pw_scriptEditor
# # add to menu
# toolMenu.addCommand("Multi Script Editor", "pw_scriptEditor.showNuke()")
# # create new pane
# pw_scriptEditor.showNuke(panel=True)