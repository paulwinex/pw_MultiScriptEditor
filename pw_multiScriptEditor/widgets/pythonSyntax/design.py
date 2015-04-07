import settingsManager
import os, re

EditorStyle = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'style', 'completer.qss')
if not os.path.exists(EditorStyle):
    EditorStyle=None

defaultColors = dict(
        background = (40,40,40),
        keywords = (65,255,130),
        digits = (250,255,62),
        definition = (255,160,250),
        operator = (230, 220, 110),
        extra = (110,180,230),
        methods = (120, 190, 205),
        comment = (110,100,100),
        string = (245,165,18),
        docstring = (130,160,75),
        boolean = (160,220,120),
        brace = (235,235,195),
        completer_text=(200,200,200),
        completer_selected_text= (105,105,105),
        completer_hover_text= (255,255,255),
        completer_background=(59,59,59),
        completer_alt_background= (65,65,65),
        completer_hover_background= (85,85,85),
        completer_selected_background= (123,123,123),
        default=(210,210,210)
)


def getColors(theme=False):
    s = settingsManager.scriptEditorClass()
    settings = s.readSettings()
    if not theme:
        theme = settings.get('theme')
    result = {k:v for k,v in defaultColors.items()}
    if theme:
        if 'colors' in settings:
            colors = settings['colors'].get(theme)
            if colors:
                for k, v in colors.items():
                    result[k] = v
    return result


def editorStyle(theme=None):
    colors = getColors(theme)
    colors = {k:tuple(v) if isinstance(v, list) else v for k,v in colors.items()}
    if EditorStyle:
        text = open(EditorStyle).read()
        proxys = re.findall('\[.*\]', text)
        for p in proxys:
            name = p[1:-1]
            if name in colors:
                text = text.replace(p, str(colors[name]))
        return text

def applyColorToEditorStyle(colors=None):
    if EditorStyle:
        text = open(EditorStyle).read()
        proxys = re.findall('\[.*\]', text)
        for p in proxys:
            name = p[1:-1]
            if name in colors:
                c = colors[name]
                if isinstance(c, list):
                    c = tuple(c)
                text = text.replace(p, str(c))
        return text
    return ''
