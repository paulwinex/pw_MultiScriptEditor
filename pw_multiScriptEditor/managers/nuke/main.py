import math, geo

# KNOB
class KnobType(object):
    pass

class _Knob(object):
    """
    Fake class for default methods in all Knobs. Not Nuke default class !!!!
    Used for auto comlete
    """
    def __init__(self,name, label, *flags):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass
    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass
    def clearAnimated(self):
        """Clear animation for channel 'c'. Return True if successful."""
        pass

    def setLabel(self,s):
        """self.setLabel(s) -> None.
@param s: New label.
@return: None.
"""
        pass

    def setTooltip(self,s):
        """self.setTooltip(s) -> None.
@param s: New tooltip.
@return: None.
"""
        pass

    def removeKey(self):
        """Remove key for channel 'c'. Return True if successful."""
        pass

    def removeKeyAt(self):
        """Remove key at time 't' for channel 'c'. Return True if successful."""
        pass

    def visible(self):
        """self.visible() -> Boolean.

@return: True if the knob is visible, False if it's hidden."""
        pass

    def warning(self,message):
        """self.warning(message) -> None.
@param message: message to put a warning on the knob.
@return: None.
"""
        pass

    def getIntegral(self):
        """Return integral at the interval [t1, t2] for channel 'c'."""
        pass

    def isKeyAt(self):
        """Return True if there is a keyframe at time 't' for channel 'c'."""
        pass

    def hasExpression(self,index=-1):
        """self.hasExpression(index=-1) -> bool
Return True if animation at index 'index' has an expression.
@param index: Optional index parameter. Defaults to -1 if not specified. This can be specified as a keyword parameter if desired.
@return: True if has expression, False otherwise.
"""
        pass

    def getKeyTime(self):
        """Return index of the keyframe at time 't' for channel 'c'."""
        pass

    def tooltip(self):
        """self.tooltip() -> tooltip.
@return: tooltip.
"""
        return ''

    def label(self):
        """self.label() -> label.
@return: label.
"""
        return ''

    def setFlag(self,f):
        """self.setFlag(f) -> None.
Logical OR of the argument and existing knob flags.
@param f: Flag.
@return: None.
"""
        pass

    def getNumKeys(self):
        """Return number of keyframes for channel 'c'."""
        pass

    def critical(self,message):
        """self.critical(message) -> None.
@param message: message to put the knob in error, and do a popup.
@return: None.
"""
        pass

    def toScript(self):
        """toScript(quote, context=current) -> string.

Return the value of the knob in script syntax.
Pass True for quote to return results quoted in {}.
Pass None for context to get results for all views and key times (as stored in a .nk file)."""
        return ''

    def clearFlag(self,f):
        """self.clearFlag(f) -> None.
Clear flag.
@param f: Flag.
@return: None.
"""
        pass

    def Class(self):
        """self.Class() -> Class name.
@return: Class name.
"""
        return ''

    def node(self):
        """self.node() -> nuke.Node
Return the node that this knob belongs to. If the node has been cloned, we'll always return a reference to the original.
@return: The node which owns this knob, or None if the knob has no owner yet."""
        return Node()

    def setEnabled(self,enabled):
        """self.setEnabled(enabled) -> None.

Enable or disable the knob.
@param enabled: True to enable the knob, False to disable it."""
        pass

    def setValue(self, val, chan):
        """self.setValue(val, chan) -> bool

Sets the value 'val' at channel 'chan'.
@return: True if successful, False if not."""
        return  True

    def setName(self,s):
        """self.setName(s) -> None.
@param s: New name.
@return: None.
"""
        pass

    def isAnimated(self):
        """Return True if channel 'c' is animated."""
        pass

    def setAnimated(self, chan):
        """Set channel 'c' to be animated."""
        pass

    def getDerivative(self):
        """Return derivative at time 't' for channel 'c'."""
        pass

    def setExpression(self,expr, channel=-1, view=None):
        """self.setExpression(expr, channel=-1, view=None) -> bool
Set the expression for a knob. You can optionally specify a channel to set the expression for.

@param expr: The new expression for the knob. This should be a string.
@param channel: Optional parameter, specifying the channel to set the expression for. This should be an integer.
@param view: Optional view parameter. Without, this command will set the expression for the current view theinterface is displaying. Can be the name of the view or the index.
@return: True if successful, False if not."""
        pass

    def setValueAt(self,val, time, chan):
        """self.setValueAt(val, time, chan) -> bool

Sets the value 'val' at channel 'chan' for time 'time'.
@return: True if successful, False if not."""
        pass

    def getNthDerivative(self):
        """Return nth derivative at time 't' for channel 'c'."""
        pass

    def getValueAt(self):
        """Return value at time 't' for channel 'c'."""
        pass

    def name(self):
        """self.name() -> name.
@return: name.
"""
        return ''

    def isKey(self):
        """Return True if there is a keyframe at the current frame for channel 'c'."""
        pass

    def fromScript(self):
        """Initialise from script."""
        pass

    def enabled(self):
        """self.enabled() -> Boolean.

@return: True if the knob is enabled, False if it's disabled."""
        pass

    def value(self):
        """Return value at the current frame for channel 'c'."""
        pass

    def getValue(self):
        """Return value at the current frame for channel 'c'."""
        pass

    def getKeyIndex(self):
        """Return keyframe index at time 't' for channel 'c'."""
        pass

    def error(self,message):
        """self.error(message) -> None.
@param message: message to put the knob in error.
@return: None.
"""
        pass

    def debug(self,message):
        """self.debug(message) -> None.
@param message: message to put out to the error console, attached to the knob, if the verbosity level is set high enough.
@return: None.
"""
        pass

    def setVisible(self,visible):
        """self.setVisible(visible) -> None.

Show or hide the knob.
@param visible: True to show the knob, False to hide it."""
        pass

    def animation(self, i):
        return AnimationCurve()

    def animations(self,view):
        """self.animations(view) -> AnimationCurve list.
@param view: Optional view.
@return: AnimationCurve list.
Example:
b = nuke.nodes.Blur()
k = b['size']
k.setAnimated(0)
a = k.animations()
a[0].setKey(0, 11)
a[0].setKey(10, 20)
"""
        return [AnimationCurve(),]


class Font_Knob(_Knob):

    def value(self):
        """None"""
        return ''

    def setValue(self):
        """None"""
        pass

class Array_Knob(_Knob):
    def clearAnimated(self, index, view):
        """self.clearAnimated(index, view) -> True if succeeded, False otherwise.
Delete animation.
@param index: Optional index.
@param view: Optional view.
@return: True if succeeded, False otherwise.
"""
        pass

    def removeKey(self, index, view):
        """self.removeKey(index, view) -> True if succeeded, False otherwise.
Remove key.
@param index: Optional index.
@param view: Optional view.
@return: True if succeeded, False otherwise.
"""
        pass

    def setValueAt(self, value, time, index, view):
        """self.setValueAt(value, time, index, view) -> bool.
Set value of element 'index' at time for view. If the knob is animated, it will set a new keyframe or change an existing one. Index and view are optional. Return True if successful.
@param value: Floating point value.
@param time: Time.
@param index: Optional index.
@param view: Optional view.
@return: True if value changed, False otherwise. Safe to ignore.
"""
        pass

    def frame(self):
        """self.frame() -> Frame number.
@return: Frame number.
"""
        return 0

    def removeKeyAt(self, time, index, view):
        """self.removeKeyAt(time, index, view) -> True if succeeded, False otherwise.
Remove keyframe at specified time, optional index and view. Return True if successful.
@param time: Time.
@param index: Optional index.
@param view: Optional view.
@return: True if succeeded, False otherwise.
"""
        pass

    def height(self):
        """self.height() -> Height of array of values.
@return: Height of array of values.
"""
        return 0

    def minimum(self):
        """self.min() -> Minimum value.
@return: Minimum value.
"""
        return 0

    def unsplitView(self,view):
        """self.unsplitView(view) -> None.
Unsplit the view so that it shares a value with other views.
@param view: Optional view. Default is current view.
@return: None.
"""
        pass

    def array(self):
        """self.array() -> List of knob values.
@return: List of knob values.
"""
        return [0,]

    def getIntegral(self):
        """Return integral at time interval [t1, t2] and index 'i'."""
        pass

    def singleValue(self,view):
        """self.singleValue(view) -> True if holds a single value.
@param view: Optional view. Default is current view.
@return: True if holds a single value.
"""
        return [0,0]

    def isKeyAt(self, time, index, view):
        """self.isKeyAt(time, index, view) -> True if succeeded, False otherwise.
Returns True if there is a keyframe at specified time, optional index and view, otherwise returns False.
@param time: Time.
@param index: Optional index.
@param view: Optional view.
@return: True if succeeded, False otherwise.
"""
        pass

    def hasExpression(self,index):
        """self.hasExpression(index) -> True if has expression, False otherwise.
@param index: Optional index.
@return: True if has expression, False otherwise.
"""
        pass

    def setKeyAt(self, time, index, view):
        """self.setKeyAt(time, index, view) -> None.
Set a key on element 'index', at time and view.
@param time: Time.
@param index: Optional index.
@param view: Optional view.
@return: None.
"""
        pass

    def min(self):
        """self.min() -> Minimum value.
@return: Minimum value.
"""
        return 0

    def defaultValue(self):
        """self.defaultValue() -> Default value.
@return: Default value.
"""
        return 0

    def getKeyTime(self):
        """Return time of the keyframe at time 't' and channel 'c'."""
        return 0

    def deleteAnimation(self,curve):
        """self.deleteAnimation(curve) -> None. Raises ValueError if not found.
Deletes the AnimationCurve.
@param curve: An AnimationCurve instance which belongs to this Knob.
@return: None. Raises ValueError if not found.
"""
        pass

    def width(self):
        """self.width() -> Width of array of values.
@return: Width of array of values.
"""
        return 0

    def getNumKeys(self):
        """Return number of keys at channel 'c'."""
        return 0

    def valueAt(self, time, index, view):
        """self.valueAt(time, index, view) -> Floating point or List of floating point values (in case some are different).
Return value for this knob at specified time, optional index and view.
@param time: Time.
@param index: Optional index. Default is 0.
@param view: Optional view.
@return: Floating point or List of floating point values (in case some are different).
"""
        return 0.0

    def arraySize(self):
        """self.arraySize() -> Number of elements in array.
@return: Number of elements in array.
"""
        return 0

    def max(self):
        """self.max() -> Maximum value.
@return: Maximum value.
"""
        return 0

    def setSingleValue(self,b, view):
        """self.setSingleValue(b, view) -> None.
Set to just hold a single value or not.
@param b: Boolean object.
@param view: Optional view. Default is current view.
@return: None.
"""
        pass

    def toScript(self,quote, context):
        """self.toScript(quote, context) -> String.
Return the value of the knob in script syntax.
@param quote: Optional, default is False. Specify True to return the knob value quoted in {}.
@param context: Optional context, default is current, None will be "contextless" (all views, all keys) as in a .nk file.
@return: String.
"""
        return ''

    def notDefault(self):
        """self.notDefault() -> True if any of the values is not set to the default, False otherwise.
@return: True if any of the values is not set to the default, False otherwise.
"""
        pass

    def splitView(self, view):
        """self.splitView(view) -> None.
Split the view away from the current knob value.
@param view: Optional view. Default is current view.
@return: None.
"""
        pass

    def setValue(self,value, index=0, time=0, view=None):
        """self.setValue(value, index, time, view) -> True if value changed, False otherwise. Safe to ignore.
Set index to value at time and view.
@param value: Floating point value.
@param index: Optional index.
@param time: Optional time.
@param view: Optional view.
@return: True if value changed, False otherwise. Safe to ignore.
"""
        pass

    def isAnimated(self,curves, view):
        """self.isAnimated(index, view) -> True if animated, False otherwise.
@param index: Optional index.
@param view: Optional view.
@return: True if animated, False otherwise.
"""
        pass

    def copyAnimations(self, curves, view):
        """self.copyAnimations(curves, view) -> None.
Copies the AnimationCurves from curves to this object. The view is optional and defaults to the current view.
@param curves: AnimationCurve list.
@param view: Optional view. Defaults to current.
@return: None.
"""
        pass

    def setDefaultValue(self,s):
        """self.setDefaultValue(s) -> None.
@param s: Sequence of floating-point values.
@return: None.
"""
        pass

    def dimensions(self):
        """self.dimensions() -> Dimensions in array.
@return: Dimensions in array.
"""
        return 0

    def vect(self):
        """self.vect() -> List of knob values.
@return: List of knob values.
"""
        return [0,]

    def animations(self,view):
        """self.animations(view) -> AnimationCurve list.
@param view: Optional view.
@return: AnimationCurve list.
Example:
b = nuke.nodes.Blur()
k = b['size']
k.setAnimated(0)
a = k.animations()
a[0].setKey(0, 11)
a[0].setKey(10, 20)
"""
        return [AnimationCurve(),]

    def setAnimated(self, index, view):
        """self.setAnimated(index, view) -> True if succeeded, False otherwise.
Create an Animation object. Return True if successful, in which case caller must initialise it by calling setValue() or setValueAt().
@param index: Optional index.
@param view: Optional view.
@return: True if succeeded, False otherwise.
"""
        pass

    def getDerivative(self, t, i):
        """Return derivative at time 't' and index 'i'."""
        pass

    def setExpression(self, expr, channel=-1, view=None):
        """self.setExpression(expr, channel=-1, view=None) -> bool
Set the expression for a knob. You can optionally specify a channel to set the expression for.

@param expr: The new expression for the knob. This should be a string.
@param channel: Optional parameter, specifying the channel to set the expression for. This should be an integer.
@param view: Optional view parameter. Without, this command will set the expression for the current view theinterface is displaying. Can be the name of the view or the index.
@return: True if successful, False if not."""
        pass

    def animation(self, chan, view):
        """self.animation(chan, view) -> AnimationCurve or None.
Return the AnimationCurve for the  channel 'chan' and view 'view'. The view argument is optional.
@param channel: The channel index.
@param view: Optional view.
@return: AnimationCurve or None.
"""
        return AnimationCurve()

    def resize(self, w, h):
        """self.resize(w, h) -> True if successful, False otherwise.
Resize the array.
@param w: New width
@param h: Optional new height
@return: True if successful, False otherwise.
"""
        pass

    def setRange(self, f1, f2):
        """self.setRange(f1, f2) -> None.
Set range of values.
@param f1 Min value.
@param f2 Max value.
@return: None.
"""
        pass

    def getValueAt(self, time, index, view):
        """self.valueAt(time, index, view) -> Floating point or List of floating point values (in case some are different).
Return value for this knob at specified time, optional index and view.
@param time: Time.
@param index: Optional index. Default is 0.
@param view: Optional view.
@return: Floating point or List of floating point values (in case some are different).
"""
        return 0.0

    def getNthDerivative(self, t, i):
        """Return n'th derivative at time 't' and index 'i'."""
        return 0

    def isKey(self, index, view):
        """self.isKey(index, view) -> True if succeeded, False otherwise.
@param index: Optional index.
@param view: Optional view.
@return: True if succeeded, False otherwise.
"""
        pass

    def fromScript(self, s):
        """self.fromScript(s) -> True if successful, False otherwise.
Set value of the knob to a user defined script (TCL syntax, as in .nk file). Return True if successful.
@param s: Nuke script to be set on knob.
@return: True if successful, False otherwise.
"""
        pass

    def maximum(self):
        """self.max() -> Maximum value.
@return: Maximum value.
"""
        return 0

    def value(self, index, view, time):
        """self.value(index, view, time) -> Floating point or List of floating point values (in case some are different).
@param index: Optional index. Default is 0.
@param view: Optional view.
@param time: Optional time.
@return: Floating point or List of floating point values (in case some are different).
"""
        return 0.0

    def getValue(self, index, view, time):
        """self.value(index, view, time) -> Floating point or List of floating point values (in case some are different).
@param index: Optional index. Default is 0.
@param view: Optional view.
@param time: Optional time.
@return: Floating point or List of floating point values (in case some are different).
"""
        return 0.0

    def getKeyIndex(self):
        """Return index of the keyframe at time 't' and channel 'c'."""
        pass

    def copyAnimation(self, channel, curve, view):
        """self.copyAnimation(channel, curve, view) -> None.
Copies the i'th channel of the AnimationCurve curve to this object. The view is optional and defaults to the current view.
@param channel: The channel index.
@param curve: AnimationCurve.
@param view: Optional view. Defaults to current.
@return: None.
"""
        pass

class Axis_Knob(_Knob):
    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass
    def uniformScale(self):
        """self.uniformScale() -> Double_Knob
Return uniform scale knob."""
        return Double_Knob()

    def rotate(self):
        """self.rotate() -> XYZ_Knob

Return rotation knob."""
        return XYZ_Knob()

    def skew(self):
        """self.skew() -> XYZ_Knob

Return skew knob."""
        return XYZ_Knob()

    def value(self):
        """self.value() -> _nukemath.Matrix4
Return the transform matrix formed by combining the input knob values for translate, rotate, scale, skew and pivot."""
        return math.Matrix4()

    def scale(self):
        """self.scale() -> Scale_Knob

Return scale knob."""
        return Scale_Knob()

    def pivot(self):
        """self.pivot() -> XYZ_Knob

Return pivot knob."""
        return XYZ_Knob()

    def translate(self):
        """self.translate() -> XYZ_Knob

Return translation knob."""
        return XYZ_Knob()

class Channel_Knob(_Knob):
    def inputNumber(self):
        """self.inputNumber() -> int"""
        return 0

    def enableChannel(self):
        """self.enableChannel(name, b) -> None
Enable or disable a channel.
@param name: The name of the channel.
@param b: True to enable the channel, False to disable it.
@return: None"""
        pass

    def layerSelector(self):
        """self.layerSelector() -> bool"""
        pass

    def setEnable(self,name):
        """self.setEnable(name) -> None
Enable a channel.
@param name: The name of the channel to enable.
@return: None"""
        pass

    def value(self):
        """self.value() -> str
Get the name of the selected channel.
@return: The name of the channel as a string.
"""
        return ''

    def checkMarks(self):
        """self.checkMarks() -> bool"""
        pass

    def channelSelector(self):
        """self.channelSelector() -> bool"""
        pass

    def depth(self):
        """self.depth() -> int

Get the channel depth.
@return: The depth of the channel as an int."""
        return 0

    def setValue(self,name):
        """self.setValue(name) -> None
Set the selected channel using the channel name.
@param name: The name of the new channel as a string.
@return: None
@raise ValueError exception if the channel doesn't exist."""
        pass

    def setInput(self,num):
        """self.setInput(num) -> None
Set the input number for this knob.@param num: The number of the new input.
@return: None"""
        pass

    def inputKnob(self):
        """self.inputKnob() -> bool"""
        return True

    def isChannelEnabled(self,name):
        """self.isChannelEnabled(name) -> bool
Test if a channel is enabled.
@param name: The name of the channel.@return: True if the channel is enabled, False otherwise."""
        pass

class BeginTabGroup_Knob(_Knob):
    pass

class Format_Knob(_Knob):
    def setValue(self,format):
        """setValue(format) -> True if succeeded, False otherwise.

Set value of knob to format (either a Format object or a name of a format, e.g. "NTSC")."""
        pass

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def fromScript(self,s):
        """fromScript(s) -> True if succeeded, False otherwise.

Initialise from script s."""
        pass

    def value(self):
        """value() -> Format.

Return value of knob."""
        return Format()

    def actualValue(self):
        """actualValue() -> Format.

Return value of knob."""
        return Format()

    def toScript(self, quote, context=None):
        """toScript(quote, context=current) -> string.

Return the value of the knob in script syntax.
Pass True for quote to return results quoted in {}.
Pass None for context to get results for all views and key times (as stored in a .nk file)."""
        return ''

    def notDefault(self):
        """notDefault() -> True if set to its default value, False otherwise."""
        pass

    def name(self):
        """name() -> string.

Return name of knob."""
        return ''

