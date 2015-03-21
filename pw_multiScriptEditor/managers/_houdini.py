import os, sys
import hou
import hqt
reload (hqt)

path = os.path.join(os.path.dirname(__file__), 'houdini')

main = __import__('__main__')
ns = main.__dict__
for mod in [os.path.splitext(x)[0] for x in os.listdir(path)]:
    if not mod in ns:
        try:
            exec 'import ' + mod in ns
        except:
            pass

if not path in sys.path:
    sys.path.insert(0, path)

from .. import scriptEditor
reload(scriptEditor)


def show(*args, **kwargs):
    hqt.show(scriptEditor.scriptEditorClass, *args, **kwargs)



# EXAMPLE SHELF BUTTON
# H13
# path = 'path/to/MultiScriptEditor_module'
# # example c:/houdini/python/lib
# if not path in sys.path:
#     sys.path.append(path)
# import pw_multiScriptEditor
# reload(pw_multiScriptEditor)
# pw_multiScriptEditor.showHoudini(ontop=1)

# H14
#import sys
# path = 'path/to/MultiScriptEditor_module'
# # example c:/houdini/python/lib
# if not path in sys.path:
#     sys.path.append(path)
# import pw_multiScriptEditor
# reload(pw_multiScriptEditor)
# pw_multiScriptEditor.showHoudini(name='Multi Script Editor',replacePyPanel=1, hideTitleMenu=0)