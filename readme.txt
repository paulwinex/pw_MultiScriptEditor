1. Для работы потруебуется PySide
2. Для старта в Windows запусти run.bat
Если python.exe не прописан в PATH, исправь поть на абсолютный в файле run.bat
3. Для запуска в Houdini потребуется hqt.py: https://github.com/paulwinex/hqt
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