class GeoSelect_Knob(_Knob):

    def __setattr__(self):
        """x.__setattr__('name', value) <==> x.name = value"""
        pass

    def getSelection(self):
        """self.getSelection() -> list of lists of floats
Returns the selection weights for each vertex as a float. If you access the result as selection[obj][pt], then obj is the index of the object in the input geometry and pt is the index of the point in that object."""
        return [0,]

    def __getattribute__(self, name):
        """x.__getattribute__('name') <==> x.name"""
        pass

    def getGeometry(self):
        """self.getGeometry() -> _geo.GeometryList
Get the geometry which this knob can select from."""
        return geo.GeometryList()

    def __delattr__(self,name):
        """x.__delattr__('name') <==> del x.name"""
        pass

class Help_Knob(_Knob):
    pass

class Histogram_Knob(_Knob):
    pass

class Link_Knob(_Knob):
    def setValue(self):
        """setValue() -> None

Set value of knob."""
        pass

    def getLinkedKnob(self):
        """getLinkedKnob() -> knob
"""
        return Knob()

    def value(self):
        """value() -> string
Return value of knob."""
        return ''

    def getLink(self):
        """getLink() -> s
"""
        pass

    def setLink(self,s):
        """setLink(s) -> None
"""
        pass

    def makeLink(self):
        """makeLink(s, t) -> None
"""
        pass

class LookupCurves_Knob(_Knob):
    def delCurve(self,curve):
        """self.delCurve(curve) -> None
Deletes a curve.
@param curve: The name of the animation curve.
@return: None
"""
        pass

    def editCurve(self):
        """self.editCurve(curve, expr=None) -> None
Edits an existing curve.
@param curve: The name of an animation curve.
@param expr: The new expression for the curve.
@return: None
"""
        pass

    def addCurve(self):
        """self.addCurve(curve, expr=None) -> None
Adds a curve.
@param curve: The name of an animation curve, or an AnimationCurve instance.
@param expr: Optional parameter giving an expression for the curve.
@return: None
"""
        pass

class MultiView_Knob(_Knob):
    def toScriptPrefix(self):
        """"""
        pass

    def setValue(self,s):
        """fromScript(s) -> True if succeeded, False otherwise.

Initialise from script s."""
        pass

    def fromScript(self,s):
        """fromScript(s) -> True if succeeded, False otherwise.

Initialise from script s."""
        pass

    def value(self, quote, context=None):
        """toScript(quote, context=current) -> string.
Return the value of the knob in script syntax.
Pass True for quote to return results quoted in {}.
Pass None for context to get results for all views and key times (as stored in a .nk file)."""
        pass

    def toScriptPrefixUserKnob(self):
        """"""
        pass

    def toScript(self, quote, context=None):
        """toScript(quote, context=current) -> string.
Return the value of the knob in script syntax.
Pass True for quote to return results quoted in {}.
Pass None for context to get results for all views and key times (as stored in a .nk file)."""
        return ''

    def notDefault(self):
        """notDefault() -> True if set to its default value, False otherwise."""
        pass

class Obsolete_Knob(_Knob):

    def setValue(self):
        """None"""
        pass

    def value(self):
        """None"""
        pass

class Password_Knob(_Knob):
    def setValue(self, val, view='default'):
        """self.setValue(val, view='default') -> None
Set value of knob.
@param val: The new value.
@param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
@return: None"""
        pass

    def value(self):
        """self.value() -> str

Get the value of this knob as a string.
@return: String value.
"""
        return ''

    def getText(self):
        """self.getText() -> string

Return text associated with knob."""
        return ''

class String_Knob(_Knob):

    def splitView(self,view):
        """self.splitView(view) -> None.
Split the view away from the current knob value.
@param view: Optional view. Default is current view.
@return: None.
"""
        pass

    def setValue(self, val, view='default'):
        """self.setValue(val, view='default') -> None

Set value of knob.
@param val: The new value.
@param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
@return: None"""
        pass

    def setText(self, val, view='default'):
        """self.setValue(val, view='default') -> None

Set value of knob.
@param val: The new value.
@param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
@return: None"""
        pass

    def getText(self, output_context):
        """self.value(oc) -> str
Get the value of this knob as a string.
@param oc: Optional parameter specifying the output context.
@return: String value.
"""
        return ''

    def getValue(self,oc):
        """self.value(oc) -> str

Get the value of this knob as a string.
@param oc: Optional parameter specifying the output context.
@return: String value.
"""
        return ''

    def value(self,oc):
        """self.value(oc) -> str
Get the value of this knob as a string.
@param oc: Optional parameter specifying the output context.
@return: String value.
"""
        return ''

    def unsplitView(self,view):
        """self.unsplitView(view) -> None.
Unsplit the view so that it shares a value with other views.
@param view: Optional view. Default is current view.
@return: None.
"""
        pass

class Tab_Knob(_Knob):
    def setValue(self):
        """None"""
        pass

    def value(self):
        """None"""
        pass

class Text_Knob(_Knob):
    def value(self):
        """None"""
        return ''

    def setValue(self):
        """None"""
        pass

class Transform2d_Knob(_Knob):
    def value(self,oc):
        """value(oc) -> matrix

Return transformation matrix. The argument oc is an OutputContext. Both arguments are optional."""
        return math.Matrix4()

class ViewView_Knob(_Knob):
    pass
class EndTabGroup_Knob(_Knob):
    pass
class Disable_Knob(_Knob):
    pass
class Radio_Knob(_Knob):
    pass
class FreeType_Knob(_Knob):
    pass
class SceneView_Knob(_Knob):
    pass

class BBox_Knob(Array_Knob):

    def value(self):
        """Return value for dimension 'i'"""
        pass

    def setT(self):
        """Set value for T extent."""
        pass

    def fromDict(self,box):
        """self.fromDict(box) -> None

Set the bounding box from the given box.
@param box: Dictionary containing the x, y, r and t keys.
@return: None"""
        pass

    def r(self):
        """Return value for R extent."""
        return 0

    def names(self):
        """Return name for dimension 'i'"""
        return ''

    def setR(self):
        """Set value for R extent."""
        return 0

    def toDict(self):
        """self.toDict() -> dict.

Returns the bounding box as a dict with x, y, r, and t keys.
@return: dict with x, y, r and t keys"""
        return {'':1,}

    def y(self):
        """Return value for Y position."""
        return 0

    def x(self):
        """Return value for X position."""
        return 0

    def setX(self):
        """Set value for X position."""
        pass

    def setY(self):
        """Set value for Y position."""
        pass

    def t(self):
        """Return value for T extent."""
        return 0

class Boolean_Knob(Array_Knob):
    def value(self):
        """self.value() -> bool
Get the boolean value for this knob.
@return: True or False.
"""
        return True

    def setValue(self,b):
        """self.setValue(b) -> bool
Set the boolean value of this knob.
@param b: Boolean convertible object.
@return: True if modified, False otherwise.
"""
        pass

class Box3_Knob(Array_Knob):

    def setF(self,far):
        """Set value for F extent. F (far) is the maximum Z extent of the box."""
        pass

    def f(self,ar):
        """Return value for F extent. F (far) is the maximum Z extent of the box."""
        return 0

    def setN(self,near):
        """Set value for N position. N (near) is the minimum Z extent of the box."""
        pass

    def value(self):
        """Return value for dimension 'i'"""
        return 0

    def n(self,ear):
        """Return value for N position. N (near) is the minimum Z extent of the box."""
        return 0

    def setT(self,top):
        """Set value for T extent. T (top) is the maximum vertical extent of the box."""
        pass

    def r(self,ight):
        """Return value for R extent. R (right) is the right extent of the box."""
        return 0

    def names(self):
        """Return name for dimension 'i'"""
        return ''

    def setR(self,right):
        """Set value for R extent. R (right) is the right extent of the box."""
        pass

    def y(self):
        """Return value for Y position. Y is the minimum vertical extent of the box."""
        return 0

    def x(self):
        """Return value for X position. X is the minimum horizontal extent of the box."""
        return 0

    def setX(self):
        """Set value for X position. X is the minimum horizontal extent of the box."""
        pass

    def setY(self):
        """Set value for Y position. Y is the minimum vertical extent of the box."""
        pass

    def t(self,op):
        """Return value for T extent. T (top) is the maximum vertical extent of the box."""
        return 0

class Color_Knob(Array_Knob):
    def inputNumber(self):
        """inputNumber() -> int
Return input number."""
        pass

    def names(self, n):
        """names(n) -> string
Return name for dimension n. The argument n is an integer."""
        return ''

class IArray_Knob(Array_Knob):
    def value(self):
        """Return value of the array at position (x, y)."""
        return (0,)


    def height(self):
        """Return height of the array."""
        return 0

    def width(self):
        """Return width of the array."""
        return 0

    def dimensions(self):
        """Return number of dimensions."""
        return 0

class Int_Knob(Array_Knob):
    def value(self):
        """self.value() -> int
Get the integer value of this knob.
@return: The value of this knob as an int.
"""
        return 0

    def setValue(self,val):
        """self.setValue(val) -> bool
Set the integer value of this knob.
@param val: The new value. Must be an integer.
@return: True if succeeded, False otherwise."""
        pass

class Keyer_Knob(Array_Knob):

    def highTol(self):
        """"""
        pass

    def lowSoft(self):
        """"""
        pass

    def lowTol(self):
        """"""
        pass

    def value(self, outputCtx, n):
        """self.value(outputCtx, n) -> float
Get the value of argument n.
@param outputCtx: The OutputContext to evaluate the argument in.
@param n: The index of the argument to get the value of.
@return: The value of argument n."""
        return 0.0

    def names(self,n):
        """self.names(n) -> string
@param n: The index of the name to return.
@return: The name at position n."""
        return ''

    def highSoft(self):
        """"""
        pass

class XY_Knob(Array_Knob):
    def value(self, n, oc):
        """value(n, oc) -> float
Return value for dimension n. The optional argument oc is an OutputContext."""
        return 0.0

    def names(self,n):
        """names(n) -> string
Return name for dimension n. The argument n is an integer."""
        return ''

    def y(self,oc):
        """y(oc) -> float
Return value for y. The optional oc argument is an OutputContext"""
        return 0.0

    def x(self,oc):
        """x(oc) -> float
Return value for x. The optional oc argument is an OutputContext"""
        return 0.0

class Double_Knob(Array_Knob):
    pass

class UV_Knob(Array_Knob):
    def names(self,n):
        """names(n) -> string
Return name for dimension n. The argument n is an integer."""
        return ''

class Unsigned_Knob(Array_Knob):
    def value(self):
        """self.value() -> int
Get the value of this knob as an integer.
@return: int
"""
        return 0

    def setValue(self,val):
        """self.setValue(val) -> bool
Set the unsigned integer value of this knob.
@param val: The new value for the knob. Must be an integer >= 0.
@return: True if succeeded, False otherwise.
"""
        pass

class Scale_Knob(Array_Knob):
    def value(self, n, oc):
        """value(n, oc) -> float
Return value for dimension n. The optional argument oc is an OutputContext."""
        return 0.0

    def names(self,n):
        """names(n) -> string

Return name for dimension n. The argument n is an integer."""
        return ''

    def y(self,oc):
        """y(oc) -> float
Return value for y. The optional oc argument is an OutputContext"""
        return 0.0

    def x(self,oc):
        """x(oc) -> float
Return value for x. The optional oc argument is an OutputContext"""
        return 0.0

    def z(self,oc):
        """z(oc) -> float
Return value for z. The optional oc argument is an OutputContext"""
        return 0.0

class Range_Knob(Array_Knob):
    pass

class WH_Knob(Array_Knob):
    def y_at(self):
        """Return value for Y position at time 't'."""
        return 0

    def names(self):
        """Return name for dimension 'i'."""
        return ''

    def y(self):
        """Return value for Y position."""
        return 0

    def x(self):
        """Return value for X position."""
        return 0

    def x_at(self):
        """Return value for X position at time 't'."""
        return 0

class XYZ_Knob(Array_Knob):
    def parent(self):
        """parent() -> XYZ_Knob

Return parent."""
        return XYZ_Knob()


    def value(self):
        """value(n, oc) -> float

Return value for dimension n. The optional argument oc is an OutputContext."""
        return 0.0

    def names(self,n):
        """names(n) -> string

Return name for dimension n. The argument n is an integer."""
        return ''


    def y(self,oc):
        """y(oc) -> float

Return value for y. The optional oc argument is an OutputContext"""
        return 0.0


    def x(self,oc):
        """x(oc) -> float

Return value for x. The optional oc argument is an OutputContext"""
        return 0.0

    def z(self,oc):
        """z(oc) -> float

Return value for z. The optional oc argument is an OutputContext"""
        return 0.0

class ChannelMask_Knob(Channel_Knob):
    pass

class EvalString_Knob(String_Knob):
    def evaluate(self):
        """self.evaluate() -> String.
Evaluate the string, performing substitutions.
@return: String.
"""
        pass

class Multiline_Eval_String_Knob(EvalString_Knob):
    pass

class Enumeration_Knob(Unsigned_Knob):
    def setValue(self,item):
        """self.setValue(item) -> None.
Set the current value. If item is of an Integer type it will treat it as an index to the enum, otherwise as a value.
@param item: String or Integer.
@return: None.
Example:
w = nuke.nodes.Write()
k = w['file_type']
k.setValue('exr')
"""
        pass

    def numValues(self):
        """self.numValues() -> int

Return number of values. Deprecated."""
        return 0

    def value(self):
        """self.value() -> String.
Current value.
@return: String.
Example:
w = nuke.nodes.Write()
k = w['file_type']
k.value()
"""
        return ''

    def enumName(self,n):
        """self.enumName(n) -> string

Return name of enumeration n. The argument n is an integer and in the range of 0 and numValues. Deprecated."""
        return ''

    def values(self):
        """self.values() -> List of strings.
Return list of items.
@return: List of strings.
Example:
w = nuke.nodes.Write()
k = w['file_type']
k.values()
"""
        return ['',]

    def setValues(self,items):
        """self.setValues(items) -> None.
(Re)initialise knob to the supplied list of items.
@param items: The new list of values.
@return: None.
Example:
w = nuke.nodes.Write()
k = w['file_type']
k.setValues(['exr'])
"""
        pass

class OneView_Knob(Enumeration_Knob):
    pass

class Pulldown_Knob(Enumeration_Knob):
    def commands(self,n):
        """commands(n) -> string

Return command n. The argument n is an integer and in the range of 0 and numValues."""
        return ''

    def numValues(self):
        """numValues() -> int

Return number of values."""
        return 0

    def value(self):
        """None"""
        return 0.0

    def setValues(self,items):
        """self.setValues(items) -> None.
(Re)initialise knob to the list of items.
@param items: Dictionary of name/value pairs.
@return: None.
Example:
w = nuke.nodes.NoOp()
k = nuke.Pulldown_Knob('kname', 'klabel')
k.setValues({'label/command' : 'eval("3*2")'})
w.addKnob(k)
k = w['kname']
"""
        pass

    def itemName(self,n):
        """itemName(n) -> string

Return name of item n. The argument n is an integer and in the range of 0 and numValues."""
        return ''

class Bitmask_Knob(Enumeration_Knob):
    pass

class Script_Knob(String_Knob):
    def execute(self):
        """self.execute() -> None
Execute the command.
@return: None.
"""
        pass

    def setValue(self,cmd):
        """self.setValue(cmd) -> None
Set the new command for this knob.
@param cmd: String containing a TCL command.
@return: None."""
        pass

    def value(self):
        """self.value() -> str

Get the current command.
@return: The current command as a string, or None if there is no current command."""
        return ''

    def command(self):
        """self.command() -> str
Get the current command.
@return: The current command as a string, or None if there is no current command."""
        return ''

    def setCommand(self,cmd):
        """self.setCommand(cmd) -> None
Set the new command for this knob.
@param cmd: String containing a TCL command.
@return: None."""
        pass

class PyCustom_Knob(Script_Knob):

    def getObject(self):
        """Returns the custom knob object as created in the by the 'command' argument to the PyCuston_Knob constructor."""
        return Knob()

class PyScript_Knob(Script_Knob):
    pass

class PythonKnob(String_Knob):
    pass

class ColorChip_Knob(Unsigned_Knob):
    pass

class CascadingEnumeration_Knob(Enumeration_Knob):
    pass

class AColor_Knob(Color_Knob):
    pass

class Eyedropper_Knob(AColor_Knob):
    pass

class File_Knob(EvalString_Knob):
    def fromUserText(self,s):
        """self.fromUserText(s) -> None.
Assign string to knob, parses frame range off the end and opens file to get set the format.
@param s: String to assign.
@return: None.
"""
        pass

    def setValue(self,s):
        """self.fromScript(s) -> None.
Assign string to knob.
@param s: String to assign.
@return: None.
"""
        pass

    def fromScript(self,s):
        """self.fromScript(s) -> None.
Assign string to knob.
@param s: String to assign.
@return: None.
"""
        pass

    def value(self):
        """self.getEvaluatedValue() -> String.
Returns the string on this knob, will be normalized to technical notation if sequence (%4d).
@return: String.
"""
        return ''

    def getValue(self):
        """self.getEvaluatedValue() -> String.
Returns the string on this knob, will be normalized to technical notation if sequence (%4d).
@return: String.
"""
        return ''

    def getEvaluatedValue(self,oc):
        """self.getValue(oc) -> String.
Returns the string on this knob, will be normalized to technical notation if sequence (%4d). Will also evaluate the string for any tcl expressions
@parm oc: the output context to use, if None the knob uiContext will be used.
@return: String.
"""
        return ''

 # NODES


class Knob(File_Knob, PyCustom_Knob, Script_Knob, Pulldown_Knob, XYZ_Knob, WH_Knob, Scale_Knob, Keyer_Knob, Color_Knob,
            Box3_Knob, BBox_Knob):
    """
    Replace main Knob class to inherit all knobs methods
    Not Nuke default. For auto complete only!!!
    """

# NODES

