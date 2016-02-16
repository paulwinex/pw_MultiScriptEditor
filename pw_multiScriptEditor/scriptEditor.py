import traceback
import sys
import webbrowser
import os
from PySide.QtCore import *
from PySide.QtGui import *
from widgets import scriptEditor_UIs as ui, tabWidget, outputWidget, about, shortcuts
from widgets.pythonSyntax import design
reload(tabWidget)
reload(outputWidget)
import sessionManager
import settingsManager
from widgets import themeEditor, findWidget
reload(themeEditor)
reload(findWidget)
import managers
reload(managers)
if managers._s == 'w':
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('paulwinex.multiscripteditor.1.0')
import icons_rcs
from icons import *

class scriptEditorClass(QMainWindow, ui.Ui_scriptEditor):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        # ui
        self.ver = '2.0.3'
        self.setupUi(self)
        self.setWindowTitle('pw Multi Script Editor v%s' % self.ver)
        self.setObjectName('pw_scriptEditor')
        # widgets
        self.out = outputWidget.outputClass()
        self.out_ly.addWidget(self.out)
        self.tab = tabWidget.tabWidgetClass(self)
        self.in_ly.addWidget(self.tab)

        for m in self.file_menu, self.tools_menu, self.options_menu, self.run_menu, self.help_menu:
            m.setWindowTitle('MSE '+self.ver)

        #variables
        self.s = settingsManager.scriptEditorClass()
        # self.namespace = {}
        self.namespace = __import__('__main__').__dict__
        self.dial = None

        self.updateNamespace({'self_main':self,
                              'self_version':self.ver,
                              'self_output': self.out,
                              'self_help': self.mse_help,
                              'self_context':managers.context})
        self.session = sessionManager.sessionManagerClass()
        self.execAll_act.setIcon(QIcon(icons['all']))
        self.execSel_act.setIcon(QIcon(icons['sel']))
        self.clearHistory_act.setIcon(QIcon(icons['clear']))
        self.toolBar.setIconSize(QSize(32,32))
        self.menubar.setNativeMenuBar(False)
        # connects

        self.save_act.triggered.connect(self.saveScript)
        self.load_act.triggered.connect(self.loadScript)
        self.exit_act.triggered.connect(self.close)
        self.tabToSpaces_act.triggered.connect(self.tabsToSpaces)
        self.saveSeccion_act.triggered.connect(lambda:self.saveSession(True))
        self.settingsFile_act.triggered.connect(self.openSettingsFile)
        self.splitter.splitterMoved.connect(self.adjustColmpeters)
        self.donate_act.triggered.connect(lambda :self.openLink('donate'))
        self.openManual_act.triggered.connect(lambda :self.openLink('manual'))
        self.about_act.triggered.connect(self.about)
        self.shortcuts_act.triggered.connect(self.shortcuts)
        self.printHelp_act.triggered.connect(self.mse_help)
        # editor
        c = Qt.WindowShortcut
        self.undo_act.triggered.connect(self.tab.undo)
        self.undo_act.setShortcut('Ctrl+Z')
        self.undo_act.setShortcutContext(Qt.WidgetShortcut)

        self.redo_act.triggered.connect(self.tab.redo)
        self.redo_act.setShortcut('Ctrl+Y')
        self.redo_act.setShortcutContext(Qt.WidgetShortcut)

        self.copy_act.triggered.connect(self.tab.copy)
        self.copy_act.setShortcut('Ctrl+C')
        self.copy_act.setShortcutContext(Qt.WidgetShortcut)

        self.cut_act.triggered.connect(self.tab.cut)
        self.cut_act.setShortcut('Ctrl+X')
        self.cut_act.setShortcutContext(Qt.WidgetShortcut)

        self.paste_act.triggered.connect(self.tab.paste)
        self.paste_act.setShortcut('Ctrl+V')
        self.paste_act.setShortcutContext(Qt.WidgetShortcut)

        self.find_act.triggered.connect(self.findWidget)
        self.find_act.setShortcut('Ctrl+F')
        self.find_act.setShortcutContext(Qt.WindowShortcut)

        self.comment_cat.triggered.connect(self.tab.comment)
        self.comment_cat.setShortcut(QKeySequence( Qt.ALT+Qt.Key_Q))
        self.comment_cat.setShortcutContext(Qt.WidgetShortcut)

        self.fillThemeMenu()

        #shortcuts
        if managers.context == 'nuke':
            import nuke
            if nuke.NUKE_VERSION_MAJOR>8:
                self.execSel_act.setShortcut('Ctrl+Return')
                self.execSel_act.setShortcutContext(Qt.ApplicationShortcut)

        self.execSel_act.triggered.connect(self.executeSelected)
        self.execSel_act.setShortcut('Ctrl+Return')
        self.execSel_act.setShortcutContext(Qt.WidgetWithChildrenShortcut)

        self.execAll_act.setShortcut('Ctrl+Shift+Return')
        self.execAll_act.triggered.connect(self.executeAll)
        self.execAll_act.setShortcutContext(Qt.ApplicationShortcut)

        self.clearHistory_act.triggered.connect(self.clearHistory)

        #start
        self.loadSession()
        self.loadSettings()
        self.setWindowStyle()
        self.out.showMessage('>>> pw Multi Script Editor v.%s\npaulwinex.ru' % self.ver)
        self.tab.widget(0).edit.setFocus()
        self.appContextMenu()
        self.addArgs()

    def __del__(self):
        self.saveSession()

    def mse_help(self):
        src = os.path.join(os.path.dirname(__file__), 'helpText.txt')
        if os.path.exists(src):
            txt = open(src).read() % self.ver
        else:
            txt = '<h3>File not found: helpText.txt</h3><br>'
        old = self.out.toPlainText().replace('\n', '<br>')
        self.out.setHtml(old+txt)
        self.out.moveCursor(QTextCursor.End)
        self.out.ensureCursorVisible()

    def closeEvent(self, event):
        self.saveSession()
        self.saveSettings()
        self.close()
        if __name__ == '__main__':
            sys.exit()
        # if managers.context == 'maya':
        #     from managers import _maya
        #     _maya.clearDoc()

    def appContextMenu(self):
        if managers.context in managers.contextMenus:
            menu = managers.contextMenus[managers.context](self)
            # menu.setStyleSheet(self.styleSheet())
            self.menubar.insertMenu(self.menubar.actions()[0], menu)
            return menu

    def addArgs(self):
        f = sys.argv[-1]
        if os.path.exists(f):
            if not os.path.basename(f) == os.path.basename(__file__):
                if os.path.splitext(f)[-1] in ['.txt', '.py']:
                    self.out.showMessage( os.path.splitext(f)[-1])
                    self.out.showMessage('Open File: '+f)
                    text = open(f).read()
                    self.tab.addNewTab(os.path.basename(f), text)

    def fillThemeMenu(self):
        self.theme_menu.clear()
        self.theme_menu.addAction(QAction('Edit...', self, triggered=self.openThemeEditor))
        self.theme_menu.addSeparator()
        self.theme_menu.addAction(QAction('default', self, triggered=lambda: self.applyTheme('default')))
        data = self.s.readSettings()
        if data.get('colors'):
            for t in data.get('colors').keys():
                self.theme_menu.addAction(QAction(t, self, triggered=lambda x=t: self.applyTheme(x)))

    def applyTheme(self, name):
        for i in range(self.tab.count()):
            w = self.tab.widget(i)
            qss = design.editorStyle(name)
            # text color
            w.edit.applyHightLighter(name)
            #completer
            w.edit.completer.setStyleSheet(qss)
            #editor
            w.edit.setStyleSheet(qss)
        s = self.s.readSettings()
        s['theme'] = name
        self.s.writeSettings(s)

    def setWindowStyle(self):
        if __name__ == '__main__':
            qss = os.path.join(os.path.dirname(__file__),'style', 'style.css')
            if os.path.exists(qss):
                self.setStyleSheet(open(qss).read())
                self.setWindowIcon(QIcon(icons['pw']))

    def loadSession(self):
        sessions = self.session.readSession()
        self.tab.clear()
        active = 0
        if sessions:
            for i, s in enumerate(sessions):
                w= self.tab.addNewTab(s['name'], s['text'])
                if s['active']:
                    active = i
                w.setFontSize(s.get('size', None))
        else:
            self.tab.addNewTab()
        self.tab.setCurrentIndex(active)

    def saveSession(self, verbos=False):
        tabs= []
        index = self.tab.currentIndex()
        for item in range(self.tab.count()):
            name = self.tab.tabText(item)
            text = self.tab.getTabText(item)
            if managers.context == 'hou':
                size = self.tab.widget(item).edit.fs
            else:
                size = self.tab.widget(item).edit.font().pointSize()
            tab = {'name':name,
                   'text':text,
                   'active': item == index,
                   'size': size}
            tabs.append(tab)
        path = self.session.writeSession(tabs)
        if verbos:
            self.out.showMessage('>>> Session saved: %s' % path.replace('\\','/'))

    def executeAll(self):
        allText = self.tab.getCurrentText()
        if allText:
            self.executeCommand(allText.strip())

    def executeSelected(self):

        text = self.tab.getCurrentSelectedText()
        if text:
            self.executeCommand(text)

    def updateNamespace(self, namespace):
        self.namespace.update(namespace)
        # md = __import__('__main__').__dict__
        # md['mse'] = self.namespace

    def executeCommand(self, cmd):
        self.out.showMessage(cmd)
        self.runCommand(cmd)

    def runCommand(self, command=None):
        if command:
            tmp_stdout = sys.stdout
            class stdoutProxy():
                def __init__(self, write_func):
                    self.write_func = write_func
                    self.skip = False

                def write(self, text):
                    if not self.skip:
                        stripped_text = text.rstrip('\n')
                        self.write_func(stripped_text)
                        QCoreApplication.processEvents()
                    self.skip = not self.skip

            sys.stdout = stdoutProxy(self.out.showMessage)
            try:
                try:
                    result = eval(command, self.namespace, self.namespace)
                    if result != None:
                        self.out.showMessage(repr(result))

                except SyntaxError:
                    exec command in self.namespace
            except SystemExit:
                self.close()
            except:
                traceback_lines = traceback.format_exc().split('\n')
                for i in (3, 2, 1, -1):
                    traceback_lines.pop(i)
                self.out.showMessage('\n'.join(traceback_lines))
            sys.stdout = tmp_stdout
            # __import__("__main__").__dict__.update(self.namespace)

    def clearHistory(self):
        self.out.setText('')

    def saveScript(self):
        text = self.tab.getCurrentText()
        d = os.getenv('HOME')
        if not d:
            d = os.path.expanduser('~')
        path = QFileDialog.getSaveFileName (self, 'Save script', d, "PY Files (*.py)")
        if path[0]:
            try:
                with open(path[0], 'w') as f:
                    f.write(text)
            except:
                self.out.showMessage('Error save file; %s' % path[0])

    def loadScript(self):
        d = os.getenv('HOME')
        if not d:
            d = os.path.expanduser('~')
        path = QFileDialog.getOpenFileName(self, 'Open script', d, "PY Files (*.py)")
        if path[0]:
            if os.path.exists(path[0]):
                text = open(path[0]).read()
                self.tab.addNewTab(os.path.basename(path[0]), text)

    def tabsToSpaces(self):
        text = self.tab.getCurrentText()
        text = text.replace('\t','    ')
        self.tab.setCurrentText(text)

    def insertText(self, text):
        self.tab.addToCurrent(text)

    def loadSettings(self):
        data = self.s.readSettings()
        if data['geometry']:
            self.move(data['geometry'][0], data['geometry'][1])
            self.resize(data['geometry'][2], data['geometry'][3])
        if data.get('center'):
            x, y = data.get('center')
            geo = self.geometry()
            geo.moveCenter(QPoint(x,y))
            self.setGeometry(geo)
        f =  self.out.font()
        f.setPointSize(data['outFontSize'])
        self.out.setFont(f)

    def saveSettings(self):
        settings = self.s.readSettings()
        geo = self.geometry()
        sGeo = [geo.x(), geo.y(), geo.width(), geo.height()]
        center = [geo.center().x(),geo.center().y()]
        size = max(8, self.out.font().pointSize())
        data = dict(geometry=sGeo,
                    center=center,
                    outFontSize=size)
        settings.update(data)
        self.s.writeSettings(settings)

    def openSettingsFile(self):
        path = settingsManager.userPrefFolder()
        self.out.showMessage('>>> Settings folder: %s' % path.replace('\\','/'))

        if os.path.exists(path):
            self.openFolder(path)
        else:
            self.out.showMessage('>>> Not created!')

    def openThemeEditor(self):
        self.dial = themeEditor.themeEditorClass(self, self.tab.desk)
        self.dial.exec_()
        self.fillThemeMenu()

    def moveEvent(self, event):
        self.adjustColmpeters()
        # super(scriptEditorClass, self).moveEvent(event)
        QMainWindow.moveEvent(self, event)

    def adjustColmpeters(self):
        for i in range(self.tab.count()):
            w = self.tab.widget(i).edit
            if w.completer.isVisible():
                w.moveCompleter()

    def resizeEvent(self, event):
        self.adjustColmpeters()
        # super(scriptEditorClass, self).resizeEvent(event)
        QMainWindow.resizeEvent(self, event)


    def openLink(self, name):
        from style.links import links
        webbrowser.open(links[name])

    def about(self):
        dial = about.aboutClass(self)
        dial.exec_()

    def shortcuts(self):
        dial = shortcuts.shortcutsClass(self)
        dial.exec_()

    def findWidget(self):
        w = findWidget.findWidgetClass(self.out)
        w.searchSignal.connect(self.tab.search)
        w.replaceSignal.connect(self.tab.replace)
        w.replaceAllSignal.connect(self.tab.replaceAll)
        w.show()
        w.activateWindow()

    def openFolder(self, path):
        if os.name == 'nt':
            os.startfile(path)
        elif os.name == 'posix':
            os.system('xdg-open "%s"' % path)
        elif os.name =='os2':
            os.system('open "%s"' % path)

QTextCodec.setCodecForCStrings(QTextCodec.codecForName("UTF-8"))

if __name__ == '__main__':
    app = QApplication([])
    w = scriptEditorClass()
    w.show()
    app.exec_()
