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
path = 'path/to/mulriscripteditor_modile'
# example c:/houdini/python/lib
if not path in sys.path:
    sys.path.append(path)
import pw_scriptEditor
reload(pw_scriptEditor)
pw_scriptEditor.showHoudini(ontop=1)
```
  
### Houdini 14

  - download [hqt.py](http://github.com/paulwinex/hqt )
  - create new tool on shelf
  
```text
import sys
path = 'path/to/mulriscripteditor_modile'
# example c:/houdini/python/lib
if not path in sys.path:
    sys.path.append(path)
import pw_scriptEditor
reload(pw_scriptEditor)
pw_scriptEditor.showHoudini(name='Multi Script Editor',replacePyPanel=1, hideTitleMenu=0)
```

### Maya

```text
import sys
path = 'path/to/mulriscripteditor_modile'
# example c:/maya/python/lib
if not path in sys.path:
    sys.path.append(path)
import pw_scriptEditor
reload(pw_scriptEditor)
pw_scriptEditor.showMaya()
```

### Nuke

```text
# Add to menu.py
menubar = nuke.menu("Nuke")
toolMenu = menubar.addMenu('&Tools')
path = 'path/to/mulriscripteditor_modile'
# example c:/nuke/python/lib
if not path in sys.path:
    sys.path.append(path)

import pw_scriptEditor
# add to menu
toolMenu.addCommand("Multi Script Editor", "pw_scriptEditor.showNuke()")
# create new pane
pw_scriptEditor.showNuke(panel=True)
```