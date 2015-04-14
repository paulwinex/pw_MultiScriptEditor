from PySide.QtCore import *
from PySide.QtGui import *
import os, re
from . pythonSyntax import design
import managers
style = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'style', 'completer.qss')
if not os.path.exists(style):
    style=None


class completeMenuClass(QListWidget):
    def __init__(self, parent=None, editor=None):
        super(completeMenuClass, self).__init__(parent)
        self.setAlternatingRowColors(1)
        self.lineHeight = 18
        self.e = editor
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        if managers._s == 'w':
            self.setWindowFlags(Qt.FramelessWindowHint |  Qt.Window)
        else:
            self.setWindowFlags(Qt.FramelessWindowHint |  Qt.Window | Qt.WindowStaysOnTopHint)
        @self.itemDoubleClicked.connect
        def insertSelected(item):
            if item:
                comp = item.data(32)
                self.sendText(comp)
                self.hideMe()

    def updateStyle(self, colors=None):
        text = design.editorStyle()
        self.setStyleSheet(text)

    def updateCompleteList(self, lines=None, extra=None):
        self.clear()
        if lines or extra:
            self.showMe()
            if lines:
                for i in [x for x in lines if not x.name == 'mro']:
                    item = QListWidgetItem(i.name)
                    item.setData(32, i)
                    self.addItem(item)
            if extra:

                font = self.font()
                font.setItalic(1)
                font.setPointSize(font.pointSize()*0.8)
                for e in extra:
                    item = QListWidgetItem(e.name)
                    item.setData(32, e)
                    item.setFont(font)
                    self.addItem(item)

            font = QFont("monospace", self.lineHeight, False)
            fm = QFontMetrics (font)
            width = fm.width(' ') *  max([len(x.name) for x in lines or extra]) + 40

            self.resize(max(250,width), 250)
            self.setCurrentRow(0)
        else:
            self.hideMe()

    def applyCurrentComplete(self):
        i = self.selectedItems()
        if i:
            comp = i[0].data(32)
            self.sendText(comp)
        self.hideMe()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
        # elif event.text():
        #     self.editor().setFocus()
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.editor().setFocus()
            self.applyCurrentComplete()
            return event
        elif event.key() == Qt.Key_Up:
            sel = self.selectedItems()
            if sel:
                i = self.row(sel[0])
                if i == 0:
                    QListWidget.keyPressEvent(self, event)
                    self.setCurrentRow(self.count()-1)
                    return
        elif event.key() == Qt.Key_Down:
            sel = self.selectedItems()
            if sel:
                i = self.row(sel[0])
                if i+1 == self.count():
                    QListWidget.keyPressEvent(self, event)
                    self.setCurrentRow(0)
                    return
        elif event.key() == Qt.Key_Backspace:
            self.editor().setFocus()
            self.editor().activateWindow()
        elif event.text():
            self.editor().keyPressEvent(event)
            return

        QListWidget.keyPressEvent(self, event)

    def sendText(self, comp):
        self.editor().insertText(comp)

    def editor(self):
        return self.e

    def activateCompleter(self, key=False):
        self.activateWindow()
        if not key==Qt.Key_Up:
            self.setCurrentRow(min(1, self.count()-1))
        else:
            self.setCurrentRow(self.count()-1)

    def showMe(self):
        self.show()
        self.e.moveCompleter()

    def hideMe(self):
        self.hide()
