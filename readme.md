# Multi Script Editor v2.0.4

![alt tag](http://www.paulwinex.ru/wp-content/uploads/2015/04/mse_banner.jpg)

#### [paulwinex.com](http://paulwinex.com/portfolio/multi-script-editor/)

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

  - Houdini 13-17
  - Nuke 8-10
  - Maya 2014-2017
  - 3DsMax 2014-2017
    
RV Integration in [nebukadhezer branch](https://github.com/nebukadhezer/multi_script_editor)

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


[Standalone](https://github.com/nebukadhezer/multi_script_editor)
[Houdini install](https://github.com/nebukadhezer/multi_script_editor)
[Maya install](https://github.com/nebukadhezer/multi_script_editor)
[Nuke install](https://github.com/nebukadhezer/multi_script_editor)
[3DsMax install](https://github.com/nebukadhezer/multi_script_editor)

You can use single module installation for each case. Just extract module `multi_script_editor`
to somewhere (no spaces and non ascii characters in path) and add this path to PYTHONPATH before start your app.

For example:

Extract to `'/home/username/myscripts/multi_script_editor'`

Add this path to PYTHONPATH environment variable

Windows:

`set PYTHONPATH=c:/users/username/myscripts`

Linux

`export PYTHONPATH=/home/username/myscripts`

Python

`os.environ['PYTHONPATH'] = '/home/username/myscripts'`

Do this for each app.

# License

This project is licensed under the MIT License
