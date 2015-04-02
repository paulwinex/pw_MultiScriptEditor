from PySide.QtCore import *
from PySide.QtGui import *
import managers

class lineNumberBarClass(QWidget):
    def __init__(self, edit, parent=None):
        QWidget.__init__(self, parent)
        self.edit = edit
        self.highest_line = 0
        self.setMinimumWidth(30)
        self.edit.installEventFilter(self)
        self.edit.viewport().installEventFilter(self)
        self.bg = None

    def update(self, *args):
        '''
        Updates the number bar to display the current set of numbers.
        Also, adjusts the width of the number bar if necessary.
        '''
        # The + 4 is used to compensate for the current line being bold.
        if managers.context == 'hou':
            fontSize = self.edit.fs
        else:
            fontSize = self.edit.font().pointSize()
        width = ((self.fontMetrics().width(str(self.highest_line)) + 7))*(fontSize/13.0)
        if self.width() != width and width > 10:
            self.setFixedWidth(width)
        bg = self.palette().brush(QPalette.Normal,QPalette.Window).color().toHsv()
        v = bg.value()
        if v > 20:
            v = int(bg.value()*0.8)
        else:
            v = int(bg.value()*1.1)
        self.bg = QColor.fromHsv(bg.hue(), bg.saturation(), v)
        QWidget.update(self, *args)

    def paintEvent(self, event):
        contents_y = self.edit.verticalScrollBar().value()
        page_bottom = contents_y + self.edit.viewport().height()
        font_metrics = self.fontMetrics()
        current_block = self.edit.document().findBlock(self.edit.textCursor().position())
        painter = QPainter(self)
        line_count = 0
        # Iterate over all text blocks in the document.
        block = self.edit.document().begin()
        if managers.context == 'hou':
            fontSize = self.edit.fs
            font = QFont('monospace', fontSize*0.7)
            offset = (font_metrics.ascent() + font_metrics.descent())/2
        else:
            fontSize = self.edit.font().pointSize()
            font = painter.font()
            font.setPixelSize(fontSize)
            offset = font_metrics.ascent() + font_metrics.descent()
        color = painter.pen().color()
        painter.setFont(font)
        align = Qt.AlignRight
        while block.isValid():
            line_count += 1
            # The top left position of the block in the document
            position = self.edit.document().documentLayout().blockBoundingRect(block).topLeft()
            # Check if the position of the block is out side of the visible
            # area.
            if position.y() == page_bottom:
                break

            rec = QRect(0,
                        round(position.y()) - contents_y,
                        self.width()-5,
                        fontSize + offset)

            # draw line rect
            if block == current_block:
                painter.setPen(Qt.NoPen)
                painter.setBrush(QBrush(self.bg))
                painter.drawRect(QRect(0,
                        round(position.y()) - contents_y,
                        self.width(),
                        fontSize + (offset/2) ))
            #   #restore color
                painter.setPen(QPen(color))

            # draw text
            painter.drawText(rec, align, str(line_count))
            # control points

            block = block.next()
        self.highest_line = line_count
        painter.end()
        QWidget.paintEvent(self, event)

    def eventFilter(self, object, event):
        # Update the line numbers for all events on the text edit and the viewport.
        # This is easier than connecting all necessary singals.
        if object in (self.edit, self.edit.viewport()):
            self.update()
            return False
        return QWidget.eventFilter(object, event)