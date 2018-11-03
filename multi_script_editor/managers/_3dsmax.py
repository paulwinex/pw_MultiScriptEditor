import os, sys, re
try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *

from multi_script_editor import scriptEditor
reload(scriptEditor)
import MaxPlus
q3dsmax = QApplication.instance()

class MaxDialogEvents(QObject):
    def eventFilter(self, obj, event):
        import MaxPlus
        if event.type() == QEvent.WindowActivate:
            MaxPlus.CUI.DisableAccelerators()
        elif event.type() == QEvent.WindowDeactivate:
            MaxPlus.CUI.EnableAccelerators()
        return False

def show():
    try:
        qtwindow = MaxPlus.GetQMaxWindow()
    except:
        qtwindow = MaxPlus.GetQMaxMainWindow()
    se = scriptEditor.scriptEditorClass(parent=qtwindow)
    #se.installEventFilter(MaxDialogEvents())
    se.runCommand('import MaxPlus')
    #se.MaxEventFilter = MaxDialogEvents()
    #se.installEventFilter(se.MaxEventFilter)
    se.show()
