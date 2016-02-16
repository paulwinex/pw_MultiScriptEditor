import os, sys

root = os.path.dirname(__file__)
if not root in sys.path:
    sys.path.append(root)


# HOUDINI
def showHoudini(clear=False, ontop=False, name=None, floating=False, position=(), size=(),
                pane=None, replacePyPanel=False, hideTitleMenu=True):
    """
    This method use hqt module. Download it before
    """
    from .managers import _houdini
    reload(_houdini)
    _houdini.show(clear=clear, ontop=ontop, name=name, floating=floating, position=position,
                  size=size, pane=pane, replacePyPanel=replacePyPanel, hideTitleMenu=hideTitleMenu)

# NUKE
def showNuke(panel=False):
    from .managers import _nuke
    reload(_nuke)
    _nuke.show(panel)


# MAYA
def showMaya(dock=False):
    from .managers import _maya
    reload (_maya)
    _maya.show(dock)

# 3DSMAX PLUS
def show3DSMax():
    from .managers import _3dsmax
    reload (_3dsmax)
    _3dsmax.show()