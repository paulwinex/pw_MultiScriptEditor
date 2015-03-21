import os, sys
import hou
import hqt
reload (hqt)

path = os.path.join(os.path.dirname(__file__), 'houdini')

modules = os.listdir(path)

main = __import__('__main__')
ns = main.__dict__
for mod in [os.path.splitext(x)[0] for x in modules]:
    if not mod in ns:
        try:
            exec 'import ' + mod in ns
        except:
            pass


if not path in sys.path:
    sys.path.insert(0, path)

from .. import scriptEditor
reload(scriptEditor)

def selectionToCode():
    sel = hou.selectedNodes()
    if sel:
        code = []
        for s in sel:
            code.append(s.asCode())
        if len(code) == 1:
            return code[0]
        else:
            return '( %s )' % ', '.join(code)

def show(*args, **kwargs):
    hqt.show(scriptEditor.scriptEditorClass, *args, **kwargs)



# EXAMPLE SHELF BUTTON
# import os, sys
#
# pp = ['D:/Dropbox/Dropbox/pw_prefs/RnD/tools',
# 'D:/Dropbox/Dropbox/pw_prefs/RnD/tools/pw_scriptEditor']
# for p in pp:
#     if not p in sys.path:
#         sys.path.append(p)
#
# import pw_scriptEditor
# reload(pw_scriptEditor)
# pw_scriptEditor.showHoudini(name='Script Editor',replacePyPanel=1, hideTitleMenu=0)