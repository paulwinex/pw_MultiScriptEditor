import sys, os
path = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
if not path in sys.path:
    sys.path.append(path)
print path
import pw_multiScriptEditor
reload(pw_multiScriptEditor)
pw_multiScriptEditor.show3DSMax()