class Node(object):
    def __init__(self, inputs=[], name='', postage_stamp=False, hide_input=False,
                 label='', help='', tile_color=0, gl_color=0, note_font='',
                 note_font_size=12, note_font_color=0, selected=False,
                 xpos=0, ypos=0, icon='', cached=False, disable=False, dope_sheet=False,
                 bookmark=False, lifetimeStart=0, lifetimeEnd=0, useLifetime=False, **kwargs):
        pass
    def __getitem__(self,y):
        """x.__getitem__(y) <==> x[y]"""
        return Knob()
    def __len__(self):
        """x.__len__() <==> len(x)"""
        return 0

    def getNumKnobs(self):
        """self.numKnobs() -> The number of knobs.
@return: The number of knobs.
"""
        return 0

    def writeKnobs(self ,i):
        """self.writeKnobs(i) -> String in .nk form.
Return a tcl list. If TO_SCRIPT | TO_VALUE is not on, this is a simple list
of knob names. If it is on, it is an alternating list of knob names
and the output of to_script().

Flags can be any of these or'd together:
- nuke.TO_SCRIPT produces to_script(0) values
- nuke.TO_VALUE produces to_script(context) values
- nuke.WRITE_NON_DEFAULT_ONLY skips knobs with not_default() false
- nuke.WRITE_USER_KNOB_DEFS writes addUserKnob commands for user knobs
- nuke.WRITE_ALL writes normally invisible knobs like name, xpos, ypos

@param i: The set of flags or'd together. Default is TO_SCRIPT | TO_VALUE.
@return: String in .nk form.
"""
        return ''

    def autoplace(self):
        """self.autoplace() -> None.
Automatically place nodes, so they do not overlap.
@return: None.
"""
        pass

    def forceValidate(self):
        """self.forceValidate() -> None

Force the node to validate itself, updating its hash.
"""
        pass

    def help(self):
        """self.help() -> str
@return: Help for the node.
"""
        return ''

    def lastFrame(self):
        """self.lastFrame() -> int.
Last frame in frame range for this node.
@return: int.
"""
        return 0

    def setSelected(self,selected):
        """self.setSelected(selected) -> None.
Set the selection state of the node.  This is the same as changing the 'selected' knob.
@param selected: New selection state - True or False.
@return: None.
"""
        pass

    def treeHasError(self):
        """treeHasError() -> bool
True if the node or any in its input tree have an error, or False otherwise.

Error state of the node and its input tree.
Note that this will always return false for viewers, which cannot generate their input trees.  Instead, choose an input of the viewer (e.g. the active one), and call treeHasError() on that."""
        pass

    def maximumInputs(self):
        """self.maximumInputs() -> Maximum number of inputs this node can have.
@return: Maximum number of inputs this node can have.
"""
        pass

    def hasError(self):
        """hasError() -> bool
True if the node itself has an error, regardless of the state of the ops in its input tree, or False otherwise.

Error state of the node itself, regardless of the state of the ops in its input tree.
Note that an error on a node may not appear if there is an error somewhere in its input tree, because it may not be possible to validate the node itself correctly in that case."""
        pass

    def deepSample(self,chan, x, y, sample):
        """self.deepSample(c, x, y, n) -> Floating point value.
Return pixel values from a deep image.
This requires the image to be calculated, so performance may be very bad if this is placed into an expression in
a control panel.
@param c: Channel name.
@param x: Position to sample (X coordinate).
@param y: Position to sample (Y coordinate).
@param n: Sample index (between 0 and the number returned by deepSampleCount() for this pixel, or -1 for the frontmost).
@return: Floating point value.
"""
        return 0.0

    def height(self):
        """self.height() -> int.
Height of the node.
@return: int.
"""
        return 0

    def sample(self, chan, x, y, dx, dy, frame):
        """self.sample(c, x, y, dx, dy) -> Floating point value.
Return pixel values from an image.
This requires the image to be calculated, so performance may be very bad if this is placed into an expression in
a control panel. Produces a cubic filtered result. Any sizes less than 1, including 0, produce the same filtered result,
this is correct based on sampling theory. Note that integers are at the corners of pixels, to center on a pixel add .5 to both coordinates.
If the optional dx,dy are not given then the exact value of the square pixel that x,y lands in is returned. This is also called 'impulse filtering'.
@param c: Channel name.
@param x: Centre of the area to sample (X coordinate).
@param y: Centre of the area to sample (Y coordinate).
@param dx: Optional size of the area to sample (X coordinate).
@param dy: Optional size of the area to sample (Y coordinate).
@param frame: Optional frame to sample the node at.
@return: Floating point value.
"""
        return 0.0

    def setInput(self, i, node):
        """self.setInput(i, node) -> bool
Connect input i to node if canSetInput() returns true.
@param i: Input number.
@param node: The node to connect to input i.
@return: True if canSetInput() returns true, or if the input is already correct.
"""
        pass

    def dependencies(self,what):
        """self.dependencies(what) -> List of nodes.

List all nodes referred to by this node. 'what' is an optional integer (see below).
You can use the following constants or'ed together to select what types of dependencies are looked for:
	 nuke.EXPRESSIONS = expressions
	 nuke.INPUTS = visible input pipes
	 nuke.HIDDEN_INPUTS = hidden input pipes.
The default is to look for all types of connections.

Example:
nuke.toNode('Blur1').dependencies( nuke.INPUTS | nuke.EXPRESSIONS )
@param what: Or'ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependencies. The default is to look for all types of connections.
@return: List of nodes.
"""
        return [Node(),]

    def canSetInput(self, i, node):
        """self.canSetInput(i, node) -> bool
Check whether the output of 'node' can be connected to input i.
@param i: Input number.
@param node: The node to be connected to input i.
@return: True if node can be connected, False otherwise.
"""
        pass

    def maximumOutputs(self):
        """self.maximumOutputs() -> Maximum number of outputs this node can have.
@return: Maximum number of outputs this node can have.
"""
        return 0

    def screenWidth(self):
        """self.screenWidth() -> int.
Width of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels.
@return: int.
"""
        return 0

    def linkableKnobs(self,knobType):
        """self.linkableKnobs(knobType) -> List

Returns a list of any knobs that may be linked to from the node as well as some meta information about the knob. This may include whether the knob is enabled and whether it should be used for absolute or relative values. Not all of these variables may make sense for all knobs..
@param knobType A KnobType describing the type of knobs you want.@return: A list of LinkableKnobInfo that may be empty .
"""
        return [Knob(),]

    def minimumInputs(self):
        """self.minimumInputs() -> Minimum number of inputs this node can have.
@return: Minimum number of inputs this node can have.
"""
        return 0

    def firstFrame(self):
        """self.firstFrame() -> int.
First frame in frame range for this node.
@return: int.
"""
        return 0

    def setXpos(self,x):
        """self.setXpos(x) -> None.
Set the x position of node in node graph.
@param x: The x position of node in node graph.
@return: None.
"""
        pass

    def shown(self):
        """self.shown() -> true if the properties panel is open. This can be used to skip updates that are not visible to the user.
@return: true if the properties panel is open. This can be used to skip updates that are not visible to the user.
"""
        pass

    def numKnobs(self):
        """self.numKnobs() -> The number of knobs.
@return: The number of knobs.
"""
        return 0

    def maxInputs(self):
        """self.maximumInputs() -> Maximum number of inputs this node can have.
@return: Maximum number of inputs this node can have.
"""
        return 0

    def isSelected(self):
        """self.isSelected() -> bool

Returns the current selection state of the node.  This is the same as checking the 'selected' knob.
@return: True if selected, or False if not.
"""
        pass

    def opHashes(self):
        """self.opHashes() -> list of int

Returns a list of hash values, one for each op in this node."""
        return (0,)

    def setYpos(self,y):
        """self.setYpos(y) -> None.
Set the y position of node in node graph.
@param y: The y position of node in node graph.
@return: None.
"""
        pass

    def showControlPanel(self):
        """self.showControlPanel(forceFloat = false) -> None
@param forceFloat: Optional python object. If it evaluates to True the control panel will always open as a floating panel. Default is False.
@return: None"""
        pass

    def width(self):
        """self.width() -> int.
Width of the node.
@return: int.
"""
        return 0

    def connectInput(self, i, node):
        """self.connectInput(i, node) -> bool
Connect the output of 'node' to the i'th input or the next available unconnected input. The requested input is tried first, but if it is already set then subsequent inputs are tried until an unconnected one is found, as when you drop a connection arrow onto a node in the GUI.
@param i: Input number to try first.
@param node: The node to connect to input i.
@return: True if a connection is made, False otherwise."""
        pass

    def allKnobs(self):
        """self.knobs() -> dict

Get a dictionary of (name, knob) pairs for all knobs in this node.

For example:

   >>> b = nuke.nodes.Blur()
   >>> b.knobs()

@return: Dictionary of all knobs.
"""
        return {'':Knob(),}

    def deepSampleCount(self,x, y):
        """self.deepSampleCount(x, y) -> Integer value.
Return number of samples for a pixel on a deep image.
This requires the image to be calculated, so performance may be very bad if this is placed into an expression in
a control panel.
@param x: Position to sample (X coordinate).
@param y: Position to sample (Y coordinate).
@return: Integer value.
"""
        return 0

    def removeKnob(self,k):
        """self.removeKnob(k) -> None.
Remove knob k from this node or panel. Throws a ValueError exception if k is not found on the node.
@param k: Knob.
@return: None.
"""
        pass

    def input(self,i):
        """self.input(i) -> The i'th input.
@param i: Input number.
@return: The i'th input.
"""
        return Node()

    def knobs(self):
        """self.knobs() -> dict

Get a dictionary of (name, knob) pairs for all knobs in this node.

For example:

   >>> b = nuke.nodes.Blur()
   >>> b.knobs()

@return: Dictionary of all knobs.
"""
        return {'':Knob(),}

    def Class(self):
        """self.Class() -> Class of node.
@return: Class of node.
"""
        return ''

    def maxOutputs(self):
        """self.maximumOutputs() -> Maximum number of outputs this node can have.
@return: Maximum number of outputs this node can have.
"""
        return 0

    def metadata(self, key, time, view):
        """self.metadata(key, time, view) -> value or dict
Return the metadata item for key on this node at current output context, or at optional time and view.
If key is not specified a dictionary containing all key/value pairs is returned.
None is returned if key does not exist on this node.
@param key: Optional name of the metadata key to retrieve.
@param time: Optional time to evaluate at (default is taken from node's current output context).
@param view: Optional view to evaluate at (default is taken from node's current output context).
@return: The requested metadata value, a dictionary containing all keys if a key name is not provided, or None if the specified key is not matched.
"""
        return 0

    def knob(self,p):
        """self.knob(p) -> The knob named p or the pth knob.
@param p: A string or an integer.
@return: The knob named p or the pth knob.
"""
        return Knob()

    def inputs(self):
        """self.inputs() -> Number of inputs.
@return: Number of inputs.
"""
        return 0

    def xpos(self):
        """self.xpos() -> X position of node in node graph.
@return: X position of node in node graph.
"""
        return 0

    def setName(self, name):
        """self.setName(name, uncollide=True) -> None
Set name of the node and resolve name collisions if optional named argument 'uncollide' is True.
@param name: A string.
@param uncollide: Optional boolean to resolve name collisions. Defaults to True.
@return: None"""
        pass

    def format(self):
        """self.format() -> Format.
Format of the node.
@return: Format.
"""
        return Format()

    def dependent(self):
        """self.dependent(what, forceEvaluate) -> List of nodes.

List all nodes that read information from this node.  'what' is an optional integer:
	 You can use any combination of the following constants or'ed together to select what types of dependent nodes to look for:
		 nuke.EXPRESSIONS = expressions
		 nuke.INPUTS = visible input pipes
		 nuke.HIDDEN_INPUTS = hidden input pipes.
The default is to look for all types of connections.

forceEvaluate is an optional boolean defaulting to True. When this parameter is true, it forces a re-evaluation of the entire tree.
This can be expensive, but otherwise could give incorrect results if nodes are expression-linked.

Example:
nuke.toNode('Blur1').dependent( nuke.INPUTS | nuke.EXPRESSIONS )
@param what: Or'ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependent nodes. The default is to look for all types of connections.
@param forceEvaluate: Specifies whether a full tree evaluation will take place. Defaults to True.
@return: List of nodes.
"""
        return [Node(),]

    def setXYpos(self, x, y):
        """self.setXYpos(x, y) -> None.
Set the (x, y) position of node in node graph.
@param x: The x position of node in node graph.
@param y: The y position of node in node graph.
@return: None.
"""
        pass

    def ypos(self):
        """self.ypos() -> Y position of node in node graph.
@return: Y position of node in node graph.
"""
        return 0

    def running(self):
        """self.running() -> Node rendering when paralled threads are running or None.
Class method.
@return: Node rendering when paralled threads are running or None.
"""
        pass

    def pixelAspect(self):
        """self.pixelAspect() -> int.
Pixel Aspect ratio of the node.
@return: float.
"""
        return 0

    def proxy(self):
        """self.proxy() -> bool
@return: True if proxy is enabled, False otherwise.
"""
        pass

    def clones(self):
        """self.clones() -> Number of clones.
@return: Number of clones.
"""
        return 0

    def fullName(self):
        """self.fullName() -> str
Get the name of this node and any groups enclosing it in 'group.group.name' form.
@return: The fully-qualified name of this node, as a string.
"""
        return ''

    def resetKnobsToDefault(self):
        """self.resetKnobsToDefault() -> None

Reset all the knobs to their default values.
"""
        pass

    def channels(self):
        """self.channels() -> String list.
List channels output by this node.
@return: String list.
"""
        return ['',]

    def showInfo(self,s):
        """self.showInfo(s) -> None.
Creates a dialog box showing the result of script s.
@param s: A string.
@return: None.
"""
        pass

    def name(self):
        """self.name() -> str
@return: Name of node.
"""
        return ''

    def minInputs(self):
        """self.minimumInputs() -> Minimum number of inputs this node can have.
@return: Minimum number of inputs this node can have.
"""
        return 0

    def hideControlPanel(self):
        """self.hideControlPanel() -> None
@return: None"""
        pass

    def optionalInput(self):
        """self.optionalInput() -> Number of first optional input.
@return: Number of first optional input.
"""
        return 0

    def screenHeight(self):
        """self.screenHeight() -> int.
Height of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels.
@return: int.
"""
        return 0

    def addKnob(self,k):
        """self.addKnob(k) -> None.
Add knob k to this node or panel.
@param k: Knob.
@return: None.
"""
        pass


    def frameRange(self):
        """self.frameRange() -> FrameRange.
Frame range for this node.
@return: FrameRange.
"""
        return FrameRange()

    def error(self):
        """error() -> bool
True if the node or any in its input tree have an error, or False otherwise.

Error state of the node and its input tree.  Deprecated; use hasError or treeHasError instead.
Note that this will always return false for viewers, which cannot generate their input trees.  Instead, choose an input of the viewer (e.g. the active one), and call treeHasError() on that."""
        pass

    def redraw(self):
        """self.redraw() -> None.
Force a redraw of the node.
@return: None.
"""
        pass

    def readKnobs(self,s):
        """self.readKnobs(s) -> None.
Read the knobs from a string (TCL syntax).
@param s: A string.
@return: None.
"""
        pass

    def bbox(self):
        """self.bbox() -> List of x, y, w, h.
Bounding box of the node.
@return: List of x, y, w, h.
"""
        return [0, 0, 0, 0]

class NodeConstructor(object):

    def __call__(self):
        """x.__call__(...) <==> x(...)"""
        pass

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

class Nodes(object):

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

class AnimationCurve(object):

    def fixSlopes(self):
        """self.fixSlopes() -> None.
@return: None.
"""
        pass

    def constant(self):
        """self.constant() -> bool
@return: True if the animation appears to be a horizontal line, is a simple number,
or it is the default and all the points are at the same y value and have 0 slopes. False otherwise.
"""
        pass

    def removeKey(self,keys):
        """self.removeKey(keys) -> None.
Remove some keys from the curve.
@param keys: The sequence of keys to be removed.
@return: None.
"""
        pass

    def size(self):
        """self.size() -> Number of keys.
@return: Number of keys.
"""
        return 0

    def knobIndex(self):
        """self.knobIndex() -> Int.
Return the knob index this animation belongs to.@return: Int.
"""
        return 0

    def inverse(self,y):
        """self.inverse(y) -> Float.
The inverse function at value y. This is the value of x such that evaluate(x) returns y.
This is designed to invert color lookup tables. It only works if the derivative is zero or positive everywhere.
@param y: The value of the function to get the inverse for.
@return: Float.
"""
        return 0.0

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def selected(self):
        """self.selected() -> bool
@return: True if selected, False otherwise.
"""
        pass

    def setKey(self, t, y):
        """self.setKey(t, y) -> Key.
Set a key at time t and value y. If there is no key
there one is created. If there is a key there it is moved
vertically to be at y.  If a new key is inserted the
interpolation and extrapolation are copied from a neighboring key, if
there were no keys then it is set to nuke.SMOOTH interpolation and
nuke.CONSTANT extrapolation.
@param t: The time to set the key at.
@param y: The value for the key.
@return: The new key.
"""
        return AnimationKey()

    def addKey(self,keys):
        """self.addKey(keys) -> None.
Insert a sequence of keys.
@param keys: Sequence of AnimationKey.
@return: None.
"""
        pass

    def changeInterpolation(self, keys, type):
        """self.changeInterpolation(keys, type) -> None.
Change interpolation (and extrapolation) type for the keys.
@param keys: Sequence of keys.
@param type: Interpolation type. One of nuke.HORIZONTAL, nuke.BREAK, nuke.BEFORE_CONST, nuke.BEFORE_LINEAR, nuke.AFTER_CONST or nuke.AFTER_LINEAR.
@return: None.
"""
        pass

    def toScript(self,selected):
        """self.toScript(selected) -> str
@param selected: Optional parameter. If this is given and is True, then only process the selected curves; otherwise convert all.
@return: A string containing the curves.
"""
        return ''

    def knob(self):
        """self.knob() -> Knob.
Return knob this animation belongs to.@return: Knob.
"""
        return Knob()

    def keys(self):
        """self.keys() -> List of keys.
@return: List of keys.
"""
        return [AnimationKey(),]

    def evaluate(self,t):
        """self.evaluate(t) -> float
Value at time 't'.
@param t: Time.
@return: The value of the animation at time 't'.
"""
        return 0.0

    def integrate(self, t1, t2):
        """self.integrate(t1, t2) -> Float.
Calculate the area underneath the curve from t1 to t2.
@param t1 The start of the integration range.
@param t2 The end of the integration range.
@return: The result of the integration.
"""
        return 0.0

    def derivative(self, t, n):
        """self.derivative(t, n) -> Float.
The n'th derivative at time 't'. If n is less than 1 it returns evaluate(t).
@param t: Time.
@param n: Optional. Default is 1.
@return: The value of the derivative.
"""
        return 0.0

    def setExpression(self,s):
        """self.setExpression(s) -> None.
Set expression.
@param s: A string containing the expression.
@return: None.
"""
        pass

    def identity(self):
        """self.identity() -> bool
@return: True if the animation appears to be such that y == x everywhere. This is True only for an expression of 'x' or the
default expression and all points having y == x and slope == 1. Extrapolation is ignored.
"""
        pass

    def clear(self):
        """self.clear() -> None.
Delete all keys.
@return: None.
"""
        pass

    def fromScript(self,s):
        """self.fromScript(s) -> None.
@param s: String.
@return: None.
"""
        pass

    def knobAndFieldName(self):
        """self.knobAndFieldName() -> string.
Knob and field name combined (e.g. 'translate.x').
@return: string.
"""
        return ''

    def noExpression(self):
        """self.noExpression() -> bool
@return: True if the expression is the default expression (i.e. the keys control the curve), False otherwise.
"""
        pass

    def expression(self):
        """self.expression() -> String.
Get the expression.@return: String.
"""
        return ''

    def view(self):
        """self.view() -> String.
The view this AnimationCurve object is associated with.
@return: String.
"""
        return ''

class AnimationKey(object):
    """
extrapolation   Controls how to set the left slope of the first point and the right slope of the last point
interpolation   Used to calculate all the slopes except for the left slope of the first key and the right slope of the last key
la              The left 'bicubic' value
lslope          The derivative to the left of the point
ra              The right 'bicubic' value
rslope          The derivative to the right of the point
selected        True if the point is selected in the curve editor
x               The horizontal position of the point
y               The vertical position of the point
    """
    def __init__(self, time, val):
        pass
    extrapolation= None
    #Controls how to set the left slope of the first point and the right slope of the last point
    interpolation=0
    #Used to calculate all the slopes except for the left slope of the first key and the right slope of the last key
    la=0
    #The left 'bicubic' value
    lslope=0.0
    #The derivative to the left of the point
    ra=0.0
    #The right 'bicubic' value
    rslope=0.0
    #The derivative to the right of the point
    selected=True
    #True if the point is selected in the curve editor
    x=0
    #The horizontal position of the point
    y=0
    #The vertical position of the point

class Box(object):

    def set(self):
        """self.set(x, y, r, t) -> None

Set all values at once."""
        pass

    def move(self):
        """self.move(dx, dy) -> None.

Move all the sides and thus the entire box by the given deltas."""
        pass

    def isConstant(self):
        """self.isConstant() -> True if box is 1x1 in both directions, False otherwise."""
        pass

    def clampY(self,y):
        """self.clampY(y) -> int.

Return y restricted to pointing at a pixel in the box."""
        return 0

    def clampX(self,x):
        """self.clampX(x) -> int.

Return x restricted to pointing at a pixel in the box."""
        return 0

    def pad(self):
        """self.pad(dx, dy, dr, dt) -> None.

Move all the sides and thus the entire box by the given deltas."""
        pass

    def centerX(self):
        """self.centerX() -> float

Return center in X."""
        return 0.0

    def centerY(self):
        """self.centerY() -> float

Return height in Y."""
        return 0.0

    def intersect(self, x, y, r, t):
        """self.intersect(x, y, r, t) -> None.

Intersect with the given edges."""
        pass

    def setH(self,n):
        """self.setH(n) -> None

Set height by moving top edge."""
        pass

    def setT(self,n):
        """self.setT(n) -> None

Set top edge."""
        pass

    def setW(self,n):
        """self.setW(n) -> None

Set width by moving right edge."""
        pass

    def setR(self,n):
        """self.setR(n) -> None

Set the right edge. The parameter n is an integer."""
        pass

    def setX(self,n):
        """self.setX(n) -> None

Set the left edge. The parameter n is an integer."""
        pass

    def setY(self,n):
        """self.setY(n) -> None

Set the bottom edge. The parameter n is an integer."""
        pass

    def h(self):
        """self.h() -> int

Return height."""
        return 0

    def clear(self):
        """self.clear() -> None.

Set to is_constant()."""
        pass

    def merge(self, x, y, r, t):
        """self.merge(x, y, r, t) -> None.

Merge with the given edges."""
        pass

    def r(self):
        """self.r() -> int

Return the right edge of the box."""
        return 0

    def t(self):
        """self.t() -> int

Return top edge."""
        return 0

    def w(self):
        """self.w() -> int

Return width."""
        return 0

    def y(self):
        """self.y() -> int

Return the bottom edge."""
        return 0

    def x(self):
        """self.x() -> int

The left edge of the box."""
        return 0

