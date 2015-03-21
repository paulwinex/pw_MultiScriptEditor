# Multi Script Editor v2.0

![alt tag](http://www.paulwinex.ru/wp-content/uploads/2015/03/mse_git.png)

## [Tutorials](http://www.paulwinex.ru/multi-script-editor-v2-0/ )

## How to install

### Standalone
    
  - install Python 2.7
  - install PySide
  - use run.cmd (Windows) ot run.sh (Linux) to start

### Houdini 13
    
  - download [hqt.py](http://github.com/paulwinex/hqt )
  - create new tool on shelf

```python
path = 'path/to/MultiScriptEditor_module'
# example c:/houdini/python/lib
if not path in sys.path:
    sys.path.append(path)
import pw_multiScriptEditor
reload(pw_multiScriptEditor)
pw_multiScriptEditor.showHoudini(ontop=1)
```
  
### Houdini 14

  - download [hqt.py](http://github.com/paulwinex/hqt )
  - create new tool on shelf
  
```python
import sys
path = 'path/to/MultiScriptEditor_module'
# example c:/houdini/python/lib
if not path in sys.path:
    sys.path.append(path)
import pw_multiScriptEditor
reload(pw_multiScriptEditor)
pw_multiScriptEditor.showHoudini(name='Multi Script Editor',replacePyPanel=1, hideTitleMenu=0)
```

### Maya

  - create shelf button with code
```python
import sys
path = 'path/to/MultiScriptEditor_module'
# example c:/maya/python/lib
if not path in sys.path:
    sys.path.append(path)
import pw_multiScriptEditor
reload(pw_multiScriptEditor)
pw_multiScriptEditor.showMaya()
```

### Nuke

```python
# Add to menu.py
menubar = nuke.menu("Nuke")
toolMenu = menubar.addMenu('&Tools')
path = 'path/to/MultiScriptEditor_module'
# example c:/nuke/python/lib
if not path in sys.path:
    sys.path.append(path)

import pw_multiScriptEditor
# add to menu
toolMenu.addCommand("Multi Script Editor", "pw_multiScriptEditor.showNuke()")
# create new pane
pw_multiScriptEditor.showNuke(panel=True)
```