import json
import os
import codecs
from managers import context

settingsFilename = 'pw_scriptEditor_pref.json'

def userPrefFolder():
    appData = None
    if context == 'hou':
        appData = os.getenv('HOUDINI_USER_PREF_DIR')
    elif context == 'maya':
        appData = os.getenv('MAYA_APP_DIR')
    elif context == 'nuke':
        appData = os.path.join(os.environ['HOME'], '.nuke')
    if not appData:
        appData = os.getenv('HOME') or os.path.expanduser('~')
    return  appData

def settingsFile():
    path = os.path.normpath(os.path.join(userPrefFolder(), settingsFilename)).replace('\\','/')
    if not os.path.exists(path):
                with open(path, 'w') as f:
                    f.write('[]')
    return path


class scriptEditorClass(object):
    def __init__(self):
        super(scriptEditorClass, self).__init__()
        self.path = settingsFile()

    def readSettings(self):
        if os.path.exists(self.path) and os.path.isfile(self.path):
            with codecs.open(self.path, "r", "utf-16") as stream:
                try:
                    return json.load(stream)
                except:
                    return self.defaults()
        return self.defaults()

    def writeSettings(self, data):
        with codecs.open(self.path, "w", "utf-16") as stream:
            json.dump(data, stream, indent=4)

    def defaults(self):
        return dict(geometry=None,
                    outFontSize=8)

