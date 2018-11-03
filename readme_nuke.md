## Nuke Install

  - extract module `multi_script_editor` to PYTHONPATH

    Example: `{HOME}/.nuke/multi_script_editor`
  - Add next code to menu.py:

```python

import multi_script_editor

# add to menu
menubar = nuke.menu("Nuke")
toolMenu = menubar.addMenu('&Tools')
toolMenu.addCommand("Multi Script Editor", multi_script_editor.showNuke)

# create new pane
multi_script_editor.showNuke(panel=True)
```
