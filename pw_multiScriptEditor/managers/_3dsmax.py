import os, sys, re

from PySide import QtGui
from PySide import QtCore

from pw_multiScriptEditor import scriptEditor
reload(scriptEditor)

q3dsmax = QtGui.QApplication.instance()

class MaxDialogEvents(QtCore.QObject):
    def eventFilter(self, obj, event):
        import MaxPlus
        if event.type() == QtCore.QEvent.WindowActivate:
            MaxPlus.CUI.DisableAccelerators()
        elif event.type() == QtCore.QEvent.WindowDeactivate:
            MaxPlus.CUI.EnableAccelerators()

        return False

def show():
    se = scriptEditor.scriptEditorClass(parent=None)
    se.installEventFilter(MaxDialogEvents())
    se.runCommand('import MaxPlus')
    se.MaxEventFilter = MaxDialogEvents()
    se.installEventFilter(se.MaxEventFilter)
    se.show()
