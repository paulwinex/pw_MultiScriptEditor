## Houdini install

### Houdini 13

  - install PySide to default Python interpreter
  - create new tool on shelf
  - extract module `multi_script_editor` to PYTHONPATH

    Example: `{HOME}/Documents/Houdini13.X/scripts/python/multi_script_editor`

```python
import multi_script_editor
multi_script_editor.showHoudini(ontop=1)
```

### Houdini 14+

  - extract module `multi_script_editor` to PYTHONPATH

    Example: `{HOME}/Documents/Houdini13.X/scripts/python/multi_script_editor`
  - create new tool on shelf

```python
import multi_script_editor
multi_script_editor.showHoudini(name='Multi Script Editor', replacePyPanel=1, hideTitleMenu=0)
```

Also you can use .pypanel file without hqt module
>/managers/houdini/multi_script_editor_16.pypanel (for Houdini 14-16)
>/managers/houdini/multi_script_editor_17.pypanel (for Houdini 17+)
