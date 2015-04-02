from PySide.QtCore import *
from PySide.QtGui import *
import findWidget_UIs as ui

class findWidgetClass(QWidget, ui.Ui_findReplace):
    searchSignal = Signal(str)
    replaceSignal = Signal(list)
    replaceAllSignal = Signal(list)
    def __init__(self, parent):
        super(findWidgetClass, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Tool)
        center = parent.parent().mapToGlobal(parent.geometry().center())
        myGeo = self.geometry()
        myGeo.moveCenter(center)
        self.setGeometry(myGeo)
        self.find_le.setFocus()
        #connect
        self.find_btn.clicked.connect(self.search)
        self.find_le.returnPressed.connect(self.search)
        self.replace_btn.clicked.connect(self.replace)
        self.replace_le.returnPressed.connect(self.replace)
        self.replaceAll_btn.clicked.connect(self.replaceAll)

    def search(self):
        self.searchSignal.emit(self.find_le.text())

    def replace(self):
        find = self.find_le.text()
        rep = self.replace_le.text()
        self.replaceSignal.emit([find, rep])

    def replaceAll(self):
        find = self.find_le.text()
        rep = self.replace_le.text()
        self.replaceAllSignal.emit([find, rep])