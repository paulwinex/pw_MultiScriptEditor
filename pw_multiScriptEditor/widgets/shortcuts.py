from PySide.QtCore import *
from PySide.QtGui import *
import shortcuts_UIs
import os

class shortcutsClass(QDialog, shortcuts_UIs.Ui_Dialog):
    def __init__(self, parent):
        super(shortcutsClass, self).__init__(parent)
        self.setupUi(self)
        self.table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Action', 'Shortcut'])
        self.read()

    def read(self):
        src = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'shortcuts.txt')
        if os.path.exists(src):
            self.label.hide()
            lines = open(src).readlines()
            for i, l in enumerate(lines):
                self.table.insertRow(self.table.rowCount())
                description, shortcut = l.split('>')
                item = QTableWidgetItem(description)
                self.table.setItem(i, 0, item)
                item.setFlags(Qt.ItemIsEnabled)
                item = QTableWidgetItem(shortcut)
                item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, 1, item)
        else:
            self.table.hide()
