# Multi Script Editor v2.0.3

![alt tag](http://www.paulwinex.ru/wp-content/uploads/2015/04/mse_banner.jpg)

#### [paulwinex.ru](http://www.paulwinex.ru/multi-script-editor-v2-0/)

## [Tutorials](https://vimeo.com/channels/multiscripteditor)

This is a cross application, cross platform and open source Python editor, which can be run as a standalone application 
or embedded in another application. The main purpose for integration - the ability to script in Python.

### Key features

  - Preserve and load of tabs and code in them
  - Interactive execute of the selected code by pressing Ctrl + Enter
  - Adjust the color theme of the code editor
  - Code completion (module [jedi](https://github.com/davidhalter/jedi))
  - Context completion for different functions like existing nodes and path in scene

### Existing integration modules

  - Houdini 13 and 14 (using [hqt.py](http://github.com/paulwinex/hqt ) module)
  - Nuke 8,9
  - Maya 2014-2016
  - 3DsMax 2014-2016
    
If necessary, you can extend this to make your own integration module.
The main pre condition - Should be used Python2.7.
 

### Houdini features
  - Code completion for all modules and return types (remastered hou library)
  - Context completion for functions CreateNode, CreateInputNode and CreateOutputNode with existing houdini node types
  - Context completion string for absolute houdini internal path and node parameters. To use this complete start string with "/ or '/
  - Drag&Drop Houdini nodes and parameters fills in their path. Use Alt modifier to wrap node or parameter as code like in Houdini Python Shell.
  - Reading and writing to PythonSOP code and asset sections 
 
### Nuke features
  - Code completion for all modules and return types (remastered nuke library)
  - Context completion for createNode with existing Nuke node types
  - Context completion for function toNode with existing nodes in current script
  - Converting selected nodes to code with function nuke.toNode
  - Searching and converting nodes to code from clipboard
  - Reading and writing from PythonKnobs code
   
### Maya features
  - Save code to shelf and accept dropped shelf button code, like default Maya script editor
  - Drag&Drop Maya nodes fills in their names. Use Alt modifier to wrap node as code. Import PyMEL before doing this!
  - Context completion for function PyNode with existing nodes in current scene
  - Context completion for function pm.createNode and cmds.createNode with existing Maya node types

### 3DsMax features
  - Works for now...


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
paths = ['path/to/folder/with/MultiScriptEditor_module','path/to/default/python27/lib/with/PySide']
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
path = 'path/to/folder/with/MultiScriptEditor_module'
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
path = 'path/to/folder/with/MultiScriptEditor_module'
# example c:/maya/python/lib
if not path in sys.path:
    sys.path.append(path)
import pw_multiScriptEditor
pw_multiScriptEditor.showMaya(dock=True)
```

### Nuke

  - Add next code to menu.py
  
```python
import nuke
menubar = nuke.menu("Nuke")
toolMenu = menubar.addMenu('&Tools')
path = 'path/to/folder/with/MultiScriptEditor_module'
# example c:/nuke/python/lib
if not path in sys.path:
    sys.path.append(path)

import pw_multiScriptEditor
# add to menu
toolMenu.addCommand("Multi Script Editor", "pw_multiScriptEditor.showNuke()")
# create new pane
pw_multiScriptEditor.showNuke(panel=True)
```

### 3DsMax

  - Create a menu, toolbar, etc with the following maxscript:

```maxscript
python.executefile("path\\to\\pw_multiScriptEditor\\run_3dsmax.py")
```