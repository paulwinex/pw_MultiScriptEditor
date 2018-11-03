## 3DsMax Install
  - extract module `multi_script_editor` to PYTHONPATH

    Example: `{MAX_INSTALL_DIR}/python/multi_script_editor`
  - create a menu, toolbar, etc with the following maxscript:

```maxscript
python.executefile("path\\to\\multi_script_editor\\managers\\run_3dsmax.py")
```
or
```
macroScript MultiScriptEditor
	category:"scripts"
	toolTip:"MultiScriptEditor"
(
	python.Execute "import multi_script_editor"
	python.Execute "multi_script_editor.show3DSMax()"
)

```