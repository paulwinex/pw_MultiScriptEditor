try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *

from managers import context
font_name = 'Courier'


class outputClass(QTextBrowser):
    def __init__(self):
        super(outputClass, self).__init__()
        self.setWordWrapMode(QTextOption.NoWrap)
        font = QFont("Courier")
        font.setStyleHint(QFont.Monospace)
        font.setFixedPitch(True)
        self.setFont(font)
        self.fs = 14
        self.document().setDefaultFont(QFont(font_name, self.fs, QFont.Monospace))
        metrics = QFontMetrics(self.document().defaultFont())
        self.setTabStopWidth(4 * metrics.width(' '))
        self.setMouseTracking(1)

    def showMessage(self, msg):
        self.moveCursor(QTextCursor.End)
        cursor = self.textCursor()
        cursor.insertText(str(msg)+'\n')
        self.setTextCursor(cursor)
        self.moveCursor(QTextCursor.End)
        self.ensureCursorVisible()

    def setTextEditFontSize(self, size):
        style = '''QTextEdit
    {
        font-size: %spx;
    }''' % size
        self.setStyleSheet(style)


    def wheelEvent(self, event):
        if event.modifiers() == Qt.ControlModifier:
            if event.delta() > 0:
                self.changeFontSize(True)
            else:
                self.changeFontSize(False)
        # super(outputClass, self).wheelEvent(event)
        QTextBrowser.wheelEvent(self, event)

    def changeFontSize(self, up):
        if context == 'hou':
            if up:
                self.fs = min(30, self.fs+1)
            else:
                self.fs = max(8, self.fs - 1)
            self.setTextEditFontSize(self.fs)
        else:
            f = self.font()
            size = f.pointSize()
            if up:
                size = min(30, size+1)
            else:
                size = max(8, size - 1)
            f.setPointSize(size)
            self.setFont(f)


    # def mousePressEvent(self, event):
    #     print context
    #     if context == 'hou':
    #         if event.button() == Qt.LeftButton:
    #             # super(outputClass, self).mousePressEvent(event)
    #             QTextBrowser.mousePressEvent(self, event)
    #     else:
    #     QTextBrowser.mousePressEvent(self, event)