# Multi Script Editor v2.0

![alt tag](http://www.paulwinex.ru/wp-content/uploads/2015/03/mse_git.png)

## [Go to tutorials](http://www.paulwinex.ru/multi-script-editor-v2-0/ )

Этот скрипт является Python редактором, который можно запустить как standalone приложение или встроить в другое приложение.
Главное условие интеграции - возможность скриптинга на Python.

### Основные возможности

  - сохранение и восстановление вкладок и кода в них
  - интерактивное выполнение выделенного кода по нажатию Ctrl+Enter
  - настройка цветовой темы редактора кода
  - автодополнение кода (модуль [jedi](https://github.com/davidhalter/jedi))

### Существующие модули интеграции

  - Houdini 13 и 14 (используется модуль [hqt.py](http://github.com/paulwinex/hqt ))
  - Nuke 8 и выше
  - Maya 2014
    
При необходимости вы можете сделать свой модуль интеграции используя имеющиеся в качестве примера. 
Основное условие - в программе должен использоваться Python 2.7.
 
# How to install

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

Also you can use .pypanel file without hqt module 
>/managers/houdini/pw_MultiScriptEditor.pypanel

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