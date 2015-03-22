from PySide.QtCore import *
from PySide.QtGui import *
import re
import jedi
# https://github.com/davidhalter/jedi
# http://jedi.jedidjah.ch/en/latest/
from pythonSyntax import syntaxHighLighter
reload(syntaxHighLighter)
import completeWidget
reload(completeWidget)
import settingsManager
import managers
reload(managers)
from pythonSyntax import design
import inspect
from jedi import settings
# settings.case_insensitive_completion = False
addEndBracket = True

indentLen = 4
minimumFontSize = 10
escapeButtons = [Qt.Key_Return, Qt.Key_Enter, Qt.Key_Left, Qt.Key_Right, Qt.Key_Home, Qt.Key_End, Qt.Key_PageUp, Qt.Key_PageDown,
                 Qt.Key_Delete, Qt.Key_Insert]


class inputClass(QTextEdit):
    executeSignal = Signal()
    saveSignal = Signal()
    def __init__(self, parent, desk=None):
        super(inputClass, self).__init__(parent)
        self.p = parent
        self.desk = desk
        self.setWordWrapMode(QTextOption.NoWrap)
        self.document().setDefaultFont(QFont("monospace", minimumFontSize, QFont.Normal))
        metrics = QFontMetrics(self.document().defaultFont())
        self.setTabStopWidth(4 * metrics.width(' '))
        self.setAcceptDrops(True)
        self.fs = 12
        self.completer = completeWidget.completeMenuClass(parent, self)
        # self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.openMenu)
        data = settingsManager.scriptEditorClass().readSettings()
        self.applyHightLighter(data.get('theme'))
        self.changeFontSize(False)
        self.changeFontSize(True)

    def focusOutEvent(self, event):
        self.saveSignal.emit()
        # self.completer.hideMe()
        super(inputClass, self).focusOutEvent(event)

    def hideEvent(self, event):
        self.completer.updateCompleteList()
        super(inputClass, self).hideEvent(event)

    def applyHightLighter(self, theme=None, qss=None):
        self.blockSignals(True)
        colors = None
        if theme or not theme =='default':
            colors = design.getColors(theme)
            if self.completer:
                self.completer.updateStyle(colors)
        self.hgl = syntaxHighLighter.PythonHighlighterClass(self, colors)
        st = design.editorStyle(theme)
        self.setStyleSheet(st)
        self.blockSignals(False)

    def applyPreviewStyle(self, colors):
        self.blockSignals(True)
        self.hgl = syntaxHighLighter.PythonHighlighterClass(self, colors)
        qss = design.applyColorToEditorStyle(colors)
        self.setStyleSheet(qss)
        self.completer.setStyleSheet(qss)
        self.blockSignals(False)

    def parseText(self):
        if self.completer:
            text = self.toPlainText()
            self.moveCompleter()
            if text:
                tc = self.textCursor()
                context_completer = False
                pos = tc.position()
                if managers.context in managers.contextCompleters:
                    line = text[:pos].split('\n')[-1]
                    comp = managers.contextCompleters[managers.context ](line)
                    if comp:
                        context_completer = True
                        self.completer.updateCompleteList(comp)

                if not context_completer:
                    if re.match('[a-zA-Z0-9.]', text[pos-1]):
                        script = jedi.Script(text, tc.blockNumber() + 1, tc.columnNumber(), '')
                        try:
                            # curframe = inspect.currentframe()
                            # print inspect.getouterframes(curframe, 2)[1][3]
                            self.completer.updateCompleteList(script.completions())
                        except:
                            pass
                        return
                    else:
                        self.completer.updateCompleteList()
            else:
                self.completer.updateCompleteList()

    def moveCompleter(self):
        rec = self.cursorRect()
        # pt = self.mapToGlobal(QPoint(rec.bottomRight().x(), rec.y()+self.completer.lineHeight))
        pt = self.mapToGlobal(rec.bottomRight())
        y=x=0
        if self.completer.isVisible() and self.desk:
            currentScreen = self.desk.screenGeometry(self.mapToGlobal(rec.bottomRight()))
            futureCompGeo = self.completer.geometry()
            futureCompGeo.moveTo(pt)
            if not currentScreen.contains(futureCompGeo):
                i = currentScreen.intersect(futureCompGeo)
                x = futureCompGeo.width() - i.width()
                y = futureCompGeo.height()+self.completer.lineHeight if (futureCompGeo.height()-i.height())>0 else 0

        pt = self.mapToGlobal(rec.bottomRight()) + QPoint(10-x, -y)

        self.completer.move(pt)


    def keyPressEvent(self, event):
        parse = 0
        if event.modifiers() == Qt.ControlModifier and event.key() in [Qt.Key_Return , Qt.Key_Enter]:
            if self.completer:
                self.completer.updateCompleteList()
            self.executeSignal.emit()
            return

        elif event.modifiers() == Qt.ShiftModifier and event.key() in [Qt.Key_Return , Qt.Key_Enter]:
            return

        elif event.key() in escapeButtons:
            if self.completer:
                self.completer.updateCompleteList()

        elif event.key() == Qt.Key_Tab:
            if self.completer:
                self.completer.updateCompleteList()
            if self.textCursor().selection().toPlainText():
                self.selectBlocks()
                self.moveSelected(True)
                return
            else:
                self.insertPlainText (' ' * indentLen)
                return

        elif event.key() == Qt.Key_Backtab:
            self.selectBlocks()
            self.moveSelected(False)
            if self.completer:
                self.completer.updateCompleteList()
            return

        elif event.key() == Qt.Key_Escape:
            if self.completer:
                self.completer.updateCompleteList()
            self.setFocus()

        elif event.key() == Qt.Key_Down or event.key() == Qt.Key_Up:
            if self.completer.isVisible():
                self.completer.activateCompleter(event.key())
                self.completer.setFocus()
                return
        elif not event.modifiers() == Qt.NoModifier and not event.modifiers() == Qt.ShiftModifier:
            self.completer.updateCompleteList()
        else:
            parse = 1
        # if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_D:
        #     print 'duplicate line'
        super(inputClass, self).keyPressEvent(event)
        if parse and event.text():
            self.parseText()

    def moveSelected(self, inc):
        cursor = self.textCursor()
        if cursor.hasSelection():
            self.document().documentLayout().blockSignals(True)
            self.selectBlocks()
            start, end = cursor.selectionStart(), cursor.selectionEnd()
            text = cursor.selection().toPlainText()
            cursor.removeSelectedText()
            if inc:
                newText = self.addTabs(text)
            else:
                newText = self.removeTabs(text)
            cursor.beginEditBlock()
            cursor.insertText(newText)
            cursor.endEditBlock()
            newEnd = cursor.position()
            cursor.setPosition(start)
            cursor.setPosition(newEnd, QTextCursor.KeepAnchor)
            self.setTextCursor(cursor)

            self.document().documentLayout().blockSignals(False)
            self.update()

    def insertText(self, comp):
        cursor = self.textCursor()
        cursor.insertText(comp.complete)
        self.fixLine(cursor, comp)
        self.setTextCursor(cursor)

    def fixLine(self, cursor, comp):
        pos = cursor.position()
        linePos = cursor.positionInBlock()

        cursor.movePosition(QTextCursor.MoveOperation.StartOfLine)
        cursor.movePosition(QTextCursor.MoveOperation.EndOfLine,QTextCursor.KeepAnchor)
        line = cursor.selectedText()
        cursor.removeSelectedText()

        start = line[:linePos]
        end = line[linePos:]
        before = start[:-len(comp.name)]
        br = ''
        ofs = 0
        if addEndBracket and before:
            brackets = {'"':'"', "'":"'"}#, '(':')', '[':']'}
            if before[-1] in brackets:
                ofs = 1
                br = brackets[before[-1]]
                if end and end[0] == brackets[before[-1]]:
                    br = ''

        res = before + comp.name + br + end

        cursor.beginEditBlock()
        cursor.insertText(res)
        cursor.endEditBlock()
        cursor.clearSelection()
        cursor.setPosition(pos+ofs,QTextCursor.MoveAnchor)
        return cursor

    def removeTabs(self, text):
        lines = text.split('\n')
        new = []
        pat = re.compile("^ .*")
        for line in lines:
            line = line.replace('\t', ' '*indentLen)
            for _ in range(4):
                if pat.match(line):
                    line = line[1:]
            new.append(line)
        return '\n'.join(new)

    def addTabs(self, text):
        lines = [(' '*indentLen)+x for x in text.split('\n')]
        return '\n'.join(lines)

    def selectBlocks(self):
        cursor = self.textCursor()
        start, end = cursor.selectionStart(), cursor.selectionEnd()
        cursor.setPosition(start)
        cursor.movePosition(QTextCursor.StartOfLine)
        cursor.setPosition(end, QTextCursor.KeepAnchor)
        cursor.movePosition(QTextCursor.EndOfLine, QTextCursor.KeepAnchor)
        self.setTextCursor(cursor)

    def getSelection(self):
        cursor = self.textCursor()
        text = cursor.selection().toPlainText()
        return text
        # if text:
        #     self.executeSignal.emit(text)

    def addText(self, text):
        if self.completer:
                self.completer.updateCompleteList()
        self.blockSignals(True)
        self.append(text)
        self.blockSignals(False)

    ########################### DROP

    def dropEvent(self, event):
        mimeData = event.mimeData()
        if mimeData.hasText():
            event.acceptProposedAction()
        super(inputClass, self).dropEvent(event)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()
        super(inputClass, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        event.acceptProposedAction()
        super(inputClass, self).dragMoveEvent(event)

    def dragLeaveEvent(self, event):
        event.acceptProposedAction()
        super(inputClass, self).dragLeaveEvent(event)

################################################################

    def wheelEvent(self, event):
        if event.modifiers() == Qt.ControlModifier:
            if self.completer:
                self.completer.updateCompleteList()
            if event.delta() > 0:
                self.changeFontSize(True)
                # self.zoomIn(1)
            else:
                self.changeFontSize(False)
                # self.zoomOut(1)
        super(inputClass, self).wheelEvent(event)

    def changeFontSize(self, up):
        if managers.context == 'hou':
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

    def setTextEditFontSize(self, size):
        style = self.styleSheet() +'''QTextEdit
    {
        font-size: %spx;
    }''' % size
        self.setStyleSheet(style)

    def insertFromMimeData (self, source ):
        self.insertPlainText(str(source.text()))

    def getFontSize(self):
        s = self.font().pointSize()
        return s

    def setFontSize(self,size):
        if size > minimumFontSize:
            if managers.context == 'hou':
                self.fs = size
                self.setTextEditFontSize(self.fs)
            else:
                f = self.font()
                f.setPointSize(size)
                self.setFont(f)

    def mousePressEvent(self, event):
        self.completer.updateCompleteList()
        # if managers.context == 'hou':
        #     if event.button() == Qt.LeftButton:
        #         super(inputClass, self).mousePressEvent(event)
        # else:
        super(inputClass, self).mousePressEvent(event)