class FnPySingleton(object):

    def __new__(self,type):
        """None"""
        pass

class Format(object):

    def setHeight(self,newHeight):
        """self.setHeight(newHeight) -> None

Set the height of image file in pixels. newHeight is the new height for the image; it should be a positive integer."""
        pass

    def pixelAspect(self):
        """self.pixelAspect() -> float

Returns the pixel aspect ratio (pixel width divided by pixel height) for this format."""
        return 0.0

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def setName(self,name):
        """self.setName(name) -> None

Set name of this format. The name parameter is the new name for the format."""
        pass

    def setPixelAspect(self,aspectRatio):
        """self.setPixelAspect(aspectRatio) -> None

Set a new pixel aspect ratio for this format. The aspectRatio parameter is the new ratio, found by dividing the desired pixel width by the desired pixel height."""
        pass

    def height(self):
        """self.height() -> int

Return the height of image file in pixels."""
        return 0

    def scaled(self, sx, sy, tx, ty):
        """scaled(sx, sy, tx, ty) -> Format

Scale and translate this format by sx, sy, tx and ty.

@param sx: Scale factor in X.@param sy: Scale factor in Y.@param tx: Offset factor in X.@param ty: Offset factor in Y.@return: Format."""
        return Format()

    def width(self):
        """self.width() -> int

Return the width of image file in pixels."""
        return 0

    def add(self,name):
        """self.add(name) -> None

Add this instance to a list of "named" formats. The name parameter is the name of the list to add the format to."""
        pass

    def toUV(self, x, y):
        """self.toUV(x, y) -> (u, v)

Back-transform an XY coordinate in the format's space into UV space.

@param x: The X coordinate.
@param y: The Y coordinate.
@return: [u, v]."""
        return (0,0)

    def fromUV(self):
        """self.fromUV(u, v) -> [x, y]

Transform a UV coordinate in the range 0-1 into the format's XY range. Returns a list containing the x and y coordinates.

@param u: The U coordinate.
@param v: The V coordinate.
@return: [x, y]"""
        return [0,0]

    def setWidth(self,newWidth):
        """self.setWidth(newWidth) -> None

Set the width of image file in pixels.newWidth is the new width for the image; it should be a positive integer."""
        pass

    def name(self):
        """self.name() -> string

Returns the user-visible name of the format."""
        return ''

class FrameRange(object):

    def minFrame(self):
        """self.minFrame() -> int

 return the minimun frame define in the range."""
        return 0

    def last(self):
        """self.last() -> int

 return the last frame of the range."""
        return 0

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def setLast(self,n):
        """self.setLast(n) -> None

 set the last frame of the range."""
        pass

    def getFrame(self,n):
        """self.getFrame(n) -> int

 return the frame according to the index, parameter n must be between 0 and frames()."""
        return 0

    def stepFrame(self):
        """self.stepFrame() -> int

 return the absolute increment between two frames."""
        return 0

    def setFirst(self,n):
        """self.setFirst(n) -> None

 set the first frame of the range."""
        pass

    def next(self):
        """x.next() -> the next value, or raise StopIteration"""
        pass

    def isInRange(self,n):
        """self.isInRange(n) -> int

 return if the frame is inside the range."""
        return 0

    def maxFrame(self):
        """self.maxFrame() -> int

 return the maximun frame define in the range."""
        return 0

    def __iter__(self):
        """x.__iter__() <==> iter(x)"""
        return 0

    def setIncrement(self,n):
        """self.setIncrement(n) -> None

 set the increment between two frames."""
        pass

    def increment(self):
        """self.increment() -> int

 return the increment between two frames."""
        return 0

    def frames(self):
        """self.frames() -> int

 return the numbers of frames defined in the range."""
        return 0

    def first(self):
        """self.first() -> int

 return the first frame of the range."""
        return 0

class FrameRanges(object):

    def compact(self):
        """compact() -> None

 compact all the frame ranges."""
        pass

    def getRange(self):
        """getRange()-> FrameRange

 return a range from the list"""
        pass

    def toFrameList(self):
        """toFrameList() -> [int]

 return a list of frames in a vector"""
        return [0,]

    def minFrame(self):
        """minFrame() -> int

 get minimun frame of all ranges."""
        return 0

    def add(self,r):
        """add(r) -> None

 add a new frame range."""
        pass

    def next(self):
        """x.next() -> the next value, or raise StopIteration"""
        pass

    def maxFrame(self):
        """maxFrame() -> int

 get maximun frame of all ranges."""
        return 0

    def __iter__(self):
        """x.__iter__() <==> iter(x)"""
        pass

    def clear(self):
        """clear() -> None

 reset all store frame ranges."""
        pass

    def size(self):
        """size() -> int

 return the ranges number."""
        return 0

class GlobalsEnvironment(object):

    def __delitem__(self,y):
        """x.__delitem__(y) <==> del x[y]"""
        pass


    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass


    def __getitem__(self,y):
        """x.__getitem__(y) <==> x[y]"""
        pass


    def __contains__(self):
        """None"""
        pass


    def keys(self):
        """None"""
        pass

    def items(self):
        """None"""
        pass

    def get(self):
        """None"""
        pass

    def __setitem__(self):
        """x.__setitem__(i, y) <==> x[i]=y"""
        pass

    def has_key(self):
        """None"""
        pass

    def values(self):
        """None"""
        pass

    def __repr__(self):
        """x.__repr__() <==> repr(x)"""
        pass

    def __len__(self):
        """x.__len__() <==> len(x)"""
        pass

class Hash(object):

    def reset(self):
        """Reset the hash."""
        pass

    def __ne__(self,y):
        """x.__ne__(y) <==> x!=y"""
        pass

    def __setattr__(self):
        """x.__setattr__('name', value) <==> x.name = value"""
        pass

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def setHash(self):
        """Set the current value of the hash."""
        pass

    def __getattribute__(self,name):
        """x.__getattribute__('name') <==> x.name"""
        pass

    def __delattr__(self,name):
        """x.__delattr__('name') <==> del x.name"""
        pass

    def __le__(self,y):
        """x.__le__(y) <==> x<=y"""
        pass

    def append(self):
        """Add another value to the hash."""
        pass

    def __gt__(self,y):
        """x.__gt__(y) <==> x>y"""
        pass

    def __hash__(self):
        """x.__hash__() <==> hash(x)"""
        pass

    def getHash(self):
        """Get the current value of the hash."""
        pass

    def __lt__(self,y):
        """x.__lt__(y) <==> x<y"""
        pass

    def __eq__(self,y):
        """x.__eq__(y) <==> x==y"""
        pass

    def __ge__(self,y):
        """x.__ge__(y) <==> x>=y"""
        pass

class Info(object):

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def h(self):
        """self.h() -> float

Return height."""
        return 0.0

    def w(self):
        """self.w() -> float

Return width."""
        return 0.0

    def y(self):
        """self.y() -> float

Return the bottom edge."""
        return 0.0

    def x(self):
        """x() -> float

Return left edge."""
        return 0.0

    def __init__(self):
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signature"""
        pass

class Layer(object):

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def setName(self,newName):
        """self.setName(newName) -> None
Set the name of this layer.

@param newName: The new name for this layer."""
        pass

    def channels(self):
        """self.channels() -> [string, ...]
Get a list of the channels in this layer.

@return: A list of strings, where each string is the name of a channel in this layer."""
        return ['',]

    def visible(self):
        """self.visible() -> bool
Check whether the layer is visible.

@return: True if visible, False if not."""
        pass

    def name(self):
        """self.name() -> str
Get the layer name.

@return: The layer name, as a string."""
        return ''

class Lut(object):

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def toByte(self,float):
        """self.toByte(float) -> float.

Converts floating point values to byte values in the range 0-255."""
        return 0.0

    def fromByteSingle(self,float):
        """self.fromByte(float) -> float.

Converts byte values in the range 0-255 to floating point."""
        return 0.0

    def fromFloat(self, src, alpha):
        """fromFloat(src, alpha) -> float list.

Convert a sequence of floating-point values to from_byte(x*255).
Alpha is an optional argument and if present unpremultiply by alpha, convert, and then multiply back."""
        return [0.0,]

    def toFloat(self):
        """toFloat(src, alpha) -> float list.

Convert a sequence of floating-point values to to_byte(x)/255.
Alpha is an optional argument and if present unpremultiply by alpha, convert, and then multiply back."""
        return [0.0,]

    def isLinear(self):
        """self.isLinear() -> True if toByte(x) appears to return x*255, False otherwise."""
        pass

    def toByteSingle(self,float):
        """self.toByte(float) -> float.

Converts floating point values to byte values in the range 0-255."""
        return 0.0

    def fromByte(self,float):
        """self.fromByte(float) -> float.

Converts byte values in the range 0-255 to floating point."""
        return 0.0

    def isZero(self):
        """self.isZero() -> True if toByte(0) returns a value <= 0, False otherwise."""
        pass

class MenuBar(object):

    def name(self):
        """self.name() -> String
Returns the name of the menu item."""
        return ''

    def addSeparator(self,**kwargs):
        """self.addSeparator(**kwargs) -> The separator that was created.
Add a separator to this menu/toolbar.
@param **kwargs The following keyword arguments are accepted:
index     The position to insert the new separator in, in the menu/toolbar.
@return: The separator that was created.
"""
        return MenuItem()

    def menu(self,name):
        """self.menu(name) -> Menu or None
Finds a submenu or command with a particular name.
@param name: The name to search for.
@return: The submenu or command we found, or None if we could not find anything.
"""
        return Menu()

    def addCommand(self, name, command, shortcut, icon, tooltip, index, readonly):
        """self.addCommand(name, command, shortcut, icon, tooltip, index, readonly) -> The menu/toolbar item that was added to hold the command.
Add a new command to this menu/toolbar. Note that when invoked, the command is automatically enclosed in an undo group, so that undo/redo functionality works. Optional arguments can be specified by name.
Note that if the command argument is not specified, then the command will be auto-created as a "nuke.createNode()" using the name argument as the node to create.

Example:
menubar = nuke.menu('Nuke')
fileMenu = menubar.findItem('File')
fileMenu.addCommand('NewCommand', 'print 10', shortcut='t')

@param name: The name for the menu/toolbar item. The name may contain submenu names delimited by '/' or '', and submenus are created as needed.
@param command: Optional. The command to add to the menu/toolbar. This can be a string to evaluate or a Python Callable (function, method, etc) to run.
@param shortcut: Optional. The keyboard shortcut for the command, such as 'R', 'F5' or 'Ctrl-H'. Note that this overrides pre-existing other uses for the shortcut.
@param icon: Optional. An icon for the command. This should be a path to an icon in the nuke.pluginPath() directory. If the icon is not specified, Nuke will automatically try to find an icon with the name argument and .png appended to it.
@param tooltip: Optional. The tooltip text, displayed on mouseover for toolbar buttons.
@param index: Optional. The position to insert the new item in, in the menu/toolbar. This defaults to last in the menu/toolbar.
@param readonly: Optional. True/False for whether the item should be available when the menu is invoked in a read-only context.
@return: The menu/toolbar item that was added to hold the command.
"""
        return MenuItem()

    def addMenu(self,**kwargs):
        """self.addMenu(**kwargs) -> The submenu that was added.
Add a new submenu.
@param **kwargs The following keyword arguments are accepted:
                name      The name for the menu/toolbar item
                icon      An icon for the menu. Loaded from the nuke search path.
                tooltip   The tooltip text.
                index     The position to insert the menu in. Use -1 to add to the end of the menu.
@return: The submenu that was added.
"""
        return Menu()

    def removeItem(self,name):
        """self.removeItem(name) -> None
Removes a submenu or command with a particular name. If the containing menu becomes empty, it will be removed too.
@param name: The name to remove for.
@return: true if removed, false if menu not found
"""
        pass

    def items(self):
        """self.items() -> None
Returns a list of sub menu items."""
        pass

    def findItem(self,name):
        """self.findItem(name) -> Menu or None
Finds a submenu or command with a particular name.
@param name: The name to search for.
@return: The submenu or command we found, or None if we could not find anything.
"""
        return Menu()

    def clearMenu(self):
        """self.clearMenu()
Clears a menu.
@param **kwargs The following keyword arguments are accepted:
                name      The name for the menu/toolbar item
@return: true if cleared, false if menu not found
"""
        pass

class MenuItem(object):

    def setEnabled(self,enabled):
        """self.setEnabled(enabled) -> None
Enable or disable the item.
@param enabled: True to enable the object; False to disable it.
"""
        pass

    def name(self):
        """self.name() -> String
Returns the name of the menu item."""
        return ''


    def invoke(self):
        """self.invoke() -> None
Perform the action associated with this menu item."""
        pass

    def script(self):
        """self.script() -> String
Returns the script that gets executed for this menu item.
"""
        return ''

    def setScript(self,script):
        """self.setScript(script) -> None
Set the script to be executed for this menu item.
Note: To call a python script file, you can use the execfile() function. i.e:
menu.setScript("execfile('script.py')")
"""
        pass

    def setShortcut(self,keySequence):
        """self.setShortcut(keySequence) -> None
Set the keyboard shortcut on this menu item.
@param keySequence: the new shortcut in PortableText format, e.g. "Ctrl+Shift+P"
"""
        pass

    def shortcut(self):
        """self.shortcut() -> String
Returns the keyboard shortcut on this menu item. The format of this is the PortableText format. It will return a string such as "Ctrl+Shift+P". Note that on Mac OS X the Command key is equivalent to Ctrl."""
        return ''

    def setIcon(self,icon):
        """self.setIcon(icon) -> None
Set the icon on this menu item.
@param icon: the new icon as a path
"""
        pass

    def icon(self):
        """self.icon() -> String
Returns the name of the icon on this menu item as path of the icon."""
        return ''

class OutputContext(object):

    def viewcount(self):
        """viewcount() -> int

Return number of views."""
        pass

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def viewname(self,n):
        """viewname(n) -> string

Return name of the view. The n argument is an integer in the range of 0 to number of views."""
        return ''

    def setFrame(self,f):
        """setFrame(f) -> True

Set frame value. The f argument is a float."""
        pass

    def frame(self):
        """frame() -> float

Return frame value."""
        return 0.0

    def setView(self,n):
        """setView(n) -> True

Set view number. The n argument is an integer in the range of 0 to number of views."""
        pass

    def viewshort(self,n):
        """viewshort(n) -> string

Return short name of the view. The n argument is an integer in the range of 0 to number of views."""
        return ''

    def view(self):
        """view() -> int

Return view number."""
        return 0

class Panel(object):
    def addEnumerationPulldown(self):
        """self.addEnumerationPulldown(name, value) -> True if successful.
Add a pulldown menu to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def show(self):
        """self.show() -> An int value indicating how the dialog was closed (normally, or cancelled).
Display the panel.
@return: An int value indicating how the dialog was closed (normally, or cancelled).
"""
        pass

    def setTitle(self,val):
        """self.setTitle(val) -> True if successful.
Set the current title for the panel.
@param val: The title as a string.
@return: True if successful.
"""
        pass

    def addButton(self):
        """self.addButton(name, value) -> True if successful.
Add a button to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def addPasswordInput(self):
        """self.addPasswordInput(name, value) -> True if successful.
Add a password input knob to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def value(self,name):
        """self.value(name) -> The value for the field if any, otherwise None.
Get the value of a particular control in the panel.
@param name: The name of the knob to get a value from.
@return: The value for the field if any, otherwise None.
"""
        pass

    def setWidth(self,val):
        """self.setWidth(val) -> True if successful.
Set the width of the panel.
@param val: The width as an int.
@return: True if successful.
"""
        pass

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def title(self):
        """self.title() -> The title as a string.
Get the current title for the panel.
@return: The title as a string.
"""
        return ''

    def addMultilineTextInput(self,name, value):
        """self.addMultilineTextInput(name, value) -> True if successful.
Add a multi-line text knob to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def width(self):
        """self.width() -> The width as an int.
Get the width of the panel.
@return: The width as an int.
"""
        return 0

    def addRGBColorChip(self,name, value):
        """self.addRGBColorChip(name, value) -> True if successful.
Add a color chooser to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def addClipnameSearch(self,name, value):
        """self.addClipnameSearch(name, value) -> True if successful.
Add a clipname search knob to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def addNotepad(self,name, value):
        """self.addNotepad(name, value) -> True if successful.
Add a text edit widget to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def addScriptCommand(self,name, value):
        """self.addScriptCommand(name, value) -> True if successful.
Add a script command evaluator to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def addSingleLineInput(self,name, value):
        """self.addSingleLineInput(name, value) -> True if successful.
Add a single-line input knob to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def addTextFontPulldown(self,name, value):
        """self.addTextFontPulldown(name, value) -> True if successful.
Add a font chooser to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def execute(self,name):
        """self.execute(name) -> The result of the script as a string, or None if it fails.
Execute the script command associated with a particular label and return the result as a string.
@param name: The name of the script field to execute.
@return: The result of the script as a string, or None if it fails.
"""
        return ''

    def clear(self):
        """self.clear() -> None
Clear all panel attributes.
"""
        pass

    def addFilenameSearch(self, name, value):
        """self.addFilenameSearch(name, value) -> True if successful.
Add a filename search knob to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

    def addBooleanCheckBox(self, name, value):
        """self.addBooleanCheckBox(name, value) -> True if successful.
Add a boolean check box knob to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass


    def addExpressionInput(self, name, value):
        """self.addExpressionInput(name, value) -> True if successful.
Add an expression evaluator to the panel.
@param name: The name for the new knob.
@param value: The initial value for the new knob.
@return: True if successful.
"""
        pass

class PanelNode(object):

    def writeKnobs(self,i):
        """self.writeKnobs(i) -> String in .nk form.
Return a tcl list. If TO_SCRIPT | TO_VALUE is not on, this is a simple list
of knob names. If it is on, it is an alternating list of knob names
and the output of to_script().

Flags can be any of these or'd together:
- nuke.TO_SCRIPT produces to_script(0) values
- nuke.TO_VALUE produces to_script(context) values
- nuke.WRITE_NON_DEFAULT_ONLY skips knobs with not_default() false
- nuke.WRITE_USER_KNOB_DEFS writes addUserKnob commands for user knobs
- nuke.WRITE_ALL writes normally invisible knobs like name, xpos, ypos

@param i: The set of flags or'd together. Default is TO_SCRIPT | TO_VALUE.
@return: String in .nk form.
"""
        return ''

    def createWidget(self):
        """Create the widget for the panel"""
        pass

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def __str__(self):
        """x.__str__() <==> str(x)"""
        pass

    def addKnob(self,k):
        """self.addKnob(k) -> None.
Add knob k to this node or panel.
@param k: Knob.
@return: None.
"""
        pass

    def removeKnob(self,k):
        """self.removeKnob(k) -> None.
Remove knob k from this node or panel. Throws a ValueError exception if k is not found on the node.
@param k: Knob.
@return: None.
"""
        pass

    def knobs(self):
        """self.knobs() -> dict

Get a dictionary of (name, knob) pairs for all knobs in this node.

For example:

   >>> b = nuke.nodes.Blur()
   >>> b.knobs()

@return: Dictionary of all knobs.
"""
        return {'':Knob(),}

    def readKnobs(self,s):
        """self.readKnobs(s) -> None.
Read the knobs from a string (TCL syntax).
@param s: A string.
@return: None.
"""
        pass

class LinkableKnobInfo(object):
    def knob(self):
        """self.knob() -> Knob
Returns the knob that may be linked to."""
        return Knob()

    def __setattr__(self):
        """x.__setattr__('name', value) <==> x.name = value"""
        pass

    def enabled(self):
        """self.enabled() -> Boolean
Returns whether the knob is currently enabled or not."""
        pass

    def __getattribute__(self,name):
        """x.__getattribute__('name') <==> x.name"""
        pass

    def __delattr__(self,name):
        """x.__delattr__('name') <==> del x.name"""
        pass

    def absolute(self):
        """self.absolute() -> Boolean
