# Multi Script Editor v2.0

## How to install

### Standalone
    
  - install Python 2.7
  - install PySide
  - use run.cmd ot run.sh to start

### Houdini 13
    
  - download [hqt.py](http://github.com/paulwinex/hqt )
  - create new tool on shelf

```text
p = 'path/to/mulriscripteditor_modile'
# example c:/houdini/python/lib
if not p in sys.path:
    sys.path.append(p)
import pw_scriptEditor
reload(pw_scriptEditor)
pw_scriptEditor.showHoudini(ontop=1)
```
  
### Houdini 14

  - download [hqt.py](http://github.com/paulwinex/hqt )
  - create new tool on shelf
  
```text
import sys
p = 'path/to/mulriscripteditor_modile'
# example c:/houdini/python/lib
if not p in sys.path:
    sys.path.append(p)
import pw_scriptEditor
reload(pw_scriptEditor)
pw_scriptEditor.showHoudini(name='Multi Script Editor',replacePyPanel=1, hideTitleMenu=0)
```

### Maya

```text
import sys
p = 'path/to/mulriscripteditor_modile'
# example c:/houdini/python/lib
if not p in sys.path:
    sys.path.append(p)
import pw_scriptEditor
reload(pw_scriptEditor)
pw_scriptEditor.showMaya()
```

### Nuke

