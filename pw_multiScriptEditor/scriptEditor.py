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
from widgets import themeEditor
reload(themeEditor)
import managers
if managers._s == 'w':
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('paulwinex.multiscripteditor.1.0')
import icons_rcs
from icons import *

class scriptEditorClass(QMainWindow, ui.Ui_scriptEditor):
    def __init__(self, parent=None):
        super(scriptEditorClass, self).__init__(parent)
        # ui
        self.ver = '2.0.1'
        self.setupUi(self)
        self.setWindowTitle('PW Multi Script Editor v%s' % self.ver)
        self.setObjectName('pw_scriptEditor')
        # widgets
        self.out = outputWidget.outputClass()
        self.out_ly.addWidget(self.out)
        self.tab = tabWidget.tabWidgetClass(self)
        self.in_ly.addWidget(self.tab)
        #variables
        self.s = settingsManager.scriptEditorClass()
        self.namespace = {}
        self.dial = None

        self.updateNamespace({'mse_main':self,
                              'mse_version':self.ver,
                              'mse_out': self.out,
                              'mse_help': self.mse_help})
        self.session = sessionManager.sessionManagerClass()

        def fixButton(btn, ico):
            btn.setText('')
            btn.setFixedSize(QSize(32,32))
            btn.setIconSize(QSize(24,24))
            btn.setIcon(QIcon(icons[ico]))
        fixButton(self.executeAll_btn, 'all')
        fixButton(self.executeSel_btn, 'sel')
        fixButton(self.clearHistory_btn, 'clear')

        # connects
        self.executeAll_btn.clicked.connect(self.executeAll)
        self.executeSel_btn.clicked.connect(self.executeSelected)
        self.clearHistory_btn.clicked.connect(self.clearHistory)
        self.save_act.triggered.connect(self.saveScript)
        self.load_act.triggered.connect(self.loadScript)
        self.exit_act.triggered.connect(self.close)
        self.exit_act.setVisible(0)
        self.tabToSpaces_act.triggered.connect(self.tabsToSpaces)
        self.saveSeccion_act.triggered.connect(lambda:self.saveSession(True))
        self.settingsFile_act.triggered.connect(self.openSettingsFile)
        self.splitter.splitterMoved.connect(self.adjustColmpeters)
        self.donate_act.triggered.connect(lambda :self.openLink('donate'))
        self.openManual_act.triggered.connect(lambda :self.openLink('tutorials'))
        self.about_act.triggered.connect(self.about)
        self.shortcuts_act.triggered.connect(self.shortcuts)
        self.fillThemeMenu()

        #shortcuts
        if managers.context == 'nuke':
            import nuke
            if nuke.NUKE_VERSION_MAJOR>8:
                self.execSel_act.setShortcut('Ctrl+Return')
                self.execSel_act.setShortcutContext(Qt.ApplicationShortcut)
        self.execSel_act.triggered.connect(self.executeSelected)

        self.execAll_act.setShortcut('Ctrl+Shift+Return')
        self.execAll_act.triggered.connect(self.executeAll)
        self.execAll_act.setShortcutContext(Qt.ApplicationShortcut)

        self.clearHistory_act.triggered.connect(self.clearHistory)

        #start
        self.loadSession()
        self.loadSettings()
        self.setWindowStyle()
        self.out.showMessage('>>> PW Multi Script Editor v.%s' % self.ver)
        self.tab.widget(0).edit.setFocus()
        self.addArgs()


    def __del__(self):
        self.saveSession()

    def mse_help(self):
        txt = '''mse_main: main widget
mse_out: output widget
mse_version: current version
mse_help: show this text'''
        self.out.showMessage(txt)

    def closeEvent(self, event):
        self.saveSession()
        self.saveSettings()
        self.close()
        if __name__ == '__main__':
            sys.exit()

    def addArgs(self):
        f = sys.argv[-1]
        if os.path.exists(f):
            if not os.path.basename(f) == os.path.basename(__file__):
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
            qss = os.path.join(os.path.dirname(__file__),'style', 'style.qss')
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
                # print 'Error save file',path[0]
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

    def loadSettings(self):
        data = self.s.readSettings()
        if data['geometry']:
            self.move(data['geometry'][0], data['geometry'][1])
            self.resize(data['geometry'][2], data['geometry'][3])
        f =  self.out.font()
        f.setPointSize(data['outFontSize'])
        self.out.setFont(f)

    def saveSettings(self):
        settings = self.s.readSettings()
        geo = self.geometry()
        sGeo = [geo.x(), geo.y(), geo.width(), geo.height()]
        size = max(8, self.out.font().pointSize())
        data = dict(geometry=sGeo,
                    outFontSize=size)
        settings.update(data)
        self.s.writeSettings(settings)

    def openSettingsFile(self):
        path = settingsManager.userPrefFolder()
        self.out.showMessage('>>> Settings folder: %s' % path.replace('\\','/'))

        if os.path.exists(path):
            os.startfile(path)
        else:
            self.out.showMessage('>>> Not created!')

    def openThemeEditor(self):
        self.dial = themeEditor.themeEditorClass(self, self.tab.desk)
        self.dial.exec_()
        self.fillThemeMenu()

    def moveEvent(self, event):
        self.adjustColmpeters()
        super(scriptEditorClass, self).moveEvent(event)

    def adjustColmpeters(self):
        for i in range(self.tab.count()):
            w = self.tab.widget(i).edit
            if w.completer.isVisible():
                w.moveCompleter()

    def resizeEvent(self, event):
        self.adjustColmpeters()
        super(scriptEditorClass, self).resizeEvent(event)


    def openLink(self, name):
        from style.links import links
        webbrowser.open(links[name])

    def about(self):
        dial = about.aboutClass(self)
        dial.exec_()

    def shortcuts(self):
        dial = shortcuts.shortcutsClass(self)
        dial.exec_()

if __name__ == '__main__':
    app = QApplication([])
    w = scriptEditorClass()
    w.show()
    app.exec_()
