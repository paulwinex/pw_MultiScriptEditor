## v2.0.4
### Fix
  - comment/uncomment function
  - optimised Nuke library

## v2.0.3
### What new

#### Editor

  - added default text editors functions in Edit menu: undo, redo, copy, paste etc 
  - added Find and Replace window
  - auto indent on new line and new block after ":"
  - backspace remove 4 spaces
  - duplicate line or selected text by Ctrl+D
  - Alt+Q to comment/uncomment line or selected lines

#### Houdini

  - added app-context menu for Houdini
    - read python scripts from node sections or PythonSOP code
    - save python script to section or PythonSOP node
  - added Houdini path autocomplete. Path contains the absolute path to the Houdini node and its parameters
  - finished default Houdini autocomplete modules. Now all functions return correct types
  - added automatic wrap dragged nodes and parameters with ALT modifier (H14)
  - no need to import main module (hou) to make completer worked

#### Nuke

  - added app-context menu for Nuke
    - read script from PythonButtonKnob
    - save script to PythonButtonKnob
    - get selected nodes as code "nuke.toNode('<nodeName>')"
    - search nodes in clipboard text
  - added autocomplete for "toNode" function with existing nodes
  - added autocomplete for "allNodes" function with all node types (parameter "filter=")
  - finished default Nuke autocomplete modules. Now all functions return correct types
  - no need to import main module (import nuke) to make completer worked

#### Maya

  - added dock control mode for Maya
  - added context autocomplete for Maya function "PyNode" with existing nodes
  - added automatic wrap dragged nodes for Maya with ALT modifier

### Fix
  - some corrections output window
  - fast complete first line with Tab key or Enter key
  - fix menu stylesheet for stand alone
  - fixed line numbers widget for Houdini
  - now comments and doc strings have different colors in theme
  - editor format set to UTF8

--------------------------------------------

## v2.0.1
### What new
  - added context depended completer for 'createNode' function
    - Hodudini : createNode, createInputNode and createOutputNode
    - Maya: pm.createNode and cmds.createNode
    - Nuke: nuke.createNode and nuke.nodes

### Fix
  - move complete when widget geometry offscreen
  - Nuke 8 now worked
  - Maya 2015 now worked

--------------------------------------------

## v2.0
### What new
  - added auto complete
  - fix auto completion for Houdini
  - fix auto completion for Nuke

## v1.0

Not released