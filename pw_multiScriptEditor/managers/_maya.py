from PySide.QtGui import *
from PySide.QtCore import *
import maya.OpenMayaUI as omui
from shiboken import wrapInstance as wrp
import os, sys, re
from managers.completeWidget import contextCompleterClass

main = __import__('__main__')
ns = main.__dict__
exec 'import pymel.core as pm' in ns
pm = main.__dict__['pm']

# jedi completion path
compPath = os.path.join(os.environ['MAYA_LOCATION'],'devkit/other/pymel/extras/completion/py').replace('\\','/')
if compPath in sys.path:
    sys.path.remove(compPath)
sys.path.insert(0, compPath)

def getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
    if ptr is not None:
        return wrp(long(ptr), QMainWindow)

def show(dock=False):
    if dock:
        showDickControl()
    else:
        showWindow()

def showWindow():
    from pw_multiScriptEditor import scriptEditor
    reload(scriptEditor)

    editor = scriptEditor.scriptEditorClass(parent=getMayaWindow())
    editor.show()


dockName = 'pw_scriptEditorDock'
name = 'pw_scriptEditor'
def clearDoc():
    if pm.dockControl(dockName, q=1, ex=1):
        pm.deleteUI(dockName)

def showDickControl():
    if pm.window(name, q=1, ex=1):
        pm.deleteUI(name)
    from pw_multiScriptEditor import scriptEditor
    reload(scriptEditor)
    editor = scriptEditor.scriptEditorClass(parent=getMayaWindow())
    clearDoc()
    pm.dockControl(dockName, area='left',
                 content=editor.objectName(),
                 width=700,
                 label='Multi Script Editor',
                 allowedArea=['right', 'left'])


# Shelf button example
# import sys
# path = 'path/to/MultiScriptEditor_module'
# # example c:/maya/python/lib
# if not path in sys.path:
#     sys.path.append(path)
# import pw_multiScriptEditor
# reload(pw_multiScriptEditor)
# pw_multiScriptEditor.showMaya(dock=True)


nodes = pm.allNodeTypes()

def completer(line, ns):
    # create node
    p = r"createNode\(['\"](\w*)$"
    m = re.search(p, line)
    if m:
        name = m.group(1)
        if name:
            auto = [x for x in nodes if x.lower().startswith(name.lower())]
            l = len(name)
            return [contextCompleterClass(x, x[l:], True) for x in auto], None
    # exists nodes
    p = r"PyNode\(['\"](\w*)$"
    m = re.search(p, line)
    if m:
        name = m.group(1)
        existsNodes = sorted(pm.cmds.ls())
        l = len(name)
        if name:
            auto = [x for x in existsNodes if x.lower().startswith(name.lower())]
            return [contextCompleterClass(x, x[l:], True) for x in auto], None
        else:
            return [contextCompleterClass(x, x, True) for x in existsNodes], None
    return None, None

# drop event

def wrapDroppedText(namespace, text, event):
    if event.keyboardModifiers() == Qt.AltModifier:
        # pymel with namespace
        for k, m in namespace.items():
            if hasattr(m, '__name__'):
                if m.__name__ == 'pymel.core' and not k == 'm':
                    syntax = []
                    for node in text.split():
                        if namespace[k].objExists(node):
                            syntax.append(k+'.PyNode("%s")' % node)
                        else:
                            syntax.append(node)
                    return '\n'.join(syntax)
        # pymel no namespace
        if 'PyNode' in namespace.keys():
            syntax = []
            for node in text.split():
                if namespace['objExists'](node):
                    syntax.append('PyNode("%s")' % node)
                else:
                    syntax.append(node)
            return '\n'.join(syntax)
                # return 'PyNode("%s")' % text

        # cmds with namespace
        for k, m in namespace.items():
            if hasattr(m, '__name__'):
                if m.__name__ == 'maya.cmds' and not k == 'm':
                    syntax = []
                    for node in text.split():
                        if namespace[k].objExists(node):
                            syntax.append('"%s"' % node)
                        else:
                            syntax.append(node)
                    return '\n'.join(syntax)
        # cmds without namespace
        if 'about' in namespace.keys():
            try:
                syntax = []
                for node in text.split():
                    if namespace['objExists'](node):
                        syntax.append('"%s"' % node)
                    else:
                        syntax.append(node)
                return '\n'.join(syntax)
            except:
                pass
    return text

