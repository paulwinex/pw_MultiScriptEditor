# Multi Script Editor v2.0.1

![alt tag](http://www.paulwinex.ru/wp-content/uploads/2015/03/mse_git.png)

## [Go to site](http://www.paulwinex.ru/multi-script-editor-v2-0/)

This is a cross application, cross platform and open source Python editor, which can be run as a standalone application 
or embedded in another application. The main purpose for integration - the ability to script in Python.

### Key features

  - Preserve and load of tabs and code in them
  - Interactive performance of the selected code by pressing Ctrl + Enter
  - Adjust the color theme of the code editor
  - Code completion (module [jedi](https://github.com/davidhalter/jedi))

### Existing integration modules

  - Houdini 13 and 14 (using [hqt.py](http://github.com/paulwinex/hqt ) module)
  - Nuke 8,9
  - Maya 2014, 2015
    
If necessary, you can extend this to make your own integration module.
The main pre condition - Should be used Python2.7.
 
 
# How to install

### Standalone
    
  - install Python 2.7
  - install PySide
  - use run.cmd (Windows) or run.sh (Linux) to start

### Houdini 13
    
  - download and install [hqt.py](http://github.com/paulwinex/hqt )
  - install PySide to default Python interpreter
  - create new tool on shelf

```python
import sys
paths = ['path/to/MultiScriptEditor_module','path/to/default/python27/lib/with/PySide']
# example ['c:/houdini/python/lib', 'c:/python27/Lib/site-packages']
for path in paths:
    if not path in sys.path:
        sys.path.append(path)
import pw_multiScriptEditor
pw_multiScriptEditor.showHoudini(ontop=1)
```
  
### Houdini 14

  - download and install [hqt.py](http://github.com/paulwinex/hqt )
  - create new tool on shelf
  
```python
import sys
path = 'path/to/MultiScriptEditor_module'
# example c:/houdini/python/lib
if not path in sys.path:
    sys.path.append(path)
import pw_multiScriptEditor
pw_multiScriptEditor.showHoudini(name='Multi Script Editor',replacePyPanel=1, hideTitleMenu=0)
```

Also you can use .pypanel file without hqt module 
>/managers/houdini/pw_MultiScriptEditor.pypanel

### Maya

  - Create shelf button with code
```python
import sys
path = 'path/to/MultiScriptEditor_module'
# example c:/maya/python/lib
if not path in sys.path:
    sys.path.append(path)
import pw_multiScriptEditor
pw_multiScriptEditor.showMaya()
```

### Nuke

  - Add next code to menu.py
  
```python
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
