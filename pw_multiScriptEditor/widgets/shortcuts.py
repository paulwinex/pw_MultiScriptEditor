from PySide.QtCore import *
from PySide.QtGui import *
import shortcuts_UIs

class shortcutsClass(QDialog, shortcuts_UIs.Ui_Dialog):
    def __init__(self, parent):
        super(shortcutsClass, self).__init__(parent)
        self.setupUi(self)