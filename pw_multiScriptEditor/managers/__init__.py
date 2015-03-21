main = __import__('__main__')
import platform

context = None
if 'hou' in main.__dict__:
    context = 'hou'
elif 'cmds' in main.__dict__:
    context = 'maya'
elif 'nuke' in main.__dict__:
    context = 'nuke'


if platform.system().lower() == 'windows':
    _s = 'w'
elif platform.system().lower() == 'darwin':
    _s = 'x'
else:
    _s = 'l'