Returns whether the values of this knob should be treated as absolute or relative. This may be useful for positions."""
        pass

class ProgressTask(object):

    def setProgress(self,i):
        """self.setProgress(i) -> None.

i is an integer representing the current progress
"""
        pass

    def isCancelled(self):
        """self.isCancelled() -> True if the user has requested the task to be cancelled.

"""
        pass

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def setMessage(self,s):
        """self.setMessage(s) -> None.

set the message for the progress task
"""
        pass

class RunInMainThread(object):

    def request(self):
        """None"""
        pass

    def result(self):
        """None"""
        pass

class ToolBar(object):

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def addSeparator(self,**kwargs):
        """self.addSeparator(**kwargs) -> The separator that was created.
Add a separator to this menu/toolbar.
@param **kwargs The following keyword arguments are accepted:
index     The position to insert the new separator in, in the menu/toolbar.
@return: The separator that was created.
"""
        return MenuItem()


    def menu(self,name):
        """self.menu(name) -> Menu or None
Finds a submenu or command with a particular name.
@param name: The name to search for.
@return: The submenu or command we found, or None if we could not find anything.
"""
        return Menu()

    def addCommand(self, name, command, shortcut, icon, tooltip, index, readonly):
        """self.addCommand(name, command, shortcut, icon, tooltip, index, readonly) -> The menu/toolbar item that was added to hold the command.
Add a new command to this menu/toolbar. Note that when invoked, the command is automatically enclosed in an undo group, so that undo/redo functionality works. Optional arguments can be specified by name.
Note that if the command argument is not specified, then the command will be auto-created as a "nuke.createNode()" using the name argument as the node to create.

Example:
menubar = nuke.menu('Nuke')
fileMenu = menubar.findItem('File')
fileMenu.addCommand('NewCommand', 'print 10', shortcut='t')

@param name: The name for the menu/toolbar item. The name may contain submenu names delimited by '/' or '', and submenus are created as needed.
@param command: Optional. The command to add to the menu/toolbar. This can be a string to evaluate or a Python Callable (function, method, etc) to run.
@param shortcut: Optional. The keyboard shortcut for the command, such as 'R', 'F5' or 'Ctrl-H'. Note that this overrides pre-existing other uses for the shortcut.
@param icon: Optional. An icon for the command. This should be a path to an icon in the nuke.pluginPath() directory. If the icon is not specified, Nuke will automatically try to find an icon with the name argument and .png appended to it.
@param tooltip: Optional. The tooltip text, displayed on mouseover for toolbar buttons.
@param index: Optional. The position to insert the new item in, in the menu/toolbar. This defaults to last in the menu/toolbar.
@param readonly: Optional. True/False for whether the item should be available when the menu is invoked in a read-only context.
@return: The menu/toolbar item that was added to hold the command.
"""
        pass

    def addMenu(self,**kwargs):
        """self.addMenu(**kwargs) -> The submenu that was added.
Add a new submenu.
@param **kwargs The following keyword arguments are accepted:
                name      The name for the menu/toolbar item
                icon      An icon for the menu. Loaded from the nuke search path.
                tooltip   The tooltip text.
                index     The position to insert the menu in. Use -1 to add to the end of the menu.
@return: The submenu that was added.
"""
        pass

    def name(self):
        """self.name() -> String
Returns the name of the menu item."""
        return ''

    def removeItem(self,name):
        """self.removeItem(name) -> None
Removes a submenu or command with a particular name. If the containing menu becomes empty, it will be removed too.
@param name: The name to remove for.
@return: true if removed, false if menu not found
"""
        pass

    def items(self):
        """self.items() -> None
Returns a list of sub menu items."""
        pass

    def findItem(self,name):
        """self.findItem(name) -> Menu or None
Finds a submenu or command with a particular name.
@param name: The name to search for.
@return: The submenu or command we found, or None if we could not find anything.
"""
        return Menu()

    def clearMenu(self):
        """self.clearMenu()
Clears a menu.
@param **kwargs The following keyword arguments are accepted:
                name      The name for the menu/toolbar item
@return: true if cleared, false if menu not found
"""
        pass

class Undo(object):

    def disabled(self):
        """True if disable() has been called"""
        pass

    def undoDescribe(self):
        """Return short description of undo n."""
        return ''

    def cancel(self):
        """Undoes any actions recorded in the current set and throws it away."""
        pass

    def redo(self):
        """Redoes 0'th redo."""
        pass

    def undoSize(self):
        """Number of undo's that can be done."""
        return 0

    def end(self):
        """Complete current undo set and add it to the undo list."""
        pass

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def redoDescribe(self):
        """Return short description of redo n."""
        pass

    def __enter__(self):
        """None"""
        pass
    def __exit__(self):
        """None"""
        pass

    def redoDescribeFully(self):
        """Return long description of redo n."""
        pass

    def new(self):
        """Same as end();begin()."""
        pass

    def redoTruncate(self):
        """Destroy any redo's greater or equal to n."""
        pass

    def undoTruncate(self):
        """Destroy any undo's greater or equal to n."""
        pass

    def begin(self):
        """Begin a new user-visible group of undo actions."""
        pass

    def enable(self):
        """Undoes the previous disable()"""
        pass

    def undo(self):
        """Undoes 0'th undo."""
        pass

    def disable(self):
        """Prevent recording undos until matching enable()"""
        pass

    def redoSize(self):
        """Number of redo's that can be done."""
        return 0

    def name(self):
        """Name current undo set."""
        return ''

    def undoDescribeFully(self):
        """Return long description of undo n."""
        pass

class View(object):
    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def __str__(self):
        """x.__str__() <==> str(x)"""
        pass

    def value(self):
        """self.value() -> Value of view.
@return: Value of view.
"""
        return 0

    def __init__(self):
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signature"""
        pass

    def string(self):
        """self.string() -> Name of view.
@return: Name of view.
"""
        return ''

class ViewerProcess(object):

    def unregister(self,name):
        """nuke.ViewerProcess.unregister(name) -> None.
Unregister a ViewerProcess. This is a class method.
@param name: Menu name.
@return: None.
"""
        pass

    def node(self):
        """nuke.ViewerProcess.node(name, viewer) -> Node.
Returns a ViewerProcess node. Default is to return the current selected one. This is a class method.
@param name: Optional ViewerProcess name.
@param viewer: Optional viewer name.
@return: Node.
"""
        return Node()

    def register(self, name, call, args, kwargs):
        """nuke.ViewerProcess.register(name, call, args, kwargs) -> None.
Register a ViewerProcess. This is a class method.
@param name: Menu name.
@param call: Python callable. Must return a Node.
@param args: Arguments to call.
@param kwargs: Optional named arguments.
@return: None.
"""
        pass

    def registeredNames(self):
        """nuke.ViewerProcess.registeredNames() -> List.
Returns a list containing the names of all currently regisered ViewerProcesses.
@return: List.
"""
        pass

class ViewerWindow(object):
    def node(self):
        """self.node() -> Node.
Returns the Viewer node currently associated with this window.
@return: Node.
"""
        return Node()

    def activeInput(self,secondary=False):
        """self.activeInput(secondary=False) -> int
Returns the currently active input of the viewer - i. e. the one with its image in the output window.
@param secondary: True to return the index of the active secondary (wipe) input, or False (the default)
to return the primary input.
@return: int: The currently active input of the viewer, starting with 0 for the first, or None if no input is active.
"""
        return 0

    def play(self):
        """Play forward (1) or reverse (0)."""
        pass

    def previousView(self):
        """self.previousView() -> switch to previous view in settings Views list.
"""
        pass

    def nextView(self):
        """self.nextView() -> switch to next view in settings Views list.
"""
        pass

    def getGeometryNodes(self):
        """self.getGeometry() -> None
Returns the a list of geometry nodes attached with this viewer
@return: Nodes: a list of the geometry nodes.
"""
        pass

    def stop(self):
        """Stop playing."""
        pass

    def activateInput(self,input, secondary=False):
        """self.activateInput(input, secondary=False) -> None
Set the given viewer input to be active - i. e. show its image in the output window.
@param input: The viewer input number, starting with 0 for the first.  If the input is not
connected, a ValueError exception is raised.
@param secondary: True if the input should be connected as the secondary (wipe) input, or
False to connect it as the primary input (the default).
@return: None
"""
        pass

    def setView(self,s):
        """self.setView(s) -> set 'current' multi-view view to 's'.
"""
        pass

    def frameControl(self,i):
        """self.frameControl(i) -> True.

i is an integer indicating viewer frame control 'button' to execute:

   -6 go to start
   -5 play reverse
   -4 go to previous keyframe
   -3 step back by increment
   -2 go back previous keyframe or increment, whichever is closer
   -1 step back one frame

    0 stop

   +1 step forward one frame
   +2 go to next keyframe or increment, whichever is closer
   +3 step forward by increment
   +4 go to next keyframe
   +5 play forward
   +6 go to end
"""
        pass

    def view(self):
        """self.view() -> string name of 'current' multi-view view.
"""
        pass

class Group(Node):
    def node(self,s):
        """self.node(s) -> Node with name s or None.
Locate a node by name.
@param s: A string.
@return: Node with name s or None.
"""
        return Node()

    def __enter__(self):
        """None"""
        return Group()

    def __exit__(self):
        """None"""
        pass

    def begin(self):
        """self.begin() -> Group.
All python code that follows will be executed in the context of node. All names are evaluated relative to this object. Must be paired with end.
@return: Group.
"""
        return Group()

    def run(self,callable):
        """self.run(callable) -> Result of callable.
Execute in the context of node. All names are evaluated relative to this object.
@param callable: callable to execute.
@return: Result of callable.
"""
        pass

    def numNodes(self):
        """self.numNodes() -> Number of nodes
Number of nodes in group.
@return: Number of nodes
"""
        return 0

    def connectSelectedNodes(self, backward, inputA):
        """self.connectSelectedNodes(backward, inputA) -> None.
Connect the selected nodes.
@param backward.
@param inputA.
@return: None.
"""
        pass

    def selectedNode(self):
        """self.selectedNode() -> Node or None.
Returns the node the user is most likely thinking about. This is the last node the user clicked on, if it is selected.  Otherwise it is an 'output' (one with no selected outputs) of the set of selected nodes. If no nodes are selected then None is returned.
@return: Node or None.
"""
        return Node()

    def selectedNodes(self):
        """self.selectedNodes() -> Node or None.
Selected nodes.
@return: Node or None.
"""
        return Node()

    def __reduce_ex__(self):
        """None"""
        pass

    def output(self):
        """self.output() -> Node or None.
Return output node of group.
@return: Node or None.
"""
        return Node()

    def expand(self):
        """self.expand() -> None.
Moves all nodes from the group node into its parent group, maintaining node input
and output connections, and deletes the group.
Returns the nodes that were moved, which will also be selected.
@return: None.
"""
        pass

    def end(self):
        """self.end() -> None.
All python code that follows will no longer be executed in the context of node. Must be paired with begin.
@return: None.
"""
        pass

    def nodes(self):
        """self.nodes() -> List of nodes
List of nodes in group.
@return: List of nodes
"""
        return [Node(),]

    def splaySelectedNodes(self, backward, inputA):
        """self.splaySelectedNodes(backward, inputA) -> None.
Splay the selected nodes.
@param backward.
@param inputA.
@return: None.
"""
        pass

class Gizmo(Group):
    def filename(self):
        """self.filename() -> String.
Gizmo filename.
@return: String.
"""
        return ''

    def command(self):
        """self.command() -> String.
Gizmo command.
@return: String.
"""
        return ''

    def makeGroup(self):
        """self.makeGroup() -> Group
Creates a Group node copy of the Gizmo node.
@return: Group.
"""
        return Group()

class Precomp(Group):

    def reload(self):
        """self.reload() -> None
Precomp Node reload()
@return: None
"""
        pass

class Root(Group):

    def lastFrame(self):
        """self.lastFrame() -> Integer.
Last frame.
@return: Integer.
"""
        return 0

    def __str__(self):
        """x.__str__() <==> str(x)"""
        pass

    def maximumInputs(self):
        """None"""
        return 0

    def modified(self):
        """self.modified() -> True if modified, False otherwise.
Get or set the 'modified' flag in a script
@return: True if modified, False otherwise.
"""
        pass

    def channels(self):
        """nuke.Root.channels() -> Channel list.
Class method.
@return: Channel list.
"""
        return ['',]

    def setInput(self, i, node):
        """None"""
        pass

    def canSetInput(self):
        """None"""
        pass

    def maximumOutputs(self):
        """None"""
        return 0

    def minimumInputs(self):
        """None"""
        return 0

    def firstFrame(self):
        """self.firstFrame() -> Integer.
First frame.
@return: Integer.
"""
        return 0

    def layers(self):
        """nuke.Root.layers() -> Layer list.
Class method.
@return: Layer list.
"""
        return [Layer(), ]

    def __new__(self,S, ):
        """T.__new__(S, ...) -> a new object with type S, a subtype of T"""
        pass

    def connectInput(self):
        """None"""
        pass

    def fps(self):
        """self.fps() -> Integer.
FPS.
@return: Integer.
"""
        return 0

    def setProxy(self,b):
        """self.setProxy(b) -> None.
Set proxy.
@param b: Boolean convertible object.
@return: None.
"""
        pass

    def input(self):
        """None"""
        pass

    def addView(self,s):
        """self.addView(s) -> None.
Add view.
@param s: Name of view.
@return: None.
"""
        pass

    def deleteView(self,s):
        """self.deleteView(s) -> None.
Delete view.
@param s: Name of view.
@return: None.
"""
        pass

    def inputs(self):
        """None"""
        return 0


    def __getitem__(self,y):
        """x.__getitem__(y) <==> x[y]"""
        pass

    def mergeFrameRange(self, a, b):
        """self.mergeFrameRange(a, b) -> None.
Merge frame range.
@param a: Low-end of interval range.
@param b: High-end of interval range.
@return: None.
"""
        pass

    def setModified(self,b):
        """self.setModified(b) -> None.
Set the 'modified' flag in a script.
Setting the value will turn the indicator in the title bar on/off and will start or stop the autosave timeout.
@param b: Boolean convertible object.
@return: None.
"""
        pass

    def proxy(self):
        """self.proxy() -> True if proxy is set, False otherwise.
@return: True if proxy is set, False otherwise.
"""
        pass

    def clones(self):
        """None"""
        return 0

    def setView(self,s):
        """self.setView(s) -> None.
Set view.
@param s: Name of view.
@return: None.
"""
        pass

    def setFrame(self,n):
        """self.setFrame(n) -> None.
Set frame.
@param n: Frame number.
@return: None.
"""
        pass

    def optionalInput(self):
        """None"""
        pass

class Viewer(Node):

    def roi(self):
        """self.roi() -> dict
Region of interest set in the viewer in pixel space coordinates.
Returns None if the Viewer has no window yet.
@return: Dict with keys x, y, r and t or None.
"""
        return {}

    def setRoi(self, box):
        """self.setRoi(box) -> None.
Set the region of interest in pixel space.
@param box: A dictionary with the x, y, r and t keys.@return: None.
"""
        pass

    def __getitem__(self,y):
        """x.__getitem__(y) <==> x[y]"""
        return 0

    def playbackRange(self):
        """self.playbackRange() -> FrameRange.
Return the frame range that's currently set to be played back in the viewer.@return: FrameRange.
"""
        return FrameRange()

    def roiEnabled(self):
        """self.roiEnabled() -> bool
Whether the viewing of just a region of interest is enabled.
Returns None if the Viewer has no window yet.
@return: Boolean or None.
"""
        pass

    def __len__(self):
        """x.__len__() <==> len(x)"""
        pass


# MENU

class Menu(MenuItem):

    def name(self):
        """self.name() -> String
Returns the name of the menu item."""
        return ''


    def addSeparator(self,**kwargs):
        """self.addSeparator(**kwargs) -> The separator that was created.
Add a separator to this menu/toolbar.
@param **kwargs The following keyword arguments are accepted:
index     The position to insert the new separator in, in the menu/toolbar.
@return: The separator that was created.
"""
        pass

    def menu(self,name):
        """self.menu(name) -> Menu or None
Finds a submenu or command with a particular name.
@param name: The name to search for.
@return: The submenu or command we found, or None if we could not find anything.
"""
        return Menu()

    def addCommand(self, name, command, shortcut, icon, tooltip, index, readonly):
        """self.addCommand(name, command, shortcut, icon, tooltip, index, readonly) -> The menu/toolbar item that was added to hold the command.
Add a new command to this menu/toolbar. Note that when invoked, the command is automatically enclosed in an undo group, so that undo/redo functionality works. Optional arguments can be specified by name.
Note that if the command argument is not specified, then the command will be auto-created as a "nuke.createNode()" using the name argument as the node to create.

Example:
menubar = nuke.menu('Nuke')
fileMenu = menubar.findItem('File')
fileMenu.addCommand('NewCommand', 'print 10', shortcut='t')

@param name: The name for the menu/toolbar item. The name may contain submenu names delimited by '/' or '', and submenus are created as needed.
@param command: Optional. The command to add to the menu/toolbar. This can be a string to evaluate or a Python Callable (function, method, etc) to run.
@param shortcut: Optional. The keyboard shortcut for the command, such as 'R', 'F5' or 'Ctrl-H'. Note that this overrides pre-existing other uses for the shortcut.
@param icon: Optional. An icon for the command. This should be a path to an icon in the nuke.pluginPath() directory. If the icon is not specified, Nuke will automatically try to find an icon with the name argument and .png appended to it.
@param tooltip: Optional. The tooltip text, displayed on mouseover for toolbar buttons.
@param index: Optional. The position to insert the new item in, in the menu/toolbar. This defaults to last in the menu/toolbar.
@param readonly: Optional. True/False for whether the item should be available when the menu is invoked in a read-only context.
@return: The menu/toolbar item that was added to hold the command.
"""
        pass

    def addMenu(self,**kwargs):
        """self.addMenu(**kwargs) -> The submenu that was added.
Add a new submenu.
@param **kwargs The following keyword arguments are accepted:
                name      The name for the menu/toolbar item
                icon      An icon for the menu. Loaded from the nuke search path.
                tooltip   The tooltip text.
                index     The position to insert the menu in. Use -1 to add to the end of the menu.
@return: The submenu that was added.
"""
        pass

    def removeItem(self,name):
        """self.removeItem(name) -> None
Removes a submenu or command with a particular name. If the containing menu becomes empty, it will be removed too.
@param name: The name to remove for.
@return: true if removed, false if menu not found
"""
        pass

    def items(self):
        """self.items() -> None
Returns a list of sub menu items."""
        return [MenuItem,]

    def findItem(self,name):
        """self.findItem(name) -> Menu or None
Finds a submenu or command with a particular name.
@param name: The name to search for.
@return: The submenu or command we found, or None if we could not find anything.
"""
        return Menu()

    def clearMenu(self):
        """self.clearMenu()
Clears a menu.
@param **kwargs The following keyword arguments are accepted:
                name      The name for the menu/toolbar item
@return: true if cleared, false if menu not found
"""
        pass

class Element(object):
    locked=True
    #Whether this element is locked.
    name=''
    #The name for this element.
    def getVisible(self, time):
        """
        Get the value of the visible attribute at a particular time.
        :param time:
        :return: bool
        """
        return True
    def setVisible(self, time, value):
        """
        Set the value of the visible attribute at a particular time.
        :param time:
        :param value:
        """
        pass

# FUNC

def IrToken():
    """Nuke internal. Not for public use."""
    pass

def __filterNames(name):
    """None"""
    pass

def activeViewer():
    """activeViewer() -> Viewer

Return an object representing the active Viewer panel. This
is not the same as the Viewer node, this is the viewer UI element.