def contextMenu(parent):
    m = mayaMenuClass(parent)
    return m

class mayaMenuClass(QMenu):
    def __init__(self, parent):
        super(mayaMenuClass, self).__init__('Maya', parent)
        self.par = parent
        self.setTearOffEnabled(1)
        self.setWindowTitle('MSE %s Maya' % self.par.ver)
        a = QAction('Save to shelf', parent, triggered=self.saveToShelfDialog)
        self.addAction(a)

    def saveToShelfDialog(self):
        dial = saveToShelfClass(self.par)
        dial.exec_()


class mayaIconsClass(QListWidget):
    def __init__(self, parent):
        super(mayaIconsClass, self).__init__()
        self.par = parent
        self.setWindowFlags(Qt.Tool)
        self.setViewMode(QListView.IconMode)
        self.setIconSize(QSize(32,32))
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setResizeMode(QListWidget.ResizeMode.Adjust)
        self.fillIcons()

    def fillIcons(self):
        res, files = self.getIcons()
        self.par.out.showMessage( "%s icons found" % len(res+files))
        for ico in sorted(res):
            item = QListWidgetItem(self)
            item.setIcon(QIcon(':/'+ico))
            item.setData(32, ':/'+ico)
            self.addItem(item)
        for f in sorted(files, key=lambda x: os.path.splitext(x)[0]):
            item = QListWidgetItem(self)
            item.setIcon(QIcon(f))
            item.setData(32, f)
            self.addItem(item)


    def getIcons(self):
        res = [ x for x in pm.resourceManager(nameFilter="*") if os.path.splitext(x)[1] in ['.png', '.svg'] ]
        files = []
        for env in 'XBMLANGPATH', 'MAYA_FILE_ICON_PATH':
            if os.getenv(env):
                paths = os.getenv(env).split(os.pathsep)
                for p in paths:
                    files += self.findInPath(p)
        return res, files

    def findInPath(self, path):
        result = []
        for path, dirs, files in os.walk(path):
            for f in files:
                if os.path.splitext(f)[1] in ['.png', '.svg'] :
                    result.append(os.path.join(path, f).replace('\\','/'))
        return result

class saveToShelfClass(QDialog):
    def __init__(self, parent):
        super(saveToShelfClass, self).__init__(parent)
        self.par = parent
        self.setWindowFlags(Qt.Tool)
        self.setObjectName('maya_create_shelfButton')
        self.setWindowTitle('Save script to shelf')
        self.verticalLayout = QVBoxLayout(self)
        self.gridLayout = QGridLayout()
        self.label = QLabel('Label')
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QLineEdit(self)
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.listWidget = mayaIconsClass(parent)
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QPushButton('Save to shelf')
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.createButton)

        center = parent.geometry().center()
        self.resize(450, 400)
        geo = self.geometry()
        geo.moveCenter(self.mapToGlobal(center))
        self.setGeometry(geo)

    def createButton(self):
        # topShelf = pm.mel.eval('$nul = $gShelfTopLevel')
        topShelf = pm.melGlobals['gShelfTopLevel']
        currentShelf = pm.tabLayout(topShelf, q=1, st=1)

        label = self.lineEdit.text()
        sel = self.listWidget.selectedItems()
        if sel:
            icon = sel[0].data(32)
        else:
            icon = 'pythonFamily.png'
        command = self.par.tab.getCurrentText()
        pm.shelfButton (
            parent=currentShelf,
            command=command,
            sourceType="python",
            label=label,
            imageOverlayLabel=label,
            image1=icon,
            style=pm.shelfLayout(currentShelf, query=1, style=1),
            width=pm.shelfLayout(currentShelf,query=1, cellWidth=1),
            height=pm.shelfLayout(currentShelf, query=1, cellHeight=1)
            )
        self.accept()

