# Multi Script Editor v2.0

## How to install

### Standalone
    
    - install Python 2.7
    - install PySide
    - use run.cmd ot run.sh to start

### Houdini
    
    - download [hqt.py](http://github.com/paulwinex/hqt )
Код для Houdini:
import sys

p = 'путь к модулю'
if not p in sys.path:
    sys.path.append(p)
import pw_scriptEditor
reload(pw_scriptEditor)
pw_scriptEditor.showHoudini()

4. Для запуска в майке код:

import sys
p = 'путь к модулю'
if not p in sys.path:
    sys.path.append(p)
import pw_scriptEditor
reload(pw_scriptEditor)
pw_scriptEditor.showMaya()

5. Код для Nuke:
в разработке...