@return: Object representing the active Viewer"""
    return ViewerWindow()

def addAfterBackgroundFrameRender(call,args,kwargs):
    """Add code to execute after each frame of a background render.
  The call must be in the form of:
  def foo(context):
    pass

  The context object that will be passed in is a dictionary containing the following elements:
  id => The identifier for the task that's making progress
  frame => the current frame number being rendered
  numFrames => the total number of frames that is being rendered
  frameProgress => the number of frames rendered so far.

  Please be aware that the current Nuke context will not make sense in the callback (e.g. nuke.thisNode will return a random node).
  """
    pass

def addAfterBackgroundRender(call,args,kwargs):
    """Add code to execute after any background renders.
  The call must be in the form of:
  def foo(context):
    pass

  The context object that will be passed in is a dictionary containing the following elements:
  id => The identifier for the task that's ended

  Please be aware that the current Nuke context will not make sense in the callback (e.g. nuke.thisNode will return a random node).
  """
    pass

def addAfterFrameRender(call,args,kwargs,nodeClass):
    """Add code to execute after each frame of a render"""
    pass

def addAfterRender(call,args,kwargs,nodeClass):
    """Add code to execute after any renders"""
    pass

def addAutoSaveDeleteFilter(filter):
    """addAutoSaveDeleteFilter(filter) -> None

  Add a function to modify the autosave filename before Nuke attempts delete the autosave file.

  Look at rollingAutoSave.py in the nukescripts directory for an example of using the auto save filters.

  @param filter: A filter function.  The first argument to the filter is the current autosave filename.
  This function should return the filename to delete or return None if no file should be deleted."""
    pass

def addAutoSaveFilter(filter):
    """addAutoSaveFilter(filter) -> None

  Add a function to modify the autosave filename before Nuke saves the current script on an autosave timeout.

  Look at rollingAutoSave.py in the nukescripts directory for an example of using the auto save filters.

  @param filter: A filter function.  The first argument to the filter is the current autosave filename.
  The filter should return the filename to save the autosave to."""
    pass

def addAutoSaveRestoreFilter(filter):
    """addAutoSaveRestoreFilter(filter) -> None

  Add a function to modify the autosave restore file before Nuke attempts to restores the autosave file.

  Look at rollingAutoSave.py in the nukescripts directory for an example of using the auto save filters.

  @param filter: A filter function.  The first argument to the filter is the current autosave filename.
  This function should return the filename to load autosave from or it should return None if the autosave file should be ignored."""
    pass

def addAutolabel(call,args,kwargs,nodeClass):
    """Add code to execute on every node to produce the text to draw on it
  in the DAG. Any value other than None is converted to a string and used
  as the text. None indicates that previously-added functions should
  be tried"""
    pass

def addBeforeBackgroundRender(call,args,kwargs):
    """Add code to execute before starting any background renders.
  The call must be in the form of:
  def foo(context):
    pass

  The context object that will be passed in is a dictionary containing the following elements:
  id => The identifier for the task that's about to begin

  Please be aware that the current Nuke context will not make sense in the callback (e.g. nuke.thisNode will return a random node).
  """
    pass

def addBeforeFrameRender(call,args,kwargs,nodeClass):
    """Add code to execute before each frame of a render"""
    pass

def addBeforeRender(call,args,kwargs,nodeClass):
    """Add code to execute before starting any renders"""
    pass

def addFavoriteDir(name, directory, type, icon, tooltip, key):
    """addFavoriteDir(name, directory, type, icon, tooltip, key) -> None.

Add a path to the file choosers favorite directory list. The path name can contain environment variables which will be expanded when the user clicks the favourites button

@param name: Favourite path entry ('Home', 'Desktop', etc.).
@param directory: FileChooser will change to this directory path.
@param type: Optional bitwise OR combination of nuke.IMAGE, nuke.SCRIPT, nuke.FONT or nuke.GEO.
@param icon: Optional filename of an image to use as an icon.
@param tooltip: Optional short text to explain the path and the meaning of the name.
@param key: Optional shortcut key.
@return: None.
"""
    pass

def addFilenameFilter(call,args,kwargs,nodeClass):
    """Add a function to modify filenames before Nuke passes them to
  the operating system. The first argument to the function is the
  filename, and it should return the new filename. None is the same as
  returning the string unchanged. All added functions are called
  in backwards order."""
    pass

def addFormat(s):
    """addFormat(s) -> Format or None.

Create a new image format, which will show up on the pull-down menus for image formats. You must give a width and height and name. The xyrt rectangle describes the image area, if it is smaller than the width and height (for Academy aperture, for example). The pixel aspect is the ratio of the width of a pixel to the height.

@param s: String in TCL format "w h ?x y r t? ?pa? name".
@return: Format or None.
"""
    return Format()

def addKnobChanged(call,args,kwargs,nodeClass='',node=None):
    """Add code to execute when the user changes a knob
  The knob is availble in nuke.thisKnob() and the node in nuke.thisNode().
  This is also called with dummy knobs when the control panel is opened
  or when the inputs to the node changes. The purpose is to update other
  knobs in the control panel. Use addUpdateUI() for changes that
  should happen even when the panel is closed."""
    pass

def addNodePresetExcludePaths( paths ):
    """addNodePresetExcludePaths( paths ) -> None
@param paths Sequence of paths to exclude
Adds a list of paths that will be excluded from Node preset search paths.
@return: None."""
    pass

def addOnCreate(call,args,kwargs,nodeClass):
    """Add code to execute when a node is created or undeleted"""
    pass

def addOnDestroy(call,args,kwargs,nodeClass):
    """Add code to execute when a node is destroyed"""
    pass

def addOnScriptClose(call,args,kwargs,nodeClass):
    """Add code to execute before a script is closed"""
    pass

def addOnScriptLoad(call,args,kwargs,nodeClass):
    """Add code to execute when a script is loaded"""
    pass

def addOnScriptSave(call,args,kwargs,nodeClass):
    """Add code to execute before a script is saved"""
    pass

def addOnUserCreate(call,args,kwargs,nodeClass):
    """Add code to execute when user creates a node"""
    pass

def addToolsetExcludePaths( paths ):
    """addToolsetExcludePaths( paths ) -> None
@param paths Sequence of paths to exclude
Adds a list of paths that will be excluded from Toolset search paths.
@return: None."""
    pass

def addUpdateUI(call,args,kwargs,nodeClass):
    """Add code to execute on every node when things change. This is done
  during idle, you cannot rely on it being done before it starts updating
  the viewer"""
    pass

def addValidateFilename(call,args,kwargs,nodeClass):
    """Add a function to validate a filename in Write nodes. The first argument
  is the filename and it should return a Boolean as to whether the filename is valid
  or not. If a callback is provided, it will control whether the Render button of Write nodes
  and the Execute button of WriteGeo nodes is enabled or not."""
    pass

def addView(name):
    """addView(s) -> None

Deprecated. Use the Root node.

Adds a new view to the list of views.

@param s: View name.
@return: None
"""
    pass

def afterBackgroundFrameRender(context):
    """None"""
    pass

def afterBackgroundRender(context):
    """None"""
    pass

def afterFrameRender():
    """None"""
    pass

def afterRender():
    """None"""
    pass

def allNodes(filter=None, group=None):
    """allNodes(filter, group) -> List.
List of all nodes in a group. If you need to get all the nodes in the script
from a context which has no child nodes, for instance a control panel, use
nuke.root().nodes().

@param filter: Optional. Only return nodes of the specified class.
@param group: Optional. If the group is omitted the current group (ie the group the user picked a menu item from the toolbar of) is used.
@return: List"""
    return [Node(),]

def animation(object, *commands):
    """animation(object, *commands) -> None

Does operations on an animation curve.

The following commands are supported:
  - B{clear} deletes all the keys from the animation.
  - B{erase} C{index I{last_index}} removes all keyframes between index and last_index
  - B{expression} C{I{newvalue}} returns or sets the expression for
    the animation. The default is 'curve' or 'y' which returns the interpolation of the keys.
  - B{generate} C{start end increment field expression I{field expression} ...}
    generates an animation with start, end, and increment. Multiple field/expression pairs
    generate a keyframe. Possible field commands are:
      - B{x} sets the frame number for the next keyframe
      - B{y} sets the keyframe value
      - B{dy} sets the left slope
      - B{ldy} sets left and right slope to the same value
      - B{la} and B{ra} are the length of the slope handle in x direction. A value of 1
        generates a handle that is one third of the distance to the next keyframe.
  - B{index} C{x} returns the index of the last key with x <= t, return -1 for none.
  - B{is_key} return non-zero if there is a key with x == t. The actual return value is the index+1.
  - B{move} C{field expression I{field expression}} replaces all selected keys
    in an animation with new ones as explained above in B{generate}
  - B{name} returns a user-friendly name for this animation. This will eliminate
    any common prefix between this animation and all other selected ones,
    and also replaces mangled names returned by animations with nice ones.
  - B{size} returns the number of keys in the animation.
  - B{test} errors if no points in the animation are selected
  - B{y} index C{I{newvalue}} gets or sets the value of an animation.
  - B{x} index C{I{newvalue}} gets or sets the horizontal postion of a key.
    If the animation contains an expression or keyframes, the new value will be overridden.

See also: animations

@param object: The animation curve.
@param commands: a varargs-style list of commands, where each command is one of those defined above.
@return: None"""
    pass

def animationEnd():
    """animationEnd() -> float.

Returns the last frame (or x value) for the currently selected animations.
@return: The end frame."""
    return 0

def animationIncrement():
    """animationIncrement() -> float

Returns a recommended interval between samples of the currently selected animation.
@return: The recommended interval."""
    return 0

def animationStart():
    """animationStart() -> float

Returns the starting frame (or x value) for the currently selected animations.
@return: The start frame."""
    return 0

def animations():
    """animations() -> tuple

Returns a list of animatable things the user wants to work on.
If this is a command being executed from a menu item in a curve editor, a list of the names of all selected curves is returned. If this list is empty a "No curves selected" error is produced.
If this is a command being executed from the pop-up list in a knob then a list of all the fields in the knob is returned.
If this is a command being executed from the right-mouse-button pop-up list in a field of a knob, the name of that field is returned.
Otherwise this produces an error indicating that the command requries a knob context. You can get such a context by doing "in <knob> {command}"
Also see the 'selected' argument to the animation command.
See also: animation, animationStart, animationEnd, animationIncrement
@return: A tuple of animatable things."""
    return (AnimationCurve(),)

def applyPreset(nodeName, presetName):
    """applyPreset(nodeName, presetName) -> None
Applies a given preset to the current node.
@param presetName: Name of the preset to use.
@return: bool."""
    pass

def applyUserPreset(nodeName, presetName):
    """applyUserPreset(nodeName, presetName) -> None
Applies a given user preset to the current node.
@param presetName: Name of the preset to use.
@return: bool."""
    pass

def ask(prompt):
    """ask(prompt) -> bool

Show a Yes/No dialog.

@param prompt: Present the user with this message.
@return: True if Yes, False otherwise."""
    pass

def autoSaveDeleteFilter(filename):
    """Internal function.  Use addAutoSaveDeleteFilter to add a callback"""
    pass

def autoSaveFilter(filename):
    """Internal function.  Use addAutoSaveFilter to add a callback"""
    pass

def autoSaveRestoreFilter(filename):
    """Internal function.  Use addAutoSaveRestoreFilter to add a callback"""
    pass

def autolabel():
    """None"""
    pass

def autoplace(node):
    """autoplace(n) -> None.

Deprecated. Use Node.autoplace.

Automatically place nodes, so they do not overlap.

@param n: Node.
@return: None"""
    pass

def autoplaceSnap(node):
    """autoplaceSnap(n) -> None

Move node to the closest grid position.

@param n: Node.
@return: None"""
    pass

def beforeBackgroundRender(context):
    """None"""
    pass

def beforeFrameRender():
    """None"""
    pass

def beforeRender():
    """None"""
    pass

def cacheUsage():
    """cacheUsage() -> int

Get the total amount of memory currently used by the cache.

@return: Current memory usage in bytes.
"""
    return 0

def cancel():
    """cancel() -> None
Cancel an in-progress operation. This has the same effect as hitting cancel on the progress panel.

@return: None"""
    pass

def channels(node_parameter=None):
    """channels(n=None) -> (string)

Deprecated. Use Node.channels.

List channels. The n argument is a Nuke node and if given only the channels output by this node are listed. If not given or None, all channels known about are listed.

@param n: Optional node parameter.
@return: A list of channel names."""
    return ''

def choice(title, prompt, options, default = 0):
    """choice(title, prompt, options, default = 0) -> index

Shows a dialog box with the given title and prompt text, and a combo box containing the given options.

@param title: Text to put in the dialog's title bar.
@param prompt: Text to display at the top of the dialog.
@param options: A list of strings for the user to choose from.
@param default: The index (starting from zero) of the option to select first.
@return: An integer index (starting from zero) of the choice the user selected, or None if the dialog was cancelled."""
    return 0


def clearDiskCache():
    """clearDiskCache() -> None

Clear the disk cache of all files.
"""
    pass

def clone(n, args, inpanel):
    """clone(n, args, inpanel) -> Node

Create a clone node that behaves identical to the original. The node argument is the node to be cloned, args and inpanel are optional arguments similar to createNode.
A cloned node shares the exact same properties with its original. Clones share the same set of knobs and the same control panel. However they can
have different positions and connections in the render tree. Any clone, including the original, can be deleted at any time without harming any of its clones.

@param n: Node.
@param args: Optional number of inputs requested.
@param inpanel: Optional boolean.
@return: Node"""
    return Node()

def cloneSelected(action):
    """cloneSelected(action) -> bool

This makes a clone of all selected nodes, preserving connections between them, and makes only the clones be selected.

@param action: Optional and if 'copy' it cuts the resulting clones to the clipboard.
@return: True if succeeded, False otherwise."""
    pass

def collapseToGroup(show=True):
    """collapseToGroup(show=True) -> Group

Moves the currently selected nodes to a new group, maintaining their previous connections.

@param show: If show is True, the node graph for the new group is shown in the background.
@return: The new Group node.
"""
    return Group()

def connectNodes():
    """connectNodes() -> None

Deprecated. Use Group.connectSelectedNodes.

@return: None"""
    pass

def connectViewer(inputNum, node):
    """connectViewer(inputNum, node) -> None

Connect a viewer input to a node. The argument i is the input number and n is either a Nuke node or None.
Some viewer in the current group is found, if there are no viewers one is created. The viewer is then altered to have at least n+1 inputs and then input n is connected to the given node.This function is used by the numeric shortcuts in the DAG view menu.

@param inputNum: Input number.
@param node: The Node to connect to the input.
@return: None"""
    pass

def createNode(inpanel=True):
    """createNode(node, args, inpanel) -> Node.

Creates a node of the specified type and adds it to the DAG.

@param node: Node class (e.g. Blur).
@param args: Optional string containing a TCL list of name value pairs (like "size 50 quality 19")
@param inpanel: Optional boolean to open the control bin (default is True; only applies when the GUI is running).
@return: Node.
"""
    return Node()

def createToolset(filename=None, overwrite=-1):
    """createToolset(filename=None, overwrite=-1) -> None

Creates a tool preset based on the currently selected nodes.

@param filename: Saves the preset as a script with the given file name.
 @param overwrite: If 1 (true) always overwrite; if 0 (false) never overwrite;  otherwise, in GUI mode ask the user, in terminal do same as False. Default  is -1, meaning 'ask the user'."""
    pass

def critical(message):
    """critical(message)-> None

Puts the message into the error console, treating it like an error. Also pops up an alert dialog to the user, immediately.

@param message: String parameter.
@return: None."""
    pass

def debug(message):
    """debug(message)-> None

Puts the message into the error console, treating it like a debug message, which only shows up when the verbosity level is high enough.

@param message: String parameter.
@return: None."""
    pass

def defaultFontPathname():
    """defaultFontPathname() -> str

Get the path to Nukes default font.

@return: Path to the font.
"""
    return ''

def defaultNodeColor(s):
    """defaultNodeColor(s) -> int

Get the default node colour.

@param s: Node class.
@return: The color as a packed integer (0xRRGGBB00)."""
    pass

def delete(n):
    """delete(n) -> None

The named node is deleted. It can be recovered with an undo.

@param n: Node.
@return: None"""
    pass

def deletePreset(nodeClassName, presetName):
    """deletePreset(nodeClassName, presetName) -> None
Deletes a pre-created node preset
@param nodeClassName: Name of the node class to create a preset for.
@param presetName: Name of the preset to create.
@return: bool."""
    pass

def deleteUserPreset(nodeClassName, presetName):
    """deleteUserPreset(nodeClassName, presetName) -> None
Deletes a pre-created user node preset
@param nodeClassName: Name of the node class to create a preset for.
@param presetName: Name of the preset to create.
@return: bool."""
    pass

def deleteView(s):
    """deleteView(s) -> None

Deprecated. Use the Root node.

Deletes a view from the list of views.

@param s: View name.
@return: None"""
    pass

def dependencies(nodes,what):
    """ List all nodes referred to by the nodes argument. 'what' is an optional integer (see below).
  You can use the following constants or'ed together to select the types of dependencies that are looked for:
  	 nuke.EXPRESSIONS = expressions
  	 nuke.INPUTS = visible input pipes
  	 nuke.HIDDEN_INPUTS = hidden input pipes.
  The default is to look for all types of connections.

Example:
  n1 = nuke.nodes.Blur()
  n2 = nuke.nodes.Merge()
  n2.setInput(0, n1)
  deps = nuke.dependencies([n2], nuke.INPUTS | nuke.HIDDEN_INPUTS | nuke.EXPRESSIONS)"""
    pass

def dependentNodes(what,nodes,evaluateAll):
    """ List all nodes referred to by the nodes argument. 'what' is an optional integer (see below).
  You can use the following constants or'ed together to select what types of dependent nodes are looked for:
  	 nuke.EXPRESSIONS = expressions
  	 nuke.INPUTS = visible input pipes
  	 nuke.HIDDEN_INPUTS = hidden input pipes.
  The default is to look for all types of connections.

  evaluateAll is an optional boolean defaulting to True. When this parameter is true, it forces a re-evaluation of the entire tree.
  This can be expensive, but otherwise could give incorrect results if nodes are expression-linked.


Example:
  n1 = nuke.nodes.Blur()
  n2 = nuke.nodes.Merge()
  n2.setInput(0, n1)
  ndeps = nuke.dependentNodes(nuke.INPUTS | nuke.HIDDEN_INPUTS | nuke.EXPRESSIONS, [n1])

  @param what: Or'ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependent nodes. The default is to look for all types of connections.
  @param evaluateAll: Specifies whether a full tree evaluation will take place. Defaults to True.
  @return: List of nodes. """
    return [Node(),]

def display(script, node, title=None, width=None):
    """display(s, node, title, width) -> None.

Creates a window showing the result of a python script. The script is
executed in the context of the given node, so this and a knob
name in expressions refer to that node.

The window will have an 'update' button to run the script again.

@param s: Python script.
@param node: Node.
@param title: Optional title of window.
@param width: Optional width of window.
@return: None.
"""
    pass

def endGroup():
    """endGroup() -> None

Deprecated. Use Group.run, Group.begin/Group.end pairs or (preferably) the with statement.

Changes the current group to the parent of the current group. Does nothing if the current group is a Root (the main window of a script).

@return: None.
"""
    pass

def error(message):
    """error(message)-> None

Puts the message into the error console, treating it like an error.

@param message: String parameter.
@return: None."""
    pass

def execute(nameOrNode, start, end, incr, views, continueOnError = False):
    """execute(nameOrNode, start, end, incr, views, continueOnError = False) -> None.
execute(nameOrNode, frameRangeSet, views, continueOnError = False) -> None.


Execute the named Write node over the specified frames.

There are two variants of this function. The first allows you to specify the frames to write range by giving the start frame number, the end frame number and the frame increment. The second allows you to specify more complicated sets of frames by providing a sequence of FrameRange objects.

If Nuke is run with the GUI up, this will pop up a progress meter. If the user hits the cancel button this command will return 'cancelled' error. If Nuke is run from the nuke command line (ie nuke was started with the -t switch) execute() prints a text percentage as it progresses. If the user types ^C it will aborting the execute() and return a 'cancelled' error.

@param nameOrNode: A node name or a node object.
@param start: Optional start frame. Default is root.first_frame.
@param end: Optional end frame. Default is root.last_frame.
@param incr: Optional increment. Default is 1.
@param views: Optional list of views. Default is None, meaning "all views".
@return: None"""
    pass

def executeBackgroundNuke(exe_path, nodes, frameRange, views, limits, continueOnError = False, flipbookToRun = False, flipbookOptions = {}):
    """executeBackgroundNuke(exe_path, nodes, frameRange, views, limits, continueOnError = False, flipbookToRun = , flipbookOptions = {}) -> None
