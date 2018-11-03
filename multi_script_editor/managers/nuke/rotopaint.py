from main import Knob


class AnimAttributes(object):
    pass
class AnimCTransform(object):
    pass
class AnimControlPoint(object):
    pass
class AnimCurve(object):
    pass
class AnimCurveKey(object):
    pass
class AnimCurveViews(object):
    pass
class BaseCurve(object):
    pass
class CMatrix4(object):
    pass
class CTransform(object):
    pass
class CVec2(object):
    pass
class CVec3(object):
    pass
class CVec4(object):
    pass
class ControlPoint(object):
    pass
class CubicCurve(object):
    pass
class CurveKnob(Knob):
    curveWidget=None
    rootLayer=None
    def changed(self):
        """
Call this after performing updates on the tree, to tell it that it's been updated. For many operations this is called automatically, but you can call it manually for those cases where it isn't.

Returns: None
"""
    def toElement(self, path):
        """
Takes a path which identifies a particular element in the curve tree and returns the corresponding Layer, Stroke or Shape object. The path is a slash separated string and is always resolved relative to the root layer. So if, for example, you have a RotoPaint node with a layer called 'Layer1' which contains a shape called 'Shape1', the path to the shape would be 'Layer1/Shape1'. >>> knob = nuke.toNode('RotoPaint1)['curves'] >>> shape = knob.toElement('Layer1/Shape1') >>> shape.name 'Shape1'

Returns: Element
"""

class RotoKnob(CurveKnob):
    pass
class CurveType(object):
    pass
class Element(object):
    pass
class ExtrapolationType(object):
    pass
class Flag(object):
    pass
class FlagType(object):
    pass
class Hash(object):
    pass
class InterpolationType(object):
    pass
class Layer(object):
    pass
class RotationOrder(object):
    pass
class Shape(object):
    pass
class ShapeControlPoint(object):
    pass
class Stroke(object):
    pass
class TransformOrder(object):
    pass

def convertDirectoryToNuke6():
    pass
def convertDirectoryToNuke7():
    pass
def convertToNuke6():
    pass
def convertToNuke7():
    pass
