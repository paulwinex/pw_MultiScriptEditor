from PySide.QtCore import *
from PySide.QtGui import *
import re
import design
import keywords


class PythonHighlighterClass (QSyntaxHighlighter):
    def __init__(self, document, colors=None):
        QSyntaxHighlighter.__init__(self, document)

        if colors:
            self.colors = colors
        else:
            self.colors = design.getColors()

        # Multi line comments
        self.tri_single = (QRegExp("'''"), 1, self.getStyle(self.colors['docstring']))
        self.tri_double = (QRegExp('"""'), 2, self.getStyle(self.colors['docstring']))

        rules = []
        # defaults
        # rules += [(r".*", 0, self.getStyle(self.colors['default'], False))]
        # Keywords
        rules += [('\\b%s\\b' % w, 0, self.getStyle(self.colors['keywords'], True))
            for w in keywords.syntax['keywords']]
        # Methods
        rules += [("\\b[A-Za-z0-9_]+(?=\\()", 0, self.getStyle(self.colors['methods'], False))]
        # Operators
        rules += [(r'[~!@$%^&*()-+=]', 0, self.getStyle(self.colors['operator']))]
        #    for o in pythonSyntax.syntax['operators']]
        #Braces
        rules += [(r'%s' % b, 0, self.getStyle(self.colors['brace']))
            for b in keywords.syntax['braces']]
        # Definition
        rules += [("\\b%s\\b" % b, 0, self.getStyle(self.colors['definition'], True))
            for b in keywords.syntax['definition']]
        # Extra
        rules += [("\\b%s\\b" % b, 0, self.getStyle(self.colors['extra']))
            for b in keywords.syntax['extras']]

        # Comment
        # rules += [(r'#([.*]+|[^#]*)', 0, self.getStyle(design.comment))]

        # Digits
        rules += [(r"\b[\d]+\b", 0, self.getStyle(self.colors['digits']))]
            # ("(?:^|[^A-Za-z])([\d|\.]*\d+)", 0, self.getStyle(design.digits)),


        # Double-quoted string
        rules += [(r'[ru]?"[^"\\]*(\\.[^"\\]*)*"', 0, self.getStyle(self.colors['string']))]

        # Single-quoted string
        rules += [(r"[ru]?'[^'\\]*(\\.[^'\\]*)*'", 0, self.getStyle(self.colors['string']))]


        # Build a QRegExp for each pattern
        self.rules = [(QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]
        # self.rehighlight()


    def getStyle(self, color, bold=False):
        brush = QBrush( QColor(*color))
        f = QTextCharFormat()
        if bold:
            f.setFontWeight( QFont.Bold )
        f.setForeground( brush )
        return f

    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        defFormat = self.getStyle(self.colors['default'])
        self.setFormat(0, len(text), defFormat)

        # Do other syntax formatting
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)
            # print expression, index
            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)


        strings = re.findall(r'(".*?")|(\'.*?\')', text)
        if '#' in text:
            copy = text
            if strings:
                pat = []
                for s in strings:
                    for match in s:
                        if match:
                            pat.append(match)
                for s in pat:
                    copy = copy.replace(s, '_'*len(s))
            if '#' in copy:
                index = copy.index('#')
                length = len(copy) - index
                self.setFormat(index, length, self.getStyle(self.colors['comment']))

        self.setCurrentBlockState(0)

        # Do multi-line strings
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)


    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings. ``delimiter`` should be a
        ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
        ``in_state`` should be a unique integer to represent the corresponding
        state changes when inside those strings. Returns True if we're still
        inside a multi-line string when this function is finished. """
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # Move past this match
            add = delimiter.matchedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + add)
            # Ending delimiter on this line?
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            # Apply formatting
            self.setFormat(start, length, style)
            # Look for the next match

            start = delimiter.indexIn(text, start + length)

        # Return True if still inside a multi-line string, False otherwise
        if self.currentBlockState() == in_state:
            return True
        else:
            return False