Run an instance of Nuke as a monitored sub process. Returns an integer that's used as unique id for the started task. If it failed to launch this will be -1.
@param exe_path: Path to Nuke or a script that can take Nuke arguments. You probably want to supply nuke.EXE_PATH.
@param nodes: A list of nodes to execute.
@param frameRanges: List of frame ranges to execute.
@param views: A list of view names to execute.
@param limits: A dictionary with system limits, currently uses keys maxThreads and maxCache.
@param flipbookToRun: The name of the flipbook application to run after the render, or an empty string if not desired.
@param flipbookOptions: A dictionary with options to pass to the flipbook. These should include roi and pixelAspect.
@return: Int."""
    return 0

def executeInMainThread(call,args,kwargs):
    """ Execute the callable 'call' with optional arguments 'args' and named arguments 'kwargs' i
n
      Nuke's main thread and return immediately. """
    pass

def executeInMainThreadWithResult(call,args,kwargs):
    """ Execute the callable 'call' with optional arguments 'args' and named arguments 'kwargs' i
n
      Nuke's main thread and wait for the result to become available. """
    pass

def executeMultiple(nodes, ranges, views, continueOnError=False):
    """executeMultiple(nodes, ranges, views, continueOnError=False) -> None

Execute the current script for a specified frame range. The argument nodes is a sequence of Nuke nodes and ranges is a sequence of range lists. A Nuke range list is a sequence of 3 integers - first, last and incr ( e.g. nuke.execute((w,), ((1,100,1),)) ). The named nodes must all be Write or other executable operators. If no nodes are given then all executable nodes in the current group are executed.
Note that DiskCache and Precomp nodes do not get executed with this call, unless explicitly specified.

If Nuke is run with the GUI up, this will pop up a progress meter. If the user hits the cancel button this command will raise a 'cancelled' error. If Nuke is run in terminal mode (with the -t switch) this prints a text percentage as it progresses.

If the user types ^C it will abort the execute() and raise a 'cancelled' error.

@param nodes: Node list.
@param ranges: Optional start frame. Default is root.first_frame.
@param views: Optional list of views. Default is None. Execute for all.
@return: None"""
    pass

def exists(s):
    """exists(s) -> bool

Check for the existence of a named item.
Function for backwards-compatibility with TCL.

@param s: Name of item.
@return: True if exists, False otherwise."""
    pass

def expandSelectedGroup():
    """expandSelectedGroup() -> None

Moves all nodes from the currently selected group node into its parent group, maintaining node input and output connections, and deletes the group. Returns the nodes that were moved, which will also be selected.

@return: None"""
    pass

def expr(s):
    """expression(s) -> float

Parse a Nuke expression. Runs the same expression parser as is used by animations. This is not the same as the tcl expr parser. The main differences are:
- Only floating point numbers are calculated. There are no strings, boolean, or integer values.
- You can name any knob that returns a floating point value, with a dot-separated name, see knob for details on these names. You may follow
the knob name with a time in parenthesis (like a function call) and if it is animated it will be evaluated at that time. If it is animated and
no time is given, 'frame' is used.
- The words 'frame', 't', and 'x' evaluate to the frame number of the context node, or the frame number this animation is being evaluated at.
- The word 'y' in an animation expression evaluates to the value the animation would have if the control points were used and there was no
expression. Outside an animation expression y returns zero.

@param s: The expression, as a string.
@return: The result.
"""
    return 0.0

def expression(s):
    """expression(s) -> float

Parse a Nuke expression. Runs the same expression parser as is used by animations. This is not the same as the tcl expr parser. The main differences are:
- Only floating point numbers are calculated. There are no strings, boolean, or integer values.
- You can name any knob that returns a floating point value, with a dot-separated name, see knob for details on these names. You may follow
the knob name with a time in parenthesis (like a function call) and if it is animated it will be evaluated at that time. If it is animated and
no time is given, 'frame' is used.
- The words 'frame', 't', and 'x' evaluate to the frame number of the context node, or the frame number this animation is being evaluated at.
- The word 'y' in an animation expression evaluates to the value the animation would have if the control points were used and there was no
expression. Outside an animation expression y returns zero.

@param s: The expression, as a string.
@return: The result.
"""
    return 0.0

def extractSelected():
    """extractSelected() -> None

Disconnects the selected nodes in the group from the tree, and shifts them to the side.

@return: None"""
    pass

def filename():
    """filename(node, i) -> str

Return the filename(s) this node or group is working with.

For a Read or Write operator (or anything else with a filename
knob) this will return the current filename, based on the
root.proxy settings and which of the fullsize/proxy filenames are
filled in. All expansion of commands and variables is
done. However by default it will still have %%04d sequences in it,
use REPLACE to get the actual filename with the current frame number.

If the node is a group, a search is done for executable (i.e. Write)
operators and the value from each of them is returned. This will duplicate
the result of calling execute() on the group.

@param node: Optional node.
@param i: Optional nuke.REPLACE. Will replace %%04d style sequences with the current frame number.
@return: Filename, or None if no filenames are found.
"""
    return ''

def filenameFilter(filename):
    """None"""
    pass

def forceClone():
    """forceClone() -> bool

@return: True if succeeded, False otherwise.
"""
    pass

def forceLoad(n):
    """forceLoad(n) -> None

Force the plugin to be fully instantiated.

@param n: Optional node argument. Default is the current node.
@return: None"""
    pass

def formats():
    """formats() -> list

@return: List of all available formats.
"""
    return [Format(),]

def frame(i):
    """frame(i) -> Current frame.

Return or set the current frame number. Deprecated. Use Root.frame.

Returns the current frame. Normally this is the frame number set in the root node, typically by the user moving the frame slider in a viewer. If a number is given, it sets the current frame number to that number. If the current context is the root this changes the root frame.

@param i: Optional frame number.
@return: Current frame.
"""
    return 0

def fromNode(n):
    """fromNode(n) -> String.

Return the Node n as a string.
This function is most useful when combining Python and TCL scripts for backwards compatibility reasons.

@param n: A Node.
@return: String.
"""
    return ''

def getAllUserPresets():
    """getAllUserPresets() -> None
gets a list of all current user presets
@return: a list of tuples containing all nodename/presetname pairs."""
    pass

def getClipname(prompt, pattern=None, default=None, multiple=False):
    """getClipname(prompt, pattern=None, default=None, multiple=False) -> list of strings or string

Pops up a file chooser dialog box. You can use the pattern to restrict the displayed choices to matching filenames,
normal Unix glob rules are used here. getClipname compresses lists of filenames that only differ by an index number
into a single entry called a 'clip'.

@param prompt: Present the user with this message.
@param pattern: Optional file selection pattern.
@param default: Optional default filename and path.
@param multiple: Optional boolean convertible object to allow for multiple  selection.
@return: If multiple is True, the user input is returned as a list of  strings, otherwise as a single string. If the dialog is cancelled, the  return value is None."""
    return ['',]

def getColor(initial):
    """getColor(initial) -> int

Show a color chooser dialog and return the selected color as an int.

The format of the color values is packed 8bit rgb multiplied by 256 (ie in hex: 0xRRGGBB00).

@param initial: Optional initial color. Integer with components packed as above.
@return: The selected color.
"""
    return 0

def getDeletedPresets():
    """getDeletedPresets() -> None
gets a list of all currently deleted presets
@return: a pyDict containing all nodename/presetname pairs."""
    pass

def getFileNameList(dir, splitSequences = False, extraInformation = False, returnDirs=True, returnHidden=False):
    """getFileNameList( dir, splitSequences = False, extraInformation = False, returnDirs=True, returnHidden=False ) -> str
@param dir the directory to get sequences from
@param splitSequences whether to split sequences or not
@param extraInformation whether or not there should be extra sequence information on the sequence name
@param returnDirs whether to return a list of directories as well as sequences
@param returnHidden whether to return hidden files and directories.
Retrieves the filename list .
@return: Array of files."""
    return ['',]

def getFilename(message, pattern=None, default=None, favorites=None, type=None, multiple=False):
    """getFilename(message, pattern=None, default=None, favorites=None, type=None, multiple=False) -> list of strings or single string

Pops up a file chooser dialog box. You can use the pattern to restrict the displayed choices to matching filenames, normal Unix glob rules are used here.

@param message: Present the user with this message.
@param pattern: Optional file selection pattern.
@param default: Optional default filename and path.
@param favorites: Optional. Restrict favorites to this set. Must be one of  'image', 'script', or 'font'.
@param type: Optional the type of browser, to define task-specific behaviors;  currently only 'save' is recognised.
@param multiple: Optional boolean convertible object to allow for multiple  selection. If this is True, the return value will be a list of strings; if  not, it will be a single string. The default is
@return: If multiple is True, the user input is returned as a list of  strings, otherwise as a single string. If the dialog was cancelled, the  return value will be None.
"""
    return ['',]

def getFramesAndViews(label, default=None, maxviews=0):
    """getFramesAndViews(label, default=None, maxviews=0) -> (ranges, views)

Pops up a dialog with fields for a frame range and view selection.

@param label: User message.
@param default: Optional value for the input field.
@param maxviews: Optional max number of views.
@return: List of ranges and views."""
    return [0, ['',],]

def getInput(prompt, default):
    """getInput(prompt, default) -> str

Pops up a dialog box with a text field for an arbitrary string.

@param prompt: Present the user with this message.
@param default: Default value for the input text field.
@return: String from text field or None if dialog is cancelled."""
    return ''

def getNodeClassName():
    """getNodeClassName() -> None
gets the class name for the currently selected node
@return: a string containing the name."""
    pass

def getNodePresetExcludePaths():
    """getNodePresetExcludePaths() -> string list

Gets a list of all paths that are excluded from the search for node presets.

@return: List of paths."""
    return ['',]

def getPaneFor( panelName ):
    """getPaneFor( panelName ) -> Dock

Returns the first pane that contains the named panel or None if it can't be found.
Note that the panelName must be exact as described in the layout.xml file or the panel ID.
For example, 'Properties.1' or 'Viewer.1 or 'co.uk.thefoundry.WebBrowser'

@return: The pane or None."""
    return Panel()

def getPresetKnobValues():
    """getPresetKnobValues() -> None
gets a list of knob values for a given preset
@param nodeClassName: Name of the node class to get values for.
@param presetName: Name of the preset to get values for.
@return: a pyDict containing all knob name/value pairs."""
    pass

def getPresets():
    """getPresets() -> None
gets a list of all presets for the currently selected node's class
@return: a pyList containing all nodename/presetname pairs."""
    pass

def getPresetsMenu(Node):
    """getPresetsMenu(Node) -> Menu or None
Gets the presets menu for the currently selected node.
@return: The menu, or None if it doesn't exist.
"""
    return Menu()

def getReadFileKnob(node):
    """getReadFileKnob(node) -> knob

rief Gets the read knob for a node (if it exists).

@param node: The node to get the knob for.

@return: A PyObject containing the read knob if it exists, NULL otherwise"""
    return Knob()

def getToolsetExcludePaths():
    """getToolsetExcludePaths() -> string list

Gets a list of all paths that are excluded from the search for node presets.

@return: List of paths."""
    return ['',]

def getUserPresetKnobValues():
    """getUserPresetKnobValues() -> None
gets a list of knob values for a given preset
@param nodeClassName: Name of the node class to get values for.
@param presetName: Name of the preset to get values for.
@return: a pyDict containing all knob name/value pairs."""
    pass

def getUserPresets(Node):
    """getUserPresets(Node) -> None
gets a list of all user presets for the currently selected node's class
@return: a pyList containing all nodename/presetname pairs."""
    pass

def hotkeys():
    """hotkeys() -> str

Returns the Nuke key assignments as a string formatted for use in nuke.display().

@return: A formatted string."""
    return ''

def import_module(name,filterRule):
    """None"""
    pass

def inputs(node, i):
    """inputs(n, i) -> int

Deprecated. Use Node.inputs.

Get how many inputs the node has. Normally this is a constant but some nodes have a variable number, the user can keep connecting them and the count will increase.
Attempting to set the number will just disconnect all inputs greater or equal to number. For a variable input node this may decrease
inputs to the new value. For most nodes this will have no effect on the value of inputs.

@param n: Node.
@param i: Optional number of inputs requested.
@return: Number of inputs."""
    return 0

def invertSelection():
    """invertSelection() -> None

Selects all unselected nodes, and deselects all selected ones.

@return: None.
"""
    pass

def knob(name, value, getType, getClass):
    """knob(name, value, getType, getClass) -> None

rief Returns or sets the entire state of a knob.

Each individual control on a control panel is called a 'knob'. A
knob's name is a dot-separated list. An example of a fully-expanded
name of a knob is 'root.Group1.Blur1.size.w'. 'root' is the node
name of the outermost group, 'Group1' is a group inside that
containing the blur operator, 'Blur1' is the name of a blur
operator, 'size' is the name of the actual knob, and 'w' is the
name of the 'field' (there are two fields in a blur size, 'w' and
'h').

You can omit a lot of this because all knob names are figured out
relative to a 'current knob' and 'current node'. These are set
depending on the context of where the scripting is invoked. For
menu items the current node is the group that contained the menu,
and there is no current knob. For expressions typed into knob
fields the current knob is that knob and the current node is the
node the knob belongs to.

If a name does not start with 'root' then a search upwards is done
for the first word in the name, first against the fields in the
current knob, then against the knobs in the current node, then
against the nodes in the group containing the current node (or in
it if it is a group), on up to the root.

The word 'this' means the current knob or the current node.

The word 'input' means the first (0 or B) input of a node. Ie
'Blur1.input' returns the node connected to the input of Blur1,
while 'Blur1.input.input' returns the input of that node.

If you are getting the value for reporting to the user, you probably
want to use the value or expression commands.

If the getType argument is specified and is True, it will print out the type of the
knob rather than getting or setting the value. The type is an integer,
using the same list as addUserKnob.

If the getClass argument is specified and is True, it will print out the type of the knob as a string, e.g. 'Int_Knob',
'Enumeration_Knob', 'XY_Knob'.

If both the getType and getClass arguments are present and are True, getType takes precedence.
@param name: The name of the knob.
@param value: Optional argument. If this is present, the value will be stored into the knob.
@param getType: Optional boolean argument. If True, return the class ID for the knob instead of the knob itself. The class ID is an int.
@param getClass: Optional boolean argument. If True, return the class name for the knob instead of the knob itself. The class name is a string.
"""
    pass

def knobChanged():
    """None"""
    pass

def knobDefault(classknob, value):
    """knobDefault(classknob, value) -> str

Set a default value for knobs in nodes that belong to the
same class. All knobs with matching names, that are created after this
command was issued, will default to the new value. If class. is missing
or is "*." then this default applies to all nodes with such a knob.
If several values are supplied, the first value which is valid will be
used as the default.
knobDefault can be used to specify file format specific knobs.
These are knobs that are added to Read, Write and other file format
dependent nodes when the file name changes. To specify defaults, use
the class name, followed by the file format extension, followed by the knob name,
all separated by periods. An example is shown below.

Example:
nuke.knobDefault("Blur.size", "20")

Example:
nuke.knobDefault("Read.exr.compression", "2")

@param classknob: String in the form "class.knob" where "class" is the class of Node, i.e. Blur, and "knob" is the name of the knob. This can also include a file extension, as in "class.extension.knob"
@param value: Optional string to convert to the default value.
@return: None or String with the default value."""
    return ''

def knobTooltip(classknob, value):
    """knobTooltip(classknob, value) -> None

Set an override for a tooltip on a knob.

Example:

   nuke.knobTooltip('Blur.size', '[some text]')

@param classknob: String in the form "class.knob" where "class" is the class of Node, i.e. Blur, and "knob" is the name of the knob.
@param value: String to use as the tooltip
@return: None"""
    pass

def layers(node=None):
    """layers(node=None) -> string list.

Lists the layers in a node. If no node is provided this will list all known layer names in this script.

@param node: Optional node parameter.
@return: A list of layer names."""
    return ['',]

def load(s):
    """load(s) -> None

Load a plugin. You can force a certain plugin to load with this function. If the plugin has already been loaded nothing happens.
If there is no slash in the name then the pluginPath() is searched for it. If there is a slash then the name is used directly as a
filename, if it does not start with a slash the name is relative to the directory containing any plugin being currently loaded.
If no filename extension is provided, it will try appending '.so' (or whatever your OS dynamic library extension is) and finding
nothing will also try to append '.tcl' and '.py'.

@param s: Plugin name or filename.
@return: None
@raise RuntimeError: if the plugin couldn't be loaded for any reason.
"""
    pass

def loadToolset(filename=None, overwrite=-1):
    """loadToolset(filename=None, overwrite=-1) -> None

Loads the tool preset with the given file name.

@param filename: name of preset script file to load
 """
    pass

def localisationEnabled(knob):
    """localisationEnabled(knob) -> bool

rief Checks if localisation is enabled on a given Read_File_Knob.

@param knob: The Read_File_Knob to check.

@return: true if enabled, false otherwise"""
    return True

def localiseFiles(readKnobs):
    """localiseFiles(readKnobs) -> None
creates localisations of all files pointed to by the given read knobs
@param readKnobs: List of read knobs.
@return: None."""
    pass

def makeGroup(show=True):
    """makeGroup(show=True) -> Group

Creates a new group containing copies of all the currently selected nodes. Note that this creates duplicates of the selected nodes, rather than moving them.

@param show: If show is True, the node graph for the new group is shown.
@return: The new Group node."""
    return Group()

def memory(cmd, value):
    """memory(cmd, value) -> str or int
Get or set information about memory usage.

The value parameter is optional and is only used by some of the commands (see below).

The cmd parameter specifies what memory information to retrieve. It can be one of the following values:
- info [node-name]         Return a string describing current memory usage. Can optionally provide it for a specific node.
- free [size]              Free as much memory as possible. If a size is specified, if will stop trying to free memory when usage drops below the size.
- usage                    Return the amount of memory currently in use.
- max_usage [size]         If no size is specified, returns the maximum amount of memory used so far. If a size is given, then set this size as the memory limit.
- total_ram                Return the total amount of RAM.
- total_vm                 Return the total virtual memory.
- free_count [num]         Get or set the free count.
- new_handler_count [num]  Get or set the new handler count.
"""
    return 0

def menu(name):
    """menu(name) -> Menu

Find and return the Menu object with the given name. Current valid menus are:

'Nuke'          the application menu
'Pane'          the UI Panes & Panels menu
'Nodes'         the Nodes toolbar (and Nodegraph right mouse menu)
'Properties'    the Properties panel right mouse menu
'Animation'     the knob Animation menu and Curve Editor right mouse menu
'Viewer'        the Viewer right mouse menu
'Node Graph'    the Node Graph right mouse menu
'Axis'          functions which appear in menus on all Axis_Knobs.

@param name: The name of the menu to get. Must be one of the values above.
@return: The menu.
@raise RuntimeError: if Nuke isn't in GUI mode."""
    return Menu()

def message(prompt):
    """message(prompt) -> None

Show an info dialog box. Pops up an info box (with a 'i' and the text message) and waits for the user to hit the OK button.

@param prompt: Present user with this message.
@return: None"""
    pass

def modified(status):
    """modified(status) -> True if modified, False otherwise.

Deprecated. Use Root.modified and Root.setModified.

Get or set the 'modified' flag in a script. Setting the value will turn the indicator in the title bar on/off and will start or stop the autosave timeout.

@param status: Optional boolean value. If this is present the status will be set to this value; otherwise it will be retrieved instead.
@return: True if modified, False otherwise.
"""
    pass

def nodeCopy(s):
    """nodeCopy(s) -> bool

Copy all selected nodes into a file or the clipboard.

@param s: The name of a clipboad to copy into. If s is the string '%clipboard%' this will copy into the operating systems clipboard.
@return: True if any nodes were selected, False otherwise.
"""
    pass

def nodeDelete(s):
    """nodeDelete(s) -> True if any nodes were deleted, False otherwise.

Removes all selected nodes from the DAG.

@return: True if any nodes were deleted, False otherwise.
"""
    pass

def nodePaste(s):
    """nodePaste(s) -> Node

Paste nodes from a script file or the clipboard.
This function executes the script stored in a file. It is assumed the script is the result of
a nodeCopy command. The 's' argument can be '%clipboard%' to paste the operating system's clipboard contents.

@param s: The 's' argument can be '%clipboard%' to paste the operating system's clipboard contents.
@return: Node"""
    return Node()

def nodesSelected():
    """nodesSelected() -> None

returns true if any nodes are currently selected
"""
    pass

