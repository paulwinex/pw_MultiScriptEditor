from PySide.QtCore import *
from PySide.QtGui import *
import os
import numBarWidget, inputWidget
reload(inputWidget)
from managers import context


style = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'style', 'completer.qss')
if not os.path.exists(style):
    style=None

class tabWidgetClass(QTabWidget):
    def __init__(self, parent=None):
        super(tabWidgetClass, self).__init__(parent)
        # ui
        self.setTabsClosable(True)
        self.setMovable(True)
        self.tabCloseRequested.connect(self.closeTab)
        self.tabBar().setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabBar().customContextMenuRequested.connect(self.openMenu)
        newTabButton = QPushButton(self)
        newTabButton.setMaximumWidth(30)
        self.setCornerWidget(newTabButton, Qt.TopLeftCorner)
        newTabButton.setCursor(Qt.ArrowCursor)
        newTabButton.setText('+')
        newTabButton.clicked.connect(self.addNewTab)
        newTabButton.setToolTip("Add Tab")
        self.desk = QApplication.desktop()
        # variables
        self.p = parent

        #connects
        self.currentChanged.connect(self.hideAllCompleters)

    def closeTab(self, i):
        if self.count() > 1:
            self.removeTab(i)

    def openMenu(self):
        menu = QMenu(self)
        menu.addAction(QAction('Rename Current Tab', self, triggered = self.renameTab))
        menu.exec_(QCursor.pos())

    def renameTab(self):
        index = self.currentIndex()
        text = self.tabText(index)
        result = QInputDialog.getText( self, 'New name', 'Enter New Name', text =text)
        if result[1]:
            self.setTabText(index, result[0])

    def addNewTab(self, name='New Tab', text = None):
        cont = container(text, self.p, self.desk)#, self.completer)
        cont.edit.saveSignal.connect(self.p.saveSession)
        # cont.edit.executeSignal.connect(self.p.executeSelected)
        self.addTab(cont, name)
        self.setCurrentIndex(self.count()-1)
        return cont.edit

    def getTabText(self, i):
        text = self.widget(i).edit.toPlainText()
        return text

    def addToCurrent(self, text):
        i = self.currentIndex()
        self.widget(i).edit.insertPlainText(text)

    def getCurrentSelectedText(self):
        i = self.currentIndex()
        text = self.widget(i).edit.getSelection()
        return text

    def getCurrentText(self):
        i = self.currentIndex()
        text = self.widget(i).edit.toPlainText()
        return text

    def setCurrentText(self, text):
        i = self.currentIndex()
        self.widget(i).edit.setPlainText(text)


    def hideAllCompleters(self):
        for i in range(self.count()):
            self.widget(i).edit.completer.hideMe()



class container(QWidget):
    def __init__(self, text, parent, desk):
        super(container, self).__init__()
        hbox = QHBoxLayout(self)
        hbox.setSpacing(0)
        hbox.setContentsMargins(0,0,0,0)
        # input widget
        self.edit = inputWidget.inputClass(parent, desk)
        self.edit.executeSignal.connect(parent.executeSelected)
        if text:
            self.edit.addText(text)
        if not context == 'hou':
            # line number
            self.lineNum = numBarWidget.lineNumberBarClass(self.edit, self)
            hbox.addWidget(self.lineNum)
        hbox.addWidget(self.edit)


if __name__ == '__main__':
    app = QApplication([])
    w = tabWidgetClass()
    w.show()
    app.exec_()