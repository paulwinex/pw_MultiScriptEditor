from __future__ import with_statement
import json
import os
import codecs
import settingsManager

sessionFilename = 'pw_scriptEditor_session.json'


class sessionManagerClass(object):
    def __init__(self):
        self.path = os.path.normpath(os.path.join(settingsManager.userPrefFolder(), sessionFilename)).replace('\\','/')
        if not os.path.exists(self.path):
            f = open(self.path, 'w')
            f.write('{}')
            f.close()

    def readSession(self):
        if os.path.exists(self.path):
            with codecs.open(self.path, "r", "utf-16") as stream:
                try:
                    return json.load(stream)
                except:
                    return []
        return []

    def writeSession(self, data):
        with codecs.open(self.path, "w", "utf-16") as stream:
            json.dump(data, stream, indent=4)
        return self.path