def numvalue(knob, default=0):
    """numvalue(knob, default=infinity) -> float

The numvalue function returns the current value of a knob.

This is the same as the value() command except it will always return a number. For enumerations this returns the index into the menu, starting at zero. For checkmarks this returns 0 for false and 1 for true.
@param knob: A knob.
@param default: Optional default value to return if the knob's value cannot  be converted to a number.
@return: A numeric value for the knob, or the default value (if any)."""
    return 0.0

def oculaPresent():
    """oculaPresent() -> bool

Check whether Ocula is present.

@return: True if Ocula is present, False if not."""
    pass

def ofxAddPluginAliasExclusion(fullOfxEffectName):
    """ofxAddPluginAliasExclusion(fullOfxEffectName) -> None
Adds the ofx effect name to a list of exclusions that will not get tcl aliases automatically created for them.
For example, if there is an ofx plugin with a fully qualified name of: 'OFXuk.co.thefoundry.noisetools.denoise_v100'.
Nuke by default would automatically alias that so that nuke.createNode('Denoise') will create that node type.
By calling nuke.ofxAddPluginAliasExclusion('OFXuk.co.thefoundry.noisetools.denoise_v100'), you'd be changing
that such that the only way to create a node of that type would be to call nuke.createNode('OFXuk.co.thefoundry.noisetools.denoise_v100')
This does not change saving or loading of Nuke scripts with that plugin used in any way.
@param fullOfxEffectName: The fully qualified name of the ofx plugin to add to the exclusion list.
@return: None.
"""
    pass

def ofxMenu():
    """ofxMenu() -> bool

Find all the OFX plugins (by searching all the directories below $OFX_PLUGIN_PATH,
or by reading a cache file stored in $NUKE_TEMP_DIR), then add a menu item for each
of them to the main menu.

@return: True if succeeded, False otherwise.
"""
    pass

def ofxPluginPath():
    """nuke.ofxPluginPath() -> String list

List of all the directories Nuke searched for OFX plugins in.

@return: String list"""
    return ['',]

def ofxRemovePluginAliasExclusion(fullOfxEffectName):
    """ofxRemovePluginAliasExclusion(fullOfxEffectName) -> None
Remove an ofx plugin alias exclusion that was previously added with .
Example: nuke.ofxRemovePluginAliasExclusion('OFXuk.co.thefoundry.noisetools.denoise_v100')
@param fullOfxEffectName: The fully qualified name of the ofx plugin to remove from the exclusion list.
@return: None.
"""
    pass

def onCreate():
    """None"""
    pass

def onDestroy():
    """None"""
    pass

def onScriptClose():
    """None"""
    pass

def onScriptLoad():
    """None"""
    pass

def onScriptSave():
    """None"""
    pass

def onUserCreate():
    """None"""
    pass

def output_redirector():
    """Internal to Nuke. Not for public use."""
    pass

def pan():
    """pan() -> array with x, then y

Return the pan values of a group's display. Like so:
n = nuke.pan()
print n[0]
print n[1]

@return: Array of x, y.
"""
    return [0,0]

def pluginAddPath(args,addToSysPath=False):
    """ Adds all the paths to the beginning of the Nuke plugin path.
      If the path already exists in the list of plugin paths, it is moved
      to the start. If this command is executed inside an init.py then
      the init.py in the path will be executed.
      It also adds the paths to the sys.path, if addToSysPath is True."""
    pass

def pluginAppendPath(args,addToSysPath):
    """ Add a filepath to the end of the Nuke plugin path.  If the path
      already exists in the list of plugin paths, it will remain at its
      current position.
      It also appends the paths to the sys.path, if addToSysPath is True."""
    pass

def pluginExists(name):
    """pluginExists(name) -> True if found, or False if not.

This function is the same as load(), but only checks for the existence of a plugin rather than loading it.
If there is no slash in the name then the pluginPath() is searched for it. If there is a slash then the name is used directly as a
filename, if it does not start with a slash the name is relative to the directory containing any plugin being currently loaded.
If no filename extension is provided, it will try appending '.so' (or whatever your OS dynamic library extension is) and finding
nothing will also try to append '.tcl' and '.py'.

@param name: Plugin name or filename.
@return: True if found, or False if not.
"""
    pass

def pluginInstallLocation():
    """pluginInstallLocation() -> string list

The system-specific locations that Nuke will look in for third-party plugins.

@return: List of paths."""
    return ['',]

def pluginPath():
    """pluginPath() -> string list

List all the directories Nuke will search in for plugins.

The built-in default is ~/.nuke and the 'plugins' directory from the same location the NUKE executable file is in. Setting the environment variable $NUKE_PATH to a colon-separated list of directories will replace the ~/.nuke with your own set of directories, but the plugins directory is always on the end.

@return: List of paths."""
    return ['',]

def plugins(switches=0, *pattern):
    """plugins(switches=0, *pattern)-> list of str

Returns a list of every loaded plugin or every plugin available. By default each plugin is returned as the full pathname of the plugin file.

You can give a glob-style matching pattern and only the plugins whose filenames (not path) match the pattern will be returned. You can give more than one glob pattern if desired.

You can also put options before the glob patterns. Currently supported:

  ALL    Return all plugins in each of the plugin_path() directories,
         rather than only the currently loaded plugins.

  NODIR  Just put the filenames in the list, not the full path. There
         may be duplicates.

If you don't specify any switches, the default behaviour is to return a list
with the full paths of all loaded plugins.

@param switches: Optional parameter. Bitwise OR of nuke.ALL, nuke.NODIR.
@param pattern: Zero or more glob patterns.
@return: List of plugins."""
    return ['',]

def recentFile(index):
    """recentFile(index) -> str

Returns a filename from the recent-files list.

@param index: A position in the recent files list. This must be a non-negative number.
@return: A file path.
@raise ValueError: if the index is negative.
@raise RuntimeError: if there is no entry in the recent files list for the specified index."""
    return ''

def redo():
    """redo() -> None

Perform the most recent redo.

@return: None"""
    pass

def removeAfterBackgroundFrameRender(call,args,kwargs):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeAfterBackgroundRender(call,args,kwargs):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeAfterFrameRender(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeAfterRender(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeAutoSaveDeleteFilter(filter):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeAutoSaveFilter(filter):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeAutoSaveRestoreFilter(filter):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeAutolabel(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeBeforeBackgroundRender(call,args,kwargs):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeBeforeFrameRender(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeBeforeRender(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeFavoriteDir(name, type):
    """removeFavoriteDir(name, type) -> None.

Remove a directory path from the favorites list.

@param name: Favourite path entry ('Home', 'Desktop', etc.).
@param type: Optional bitwise OR combination of nuke.IMAGE, nuke.SCRIPT, nuke.FONT or nuke.GEO.
@return: None"""
    pass

def removeFilenameFilter(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeFilenameValidate(call,args,kwargs,nodeClass):
    """Remove a previously-added callback."""
    pass

def removeKnobChanged(call,args,kwargs,nodeClass,node):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeOnCreate(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeOnDestroy(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeOnScriptClose(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeOnScriptLoad(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeOnScriptSave(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeOnUserCreate(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def removeUpdateUI(call,args,kwargs,nodeClass):
    """Remove a previously-added callback with the same arguments."""
    pass

def render(nameOrNode, start, end, incr, views, continueOnError = False):
    """execute(nameOrNode, start, end, incr, views, continueOnError = False) -> None.
execute(nameOrNode, frameRangeSet, views, continueOnError = False) -> None.


Execute the named Write node over the specified frames.

There are two variants of this function. The first allows you to specify the frames to write range by giving the start frame number, the end frame number and the frame increment. The second allows you to specify more complicated sets of frames by providing a sequence of FrameRange objects.

If Nuke is run with the GUI up, this will pop up a progress meter. If the user hits the cancel button this command will return 'cancelled' error. If Nuke is run from the nuke command line (ie nuke was started with the -t switch) execute() prints a text percentage as it progresses. If the user types ^C it will aborting the execute() and return a 'cancelled' error.

@param nameOrNode: A node name or a node object.
@param start: Optional start frame. Default is root.first_frame.
@param end: Optional end frame. Default is root.last_frame.
@param incr: Optional increment. Default is 1.
@param views: Optional list of views. Default is None, meaning "all views".
@return: None"""
    pass

def restoreWindowLayout(i):
    """restoreWindowLayout(i) -> None.
Restores a saved window layout.
@param i: Layout number
@return: None"""
    pass

def root():
    """root() -> node

Get the DAG's root node. Always succeeds.

@return: The root node. This will never be None."""
    return Root()


def runIn(object, cmd):
    """runIn(object, cmd) -> bool

Execute commands with a given node/knob/field as the 'context'.
This means that all names are evaluated relative to this object, and commands that modify 'this' node will modify the given one.

@param object: Name of object.
@param cmd: Command to run.
@return: True if succeeded, False otherwise.
"""
    pass

def sample(node, chan, x, y, dx, dy):
    """sample(n, c, x, y, dx, dy) -> float.

Get pixel values from an image. Deprecated, use Node.sample instead.

This requires the image to be calculated, so performance may be very bad if this is placed into an expression in a control panel. Produces a cubic filtered result. Any sizes less than 1, including 0, produce the same filtered result, this is correct based on sampling theory. Note that integers are at the corners of pixels, to center on a pixel add .5 to both coordinates. If the optional dx,dy are not given then the exact value of the square pixel that x,y lands in is returned. This is also called 'impulse filtering'.

@param n: Node.
@param c: Channel name.
@param x: Centre of the area to sample (X coordinate).
@param y: Centre of the area to sample (Y coordinate).
@param dx: Optional size of the area to sample (X coordinate).
@param dy: Optional size of the area to sample (Y coordinate).
@return: Floating point value.
"""
    return 0.0

def saveUserPreset(node, presetName):
    """saveUserPreset(node, presetName) -> None
Saves a node's current knob values as a user preset.
@param presetName: Name of the preset to create.
@return: bool."""
    pass

def saveWindowLayout(i=-1):
    """saveWindowLayout(i=-1) -> None

Saves the current window layout.

@param i: Optional layout index. If this is omitted or set to a negative value, save as the default layout.
@return: None.
"""
    pass

def scriptClear():
    """Clears a Nuke script."""
    pass

def scriptClose():
    """Close the current script or group. Returns True if successful."""
    pass

def scriptExit():
    """Exit Nuke."""
    pass

def scriptNew():
    """Start a new script. Returns True if successful."""
    pass

def scriptOpen():
    """Opens a new script containing the contents of the named file."""
    pass

def scriptReadFile():
    """Read nodes from a file."""
    pass

def scriptReadText():
    """Read nodes from a string."""
    pass

def scriptSave(filename=None):
    """scriptSave(filename=None) -> bool

Saves the current script to the current file name. If there is no current file name and Nuke is running in GUI mode, the user is asked for a name using the file chooser.

@param filename: Save to this file name without changing the script name in the project (use scriptSaveAs() if you want it to change).
@return: True if the file was saved, otherwise an exception is thrown."""
    pass

def scriptSaveAs(filename=None, overwrite=-1):
    """scriptSaveAs(filename=None, overwrite=-1) -> None

Saves the current script with the given file name if supplied, or (in GUI mode) asks the user for one using the file chooser. If Nuke is not running in GUI mode, you must supply a filename.

@param filename: Saves the current script with the given file name if  supplied, or (in GUI mode) asks the user for one using the file chooser.
@param overwrite: If 1 (true) always overwrite; if 0 (false) never overwrite;  otherwise, in GUI mode ask the user, in terminal do same as False. Default  is -1, meaning 'ask the user'."""
    pass

def scriptSource():
    """Same as scriptReadFile()."""
    pass
def scriptSaveAndClear():
    """Calls nuke.scriptSave and nuke.scriptClear

Parameters:

        filename - Save to this file name without changing the script name in the project.
        ignoreUnsavedChanges - Optional. If set to True scripSave will be called, ignoring any unsaved changes

Returns: None
    True when sucessful. False if the user cancels the operation. In this case nuke.scripClear will not be called """
    pass

def script_directory():
    """None"""
    pass

def selectAll():
    """selectAll() -> None

Select all nodes in the DAG.

@return: None"""
    pass

def selectConnectedNodes():
    """ Selects all nodes in the tree of the selected node. """
    pass

def selectPattern():
    """selectPattern() -> None

Selects nodes according to a regular expression matching pattern, entered through an input dialog. The pattern can include wildcards ('?' and '*') as well as regular expressions. The expressions are checked against the node name, label, class, and associated file names.

@return: None"""
    pass

def selectSimilar(matchType=None):
    """selectSimilar(matchType) -> None

Selects nodes that match a node in the current selection based on matchType criteria.

@param matchType: One of nuke.MATCH_CLASS, nuke.MATCH_LABEL, nuke.MATCH_COLOR.
@return: None.
"""
    pass

def selectedNode():
    """selectedNode() -> Node.

Returns the 'node the user is thinking about'.
If several nodes are selected, this returns one of them. The one returned will be an 'output' node in that no other selected nodes
use that node as an input. If no nodes are selected, then if the last thing typed was a hotkey this returns the node the cursor is pointing at.
If none, or the last event was not a hotkey, this produces a 'No node selected' error.

@return: Node.
"""
    return Node()

def selectedNodes(filter=None):
    """selectedNodes(filter) -> List.

Returns a list of all selected nodes in the current group. An attempt is made to return them in 'useful' order where inputs are done before the final node, so commands applied to this list go from top-down.

@param filter: Optional class of Node. Instructs the algorithm to apply only to a specific class of nodes.
@return: The list of selected nodes.
"""
    return [Node(),]

def setPreset(nodeClassName, presetName, knobValues):
    """setPreset(nodeClassName, presetName, knobValues) -> None
Create a node preset for the given node using the supplied knob values
@param nodeClassName: Name of the node class to create a preset for.
@param presetName: Name of the preset to create.
@param knobValues: A dictionary containing a set of knob names and preset values.
@return: bool."""
    pass

def setUserPreset(nodeClassName, presetName, knobValues):
    """setUserPreset(nodeClassName, presetName, knobValues) -> None
Create a node preset for the given node using the supplied knob values
@param nodeClassName: Name of the node class to create a preset for.
@param presetName: Name of the preset to create.
@param knobValues: A dictionary containing a set of knob names and preset values.
@return: bool."""
    pass

def show(node=None, forceFloat=None):
    """show(n, forceFloat) -> None

Opens a window for each named node, as though the user double-clicked on them.  For normal operators this opens the
control panel, for viewers it opens the viewer, for groups it opens the control panel.

@param n: Optional node argument. Default is the current node.
@param forceFloat: Optional python object. If it evaluates to True it will open the window as a floating panel. Default is False.
@return: None"""
    pass

def showDag(group):
    """showDag(n) -> None
Show the tree view of a group node or opens a node control panel.

@param n: Group.
@return: None"""
    pass

def showInfo(node):
    """showInfo(n) -> str

Returns a long string of debugging information about each node and
the operators it is currently managing. You should not rely on its
contents or format being the same in different versions of Nuke.

@param n: Optional node argument.
@return: String.
"""
    return ''

def showSettings():
    """showSettings() -> None

Show the settings of the current group.

@return: None"""
    pass

def splayNodes():
    """splayNodes() -> None

Deprecated. Use Group.splaySelectedNodes.

@return: None"""
    pass

def stderr_redirector():
    """Internal to Nuke. Not for public use."""
    pass

def tabClose():
    """Close the active dock tab. Returns True if successful."""
    pass

def tabNext():
    """Make the next tab in this dock active. Returns True if successful."""
    pass

def tcl(s, *args):
    """tcl(s, *args) -> str.

Run a tcl command. The arguments must be strings and passed to the command. If no arguments are given and the command has whitespace in it then it is instead interpreted as a tcl program (this is deprecated).

@param s: TCL code.
@param args: The arguments to pass in to the TCL code.
@return: Result of TCL command as string.
"""
    return ''

def thisClass():
    """thisClass() -> None

Get the class name of the current node. This equivalent to calling nuke.thisNode().Class(), only faster.

@return: The class name for the current node."""
    pass

def thisGroup():
    """thisGroup() -> Group

Returns the current context Group node.

@return: The group node."""
    return Group()

def thisKnob():
    """thisKnob() -> Knob

Returns the current context knob if any.

@return: Knob or None"""
    return Knob()

def thisNode():
    """thisNode() -> Node.

Return the current context node.

@return: The node.
"""
    return Node()

def thisPane():
    """thisPane() -> the active pane.

Returns the active pane. This is only valid during a pane menu callback or window layout restoration.

@return: The active pane."""
    return Panel()

def thisParent():
    """thisParent() -> Node

Returns the current context Node parent.

@return: A node.
"""
    return Node()

def thisView():
    """thisView() -> str
Get the name of the current view.
@return: The current view name as a string."""
    return ''

def toNode(s):
    """toNode(s) -> Node

Search for a node in the DAG by name and return it as a Python object.

@param s: Node name.
@return: Node or None if it does not exist."""
    return Node()

def toggleFullscreen():
    """toggleFullscreen() -> None

Toggles between windowed and fullscreen mode.

@return: None"""
    pass

def toggleViewers():
    """toggleViewers() -> None

Toggles all the viewers on and off.

@return: None"""
    pass

def toolbar(name, create=True):
    """toolbar(name, create=True)-> ToolBar

Find and return the ToolBar object with the given name. The name of the built-in nodes toolbar is 'Nodes'.

A RuntimeException is thrown if not in GUI mode.

@param name: The name of the toolbar to find or create.
@param create: Optional parameter. True (the default value) will mean that a new  toolbar gets created if one with the given name couldn't be found; False will  mean that no new toolbar will be created.@return: The toolbar, or None if no toolbar was found and 'create' was False."""
    return ToolBar()

def tprint(text, sep=' ', end='\n', file=None):
    """tprint(value, ..., sep=' ', end='\n', file=sys.stdout) -> None

Prints the values to a stream, or to stdout by default.

@param value: A python object
@param file: a file-like object (stream); defaults to stdout.
@param sep: string inserted between values, default a space.
@param end: string appended after the last value, default a newline.
@return: None
"""
    pass

def undo():
    """undo() -> None

Perform the most recent undo.

@return: None
"""
    pass

def updateUI():
    """None"""
    pass

def validateFilename(filename):
    """None"""
    pass

def value(knob, default):
    """value(knob, default) -> string.

The value function returns the current value of a knob. The knob argument is a string referring to a knob and default is an optional default value to be returned in case of an error. Unlike knob(), this will evaluate animation at the current frame, and expand brackets and dollar signs in string knobs."""
    return ''

def views():
    """views() -> List.

List of all the globally existing views.

@return: List"""
    return (View(),)

def waitForThreadsToFinish():
    """waitForThreadsToFinish() -> str
Returns true if Nuke should wait for any Python threads to finish before exitting.
@return: True or False."""
    return ''

def warning(message):
    """warning(message)-> None

Puts the message into the error console, treating it like a warning.

@param message: String parameter.
@return: None."""
    pass

def zoom(scale, center, group):
    """zoom(scale, center, group) -> float

Change the zoom and pan of a group's display. The scale argument is the new zoom factor.
If the scale is given, but not the center, the zoom is set to that factor and the view is
positioned so the cursor is pointing at the same place it was before zooming. A zero or negative
scale value will cause a zoom-to-fit.

If both scale and center arguments are given, the view is zoomed and then centered on the
specified point.

The new scale factor will be returned, or None if the function is run in a non-GUI context.

@param scale: New zoom factor.
@param center: Optional 2-item tuple specifying the center coordinates.
@param group: Optional Group. This is ignored at present.
@return: Current zoom factor or None if not in a GUI context.
"""
    return 0.0

def zoomToFitSelected():
    """
    Does a zoom to fit on the selected nodes in the DAG
    :return: None
    """

def center():
    """
    center() -> array with x, then y

    Return the center values of a group's display, these values are suitable to be passed to nuke.zoom as the DAG center point.  Like so:
    center = nuke.center()
    zoom = nuke.zoom()
    print center[0]
    print center[1]
    ## move DAG back to center point without changing zoom.
    nuke.zoom( zoom, center )
    @return: Array of x, y.
    """
    return [0,0]

def openPanels():
    """
    returns a list of Nodes which have panels open.The last item in the list is the currently active Node panel.
    """
    return ['',]

