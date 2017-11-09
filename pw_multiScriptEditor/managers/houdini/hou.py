from PySide2.QtWidgets import *

class appearanceChangeType:

    Any = EnumValue
    ErrorState = EnumValue
    Pick = EnumValue
    Color = EnumValue
    DeleteScript = EnumValue
    CommentLockFlag = EnumValue
    CompressFlag = EnumValue
    OTLMatchState = EnumValue
    ActiveInput = EnumValue
    Connections = EnumValue
    ExpressionLanguage = EnumValue
    NetworkBox = EnumValue
    PostIt = EnumValue


class attribData:

    Int = EnumValue
    Float = EnumValue
    String = EnumValue


class attribType:

    Point = EnumValue
    Prim = EnumValue
    Vertex = EnumValue
    Global = EnumValue


class colorItemType:

    NetworkBox = EnumValue
    StickyNote = EnumValue
    StickyNoteText = EnumValue


class colorType:

    RGB = EnumValue
    HSV = EnumValue
    HSL = EnumValue
    LAB = EnumValue
    XYZ = EnumValue


class componentLoopType:

    Partial = EnumValue
    Extended = EnumValue
    Closed = EnumValue


class compressionType:

    Gzip = EnumValue
    Blosc = EnumValue
    NoCompression = EnumValue


class confirmType:

    OverwriteFile = EnumValue
    UnlockNode = EnumValue
    DeleteSpareParameters = EnumValue
    DeleteWithoutReferences = EnumValue
    NestedChannelGroups = EnumValue
    SiblingChannelGroups = EnumValue
    DeleteShelfElement = EnumValue
    DeleteGalleryEntry = EnumValue
    InactiveSnapMode = EnumValue
    BackgroundSave = EnumValue


class connectivityType:

    NoConnectivity = EnumValue
    Texture = EnumValue
    Position = EnumValue


class dataParmType:

    Geometry = EnumValue
    KeyValueDictionary = EnumValue


class exprLanguage:

    Python = EnumValue
    Hscript = EnumValue


class fieldType:

    NoSuchField = EnumValue
    Integer = EnumValue
    Boolean = EnumValue
    Float = EnumValue
    String = EnumValue
    Vector2 = EnumValue
    Vector3 = EnumValue
    Vector4 = EnumValue
    Quaternion = EnumValue
    Matrix3 = EnumValue
    Matrix4 = EnumValue
    UV = EnumValue
    UVW = EnumValue
    IntArray = EnumValue
    FloatArray = EnumValue


class fileChooserMode:

    Read = EnumValue
    Write = EnumValue
    ReadAndWrite = EnumValue


class fileType:

    Any = EnumValue
    Image = EnumValue
    Geometry = EnumValue
    Ramp = EnumValue
    Capture = EnumValue
    Clip = EnumValue
    Lut = EnumValue
    Cmd = EnumValue
    Midi = EnumValue
    I3d = EnumValue
    Chan = EnumValue
    Sim = EnumValue
    SimData = EnumValue
    Hip = EnumValue
    Otl = EnumValue
    Dae = EnumValue
    Gallery = EnumValue
    Directory = EnumValue


class flipbookAntialias:

    UseViewportSetting = EnumValue
    Off = EnumValue
    Fast = EnumValue
    Good = EnumValue
    HighQuality = EnumValue


class flipbookMotionBlurBias:

    Centered = EnumValue
    Forward = EnumValue
    Previous = EnumValue


class folderType:

    Collapsible = EnumValue
    Simple = EnumValue
    Tabs = EnumValue
    RadioButtons = EnumValue
    MultiparmBlock = EnumValue
    ScrollingMultiparmBlock = EnumValue
    TabbedMultiparmBlock = EnumValue
    ImportBlock = EnumValue


class geometryType:

    Points = EnumValue
    Vertices = EnumValue
    Edges = EnumValue
    Breakpoints = EnumValue
    Primitives = EnumValue


class geometryViewportLayout:

    DoubleSide = EnumValue
    DoubleStack = EnumValue
    Quad = EnumValue
    QuadBottomSplit = EnumValue
    QuadLeftSplit = EnumValue
    Single = EnumValue
    TripleBottomSplit = EnumValue
    TripleLeftSplit = EnumValue


class geometryViewportType:

    Perspective = EnumValue
    Top = EnumValue
    Bottom = EnumValue
    Front = EnumValue
    Back = EnumValue
    Right = EnumValue
    Left = EnumValue
    UV = EnumValue


class groupListType:

    Points = EnumValue
    Vertices = EnumValue
    Edges = EnumValue
    Breakpoints = EnumValue
    Primitives = EnumValue
    MatchPickType = EnumValue


class hdaEventType:

    AssetCreated = EnumValue
    AssetDeleted = EnumValue
    AssetSaved = EnumValue
    LibraryInstalled = EnumValue
    LibraryUninstalled = EnumValue


class hdaLicenseType:

    Execute = EnumValue
    Read = EnumValue
    Full = EnumValue


class hipFileEventType:

    BeforeClear = EnumValue
    AfterClear = EnumValue
    BeforeLoad = EnumValue
    AfterLoad = EnumValue
    BeforeMerge = EnumValue
    AfterMerge = EnumValue
    BeforeSave = EnumValue
    AfterSave = EnumValue


class imageDepth:

    Int8 = EnumValue
    Int16 = EnumValue
    Int32 = EnumValue
    Float16 = EnumValue
    Float32 = EnumValue


class licenseCategoryType:

    Commercial = EnumValue
    Education = EnumValue
    ApprenticeHD = EnumValue
    Apprentice = EnumValue


class menuType:

    Normal = EnumValue
    Mini = EnumValue
    StringReplace = EnumValue
    StringToggle = EnumValue


class networkItemType:

    Connection = EnumValue
    NetworkBox = EnumValue
    NetworkDot = EnumValue
    Node = EnumValue
    StickyNote = EnumValue
    SubnetIndirectInput = EnumValue


class nodeEventType:

    BeingDeleted = EnumValue
    NameChanged = EnumValue
    FlagChanged = EnumValue
    AppearanceChanged = EnumValue
    PositionChanged = EnumValue
    InputRewired = EnumValue
    ParmTupleChanged = EnumValue
    ChildCreated = EnumValue
    ChildDeleted = EnumValue
    ChildSwitched = EnumValue
    ChildSelectionChanged = EnumValue
    SpareParmTemplatesChanged = EnumValue


class nodeFlag:

    Audio = EnumValue
    Bypass = EnumValue
    ColorDefault = EnumValue
    Compress = EnumValue
    Current = EnumValue
    Debug = EnumValue
    Display = EnumValue
    DisplayComment = EnumValue
    DisplayDescriptiveName = EnumValue
    Export = EnumValue
    Expose = EnumValue
    Footprint = EnumValue
    Highlight = EnumValue
    InOutDetailLow = EnumValue
    InOutDetailMedium = EnumValue
    InOutDetailHigh = EnumValue
    Material = EnumValue
    Lock = EnumValue
    SoftLock = EnumValue
    Origin = EnumValue
    Pick = EnumValue
    Render = EnumValue
    Selectable = EnumValue
    Template = EnumValue
    Unload = EnumValue
    Visible = EnumValue
    XRay = EnumValue


class nodeTypeFilter:

    NoFilter = EnumValue
    Sop = EnumValue
    Dop = EnumValue
    Pop = EnumValue
    Popnet = EnumValue
    Chop = EnumValue
    Chopnet = EnumValue
    Cop = EnumValue
    Copnet = EnumValue
    Vop = EnumValue
    Vopnet = EnumValue
    Rop = EnumValue
    Shop = EnumValue
    Obj = EnumValue
    ObjBone = EnumValue
    ObjCamera = EnumValue
    ObjFog = EnumValue
    ObjGeometry = EnumValue
    ObjGeometryOrFog = EnumValue
    ObjLight = EnumValue
    ObjMuscle = EnumValue
    ObjSubnet = EnumValue
    ShopAtmosphere = EnumValue
    ShopCVEX = EnumValue
    ShopDisplacement = EnumValue
    ShopImage3D = EnumValue
    ShopInterior = EnumValue
    ShopLight = EnumValue
    ShopLightShadow = EnumValue
    ShopShopMaterial = EnumValue
    ShopPhoton = EnumValue
    ShopProperties = EnumValue
    ShopSurface = EnumValue


class nodeTypeSource:

    Internal = EnumValue
    CompiledCode = EnumValue
    VexCode = EnumValue
    RslCode = EnumValue
    Subnet = EnumValue


class numericType:

    Int8 = EnumValue
    Int16 = EnumValue
    Int32 = EnumValue
    Int64 = EnumValue
    Float16 = EnumValue
    Float32 = EnumValue
    Float64 = EnumValue


class orientUpAxis:

    Y = EnumValue
    Z = EnumValue


class paneLinkType:

    Pinned = EnumValue
    Group1 = EnumValue
    Group2 = EnumValue
    Group3 = EnumValue
    Group4 = EnumValue
    Group5 = EnumValue
    Group6 = EnumValue
    Group7 = EnumValue
    Group8 = EnumValue
    FollowSelection = EnumValue


class paneTabType:

    SceneViewer = EnumValue
    ChannelViewer = EnumValue
    CompositorViewer = EnumValue
    OutputViewer = EnumValue
    MaterialPalette = EnumValue
    IPRViewer = EnumValue
    NetworkEditor = EnumValue
    Parm = EnumValue
    DetailsView = EnumValue
    ChannelEditor = EnumValue
    ChannelList = EnumValue
    Textport = EnumValue
    HandleList = EnumValue
    BundleList = EnumValue
    TakeList = EnumValue
    TreeView = EnumValue
    HelpBrowser = EnumValue
    PythonPanel = EnumValue
    ParmSpreadsheet = EnumValue
    LightLinker = EnumValue
    AssetBrowser = EnumValue


class parmBakeChop:

    Off = EnumValue
    KeepExportFlag = EnumValue
    DisableExportFlag = EnumValue
    CreateDeleteChop = EnumValue


class parmCondType:

    DisableWhen = EnumValue
    HideWhen = EnumValue


class parmData:

    Int = EnumValue
    Float = EnumValue
    String = EnumValue
    Ramp = EnumValue


class parmExtrapolate:

    Default = EnumValue
    Hold = EnumValue
    Cycle = EnumValue
    Extend = EnumValue
    Slope = EnumValue
    CycleOffset = EnumValue
    Oscillate = EnumValue


class parmLook:

    Regular = EnumValue
    Logarithmic = EnumValue
    Angle = EnumValue
    Vector = EnumValue
    ColorSquare = EnumValue
    HueCircle = EnumValue
    CRGBAPlaneChooser = EnumValue


class parmNamingScheme:

    Base1 = EnumValue
    XYZW = EnumValue
    XYWH = EnumValue
    UVW = EnumValue
    RGBA = EnumValue
    MinMax = EnumValue
    MaxMin = EnumValue
    StartEnd = EnumValue
    BeginEnd = EnumValue


class parmTemplateType:

    Int = EnumValue
    Float = EnumValue
    String = EnumValue
    Toggle = EnumValue
    Menu = EnumValue
    Button = EnumValue
    FolderSet = EnumValue
    Separator = EnumValue
    Label = EnumValue
    Ramp = EnumValue


class perfMonObjectView:

    List = EnumValue
    Tree = EnumValue
    EventLog = EnumValue


class perfMonTimeFormat:

    Absolute = EnumValue
    Percent = EnumValue


class pickFacing:

    Front = EnumValue
    Back = EnumValue
    FrontAndBack = EnumValue


class pickModifier:

    Add = EnumValue
    Toggle = EnumValue
    Remove = EnumValue
    Replace = EnumValue
    Intersect = EnumValue


class pickStyle:

    Box = EnumValue
    Lasso = EnumValue
    Brush = EnumValue
    Laser = EnumValue


class playMode:

    Loop = EnumValue
    Once = EnumValue
    Zigzag = EnumValue


class playbarEvent:

    Started = EnumValue
    Stopped = EnumValue
    FrameChanged = EnumValue


class positionType:

    WorldSpace = EnumValue
    ViewportXY = EnumValue
    ViewportUV = EnumValue


class primType:

    Polygon = EnumValue
    NURBSCurve = EnumValue
    BezierCurve = EnumValue
    Mesh = EnumValue
    NURBSSurface = EnumValue
    BezierSurface = EnumValue
    Circle = EnumValue
    Sphere = EnumValue
    Tube = EnumValue
    Metaball = EnumValue
    TriangleFan = EnumValue
    TriangleStrip = EnumValue
    TriangleBezier = EnumValue
    PastedSurface = EnumValue
    Volume = EnumValue
    ParticleSystem = EnumValue
    Tetrahedron = EnumValue
    PolySoup = EnumValue
    VDB = EnumValue
    AlembicRef = EnumValue
    Custom = EnumValue
    PackedPrim = EnumValue
    PackedFragment = EnumValue
    PackedGeometry = EnumValue
    Agent = EnumValue
    Unknown = EnumValue


class radialItemLocation:

    Top = EnumValue
    TopLeft = EnumValue
    Left = EnumValue
    BottomLeft = EnumValue
    Bottom = EnumValue
    BottomRight = EnumValue
    Right = EnumValue
    TopRight = EnumValue


class radialItemType:

    Script = EnumValue
    Submenu = EnumValue
    Menu = EnumValue


class rampBasis:

    Linear = EnumValue
    Constant = EnumValue
    CatmullRom = EnumValue
    MonotoneCubic = EnumValue
    Bezier = EnumValue
    BSpline = EnumValue
    Hermite = EnumValue


class rampParmType:

    Color = EnumValue
    Float = EnumValue


class renderMethod:

    RopByRop = EnumValue
    FrameByFrame = EnumValue


class saveMode:

    Text = EnumValue
    Binary = EnumValue


class scriptLanguage:

    Python = EnumValue
    Hscript = EnumValue


class selectionMode:

    Object = EnumValue
    Geometry = EnumValue
    Dynamics = EnumValue


class severityType:

    Message = EnumValue
    ImportantMessage = EnumValue
    Warning = EnumValue
    Error = EnumValue
    Fatal = EnumValue


class shaderType:

    Invalid = EnumValue
    Surface = EnumValue
    SurfaceShadow = EnumValue
    Displacement = EnumValue
    Geometry = EnumValue
    Interior = EnumValue
    Light = EnumValue
    LightShadow = EnumValue
    Atmosphere = EnumValue
    Lens = EnumValue
    Output = EnumValue
    Background = EnumValue
    Photon = EnumValue
    Image3D = EnumValue
    BSDF = EnumValue
    CVEX = EnumValue
    Mutable = EnumValue
    Properties = EnumValue
    Material = EnumValue
    VopMaterial = EnumValue
    ShaderClass = EnumValue


class snappingMode:

    Off = EnumValue
    Grid = EnumValue
    Prim = EnumValue
    Point = EnumValue
    Multi = EnumValue


class stateGenerateMode:

    Insert = EnumValue
    Branch = EnumValue


class stateViewerType:

    Scene = EnumValue
    Compositor = EnumValue


class stringParmType:

    Regular = EnumValue
    FileReference = EnumValue
    NodeReference = EnumValue
    NodeReferenceList = EnumValue


class updateMode:

    AutoUpdate = EnumValue
    OnMouseUp = EnumValue
    Manual = EnumValue


class vdbData:

    Boolean = EnumValue
    Float = EnumValue
    Int = EnumValue
    Vector3 = EnumValue


class viewportParticleDisplay:

    Points = EnumValue
    Lines = EnumValue
    Pixels = EnumValue
    Discs = EnumValue


class viewportStandInGeometry:

    DisplayOff = EnumValue
    LocationMarker = EnumValue
    BoundingBox = EnumValue


class viewportVisualizerCategory:

    Common = EnumValue
    Scene = EnumValue
    Node = EnumValue


class viewportVisualizerScope:

    NodeOnly = EnumValue
    SameNetworkTypeDescendants = EnumValue
    AllDescendents = EnumValue
    Global = EnumValue


class viewportVolumeQuality:

    VeryLow = EnumValue
    Low = EnumValue
    Normal = EnumValue
    High = EnumValue


class vopParmGenType:

    Constant = EnumValue
    Parameter = EnumValue
    SubnetInput = EnumValue


class BaseKeyframe():


    def asCode(self, brief=True, save_keys_in_frames=True, function_name=None):

        return ""
    
    def evaluatedType(self):

        return EnumValue
    
    def expression(self):

        return ""
    
    def expressionLanguage(self):

        return EnumValue
    
    def frame(self):

        return 0.0
    
    def isExpressionLanguageSet(self):

        return True
    
    def isExpressionSet(self):

        return True
    
    def isTimeSet(self):

        return True
    
    def setExpression(self, expression, language=None):

        return None
    
    def setFrame(self, frame):

        return None
    
    def setTime(self, time):

        return None
    
    def time(self):

        return 0.0
    

class Keyframe(BaseKeyframe):


    def __init__(self, values):

        pass
    
    def accel(self):

        return 0.0
    
    def asJSON(self, brief=True, save_keys_in_frames=True):

        return {}
    
    def fromJSON(self, keyframe_dict):

        return None
    
    def evaluatedType(self):

        return EnumValue
    
    def inAccel(self):

        return 0.0
    
    def inSlope(self):

        return 0.0
    
    def interpretAccelAsRatio(self, on):

        return None
    
    def inValue(self):

        return 0.0
    
    def isAccelInterpretedAsRatio(self):

        return True
    
    def isAccelSet(self):

        return True
    
    def isAccelTied(self):

        return True
    
    def isInSlopeAuto(self):

        return True
    
    def isSlopeAuto(self):

        return True
    
    def isSlopeSet(self):

        return True
    
    def isSlopeTied(self):

        return True
    
    def isValueSet(self):

        return True
    
    def isValueTied(self):

        return True
    
    def setAccel(self, accel):

        return None
    
    def setInAccel(self, in_accel):

        return None
    
    def setInSlope(self, in_slope):

        return None
    
    def setInSlopeAuto(self, on):

        return None
    
    def setInValue(self, in_value):

        return None
    
    def setSlope(self, slope):

        return None
    
    def setSlopeAuto(self, on):

        return None
    
    def setValue(self, value):

        return None
    
    def slope(self):

        return 0.0
    
    def unsetInAccel(self):

        return None
    
    def unsetInSlope(self):

        return None
    
    def unsetInValue(self):

        return None
    
    def value(self):

        return 0.0
    

class StringKeyframe(BaseKeyframe):


    def asJSON(self, brief=True, save_keys_in_frames=True):

        return {}
    
    def fromJSON(self, keyframe_dict):

        return None
    
    def evaluatedType(self):

        return EnumValue
    

class HDADefinition():


    def nodeType(self):

        return NodeType
    
    def nodeTypeCategory(self):

        return NodeTypeCategory
    
    def nodeTypeName(self):

        return ""
    

class HDAModule():

    pass

class HDAOptions():


    def __init__(self):

        pass
    
    def checkForExternalLinks(self):

        return True
    
    def setCheckForExternalLinks(self, check_for_external_links):

        return None
    
    def forbidOutsideParms(self):

        return True
    
    def setForbidOutsideParms(self, forbid_outside_parms):

        return None
    
    def lockContents(self):

        return True
    
    def setLockContents(self, lock_contents):

        return None
    
    def unlockNewInstances(self):

        return True
    
    def setUnlockNewInstances(self, unlock_new_instances):

        return None
    
    def compressContents(self):

        return True
    
    def setCompressContents(self, compress_contents):

        return None
    
    def makeInitialParmsDefaults(self):

        return True
    
    def setMakeInitialParmsDefaults(self, make_initial_parms_defaults):

        return None
    
    def saveInitialParmsAndContents(self):

        return True
    
    def setSaveInitialParmsAndContents(self, save_initial_parms_and_contents):

        return None
    
    def saveSpareParms(self):

        return True
    
    def setSaveSpareParms(self, save_spare_parms):

        return None
    
    def saveCachedCode(self):

        return True
    
    def setSaveCachedCode(self, save_cached_code):

        return None
    
    def parametersFromVexCode(self):

        return True
    
    def setParametersFromVexCode(self, parameters_from_vex_code):

        return None
    
    def prefixDroppedParmNames(self):

        return True
    
    def setPrefixDroppedParmNames(self, prefix_dropped_parm_names):

        return None
    
    def prefixDroppedParmLabels(self):

        return True
    
    def setPrefixDroppedParmLabels(self, prefix_dropped_parm_labels):

        return None
    

class Pane():


    def tabs(self):

        return (PaneTab, )
    
    def tabOfType(self, type, index=object):

        return PaneTab
    
    def currentTab(self):

        return PaneTab
    
    def createTab(self, type):

        return PaneTab
    
    def splitHorizontally(self):

        return Pane
    
    def splitVertically(self):

        return Pane
    
    def desktop(self):

        return Desktop
    
    def isMaximized(self):

        return True
    
    def setIsMaximized(self, on):

        return None
    
    def getSplitParent(self):

        return Pane
    
    def getSplitChild(self, index):

        return Pane
    
    def splitSwap(self):

        return None
    
    def splitRotate(self):

        return None
    
    def isSplitMinimized(self):

        return True
    
    def isSplitMaximized(self):

        return True
    
    def setIsSplitMaximized(self, on):

        return True
    
    def isSplit(self):

        return True
    
    def setSplitFraction(self, fraction):

        return None
    
    def getSplitFraction(self, fraction):

        return 0.0
    
    def setSplitDirection(self, dir):

        return None
    
    def getSplitDirection(self, dir):

        return 0.0
    

class HDASection():


    def name(self):

        return ""
    
    def definition(self):

        return HDADefinition
    
    def contents(self, compressionType=object):

        return ""
    
    def size(self):

        return 0
    
    def setContents(self, contents, compressionType=object):

        return None
    
    def destroy(self):

        return None
    
    def modificationTime(self):

        return 0
    

class ChannelEditorPane(Pane):


    def graph(self):

        return ChannelGraph
    
    def channelListSplitFraction(self):

        return 0.0
    
    def setChannelListSplitFraction(self, value):

        return None
    
    def displayFilter(self):

        return ""
    
    def setDisplayFilter(self, filter):

        return None
    
    def editorMode(self):

        return EnumValue
    
    def setEditorMode(self, mode):

        return None
    
    def templateFilter(self):

        return ""
    
    def setTemplateFilter(self, filter):

        return None
    
    def colorsCallback(self):

        return ""
    
    def setColorsCallback(self, callback_name):

        return True
    
    def registerColorsCallback(self, callback_name, callback_object):

        return True
    
    def unregisterColorsCallback(self, callback_name):

        return True
    
    def colorsCallbacks(self):

        return ("", )
    

class ChannelGraph():


    def selectedKeyframes(self):

        return {Parm: (BaseKeyframe, )}
    

class NetworkItem():


    def networkItemType(self):

        return networkItemType
    

class NetworkMovableItem(NetworkItem):


    def name(self):

        return ""
    
    def setName(self, name, unique_name=True):

        return None
    
    def digitsInName(self):

        return 0
    
    def path(self):

        return ""
    
    def relativePathTo(self, base_node):

        return ""
    

class Node(NetworkItem, NetworkMovableItem):


    def node(self, node_path):

        return Node
    
    def nodes(self, node_path_tuple):

        return (Node, )
    
    def item(self, item_path):

        return NetworkMovableItem
    
    def items(self, item_path_tuple):

        return (NetworkMovableItem, )
    
    def isNetwork(self):

        return True
    
    def children(self):

        return (Node, )
    
    def allItems(self):

        return (NetworkMovableItem, )
    
    def allSubChildren(self, top_down=True):

        return (Node, )
    
    def allNodes(self):

        return Node
    
    def glob(self, pattern, ignore_case=True):

        return (Node, )
    
    def recursiveGlob(self, pattern, filter=object):

        return (Node, )
    

class Prim():


    def attribValue(self, name_or_attrib):

        return object
    
    def floatAttribValue(self, attrib):

        return 0.0
    
    def floatListAttribValue(self, name_or_attrib):

        return (0.0, )
    
    def intAttribValue(self, name_or_attrib):

        return 0
    
    def intListAttribValue(self, name_or_attrib):

        return (0, )
    
    def stringAttribValue(self, name_or_attrib):

        return ""
    
    def stringListAttribValue(self, name_or_attrib):

        return ("", )
    
    def setAttribValue(self, name_or_attrib, attrib_value):

        return None
    
    def attribType(self):

        return EnumValue
    
    def intrinsicValueDict(self):

        return {"": object}
    
    def intrinsicValue(self, intrinsic_name):

        return object
    
    def intrinsicNames(self):

        return ("", )
    
    def setIntrinsicValue(self, intrinsic_name, value):

        return None
    
    def intrinsicReadOnly(self, intrinsic_name):

        return True
    
    def intrinsicSize(self, intrinsic_name):

        return 0
    
    def positionAtInterior(self, u, v, w=object):

        return Vector3
    
    def attribValueAtInterior(self, attrib_or_name, u, v, w=object):

        return object
    
    def geometry(self):

        return Geometry
    
    def number(self):

        return 0
    
    def type(self):

        return EnumValue
    
    def vertices(self):

        return Vertex
    
    def numVertices(self):

        return 0
    
    def vertex(self, index):

        return Vertex
    
    def boundingBox(self):

        return BoundingBox
    
    def nearestToPosition(self, pos3):

        return None
    
    def groups(self):

        return (PrimGroup, )
    

class ChopNode(NetworkItem, NetworkMovableItem, Node):


    def bypass(self, on):

        return None
    
    def clipData(self, binary):

        return ""
    
    def setClipData(self, data, binary):

        return None
    
    def frameToSamples(self, frame):

        return 0.0
    
    def isAudioFlagSet(self):

        return True
    
    def isBypassed(self):

        return True
    
    def isDisplayFlagSet(self):

        return True
    
    def isExportFlagSet(self):

        return True
    
    def isLocked(self):

        return True
    
    def isUnloadFlagSet(self):

        return True
    
    def sampleRange(self):

        return (0, 0,)
    
    def sampleRate(self):

        return 0.0
    
    def samplesToFrame(self, samples):

        return 0.0
    
    def samplesToTime(self, samples):

        return 0.0
    
    def setAudioFlag(self, on):

        return None
    
    def setDisplayFlag(self, on):

        return None
    
    def setExportFlag(self, on):

        return None
    
    def setLocked(self, on):

        return None
    
    def setUnloadFlag(self, on):

        return None
    
    def timeToSamples(self, time):

        return 0.0
    
    def tracks(self):

        return (Track, )
    
    def track(self, track_name):

        return Track
    

class PackedPrim(Prim):


    def transform(self):

        return Matrix3
    
    def fullTransform(self):

        return Matrix4
    
    def setTransform(self, m4):

        return None
    

class Track():


    def allSamples(self):

        return (0.0, )
    
    def chopNode(self):

        return ChopNode
    
    def eval(self):

        return 0.0
    
    def evalAtFrame(self, frame):

        return 0.0
    
    def evalAtSample(self, sample):

        return 0.0
    
    def evalAtSampleIndex(self, index):

        return 0.0
    
    def evalAtTime(self, time):

        return 0.0
    
    def evalAtFrameRange(self, start, end):

        return (0.0, )
    
    def evalAtSampleRange(self, start, end):

        return (0.0, )
    
    def evalAtTimeRange(self, start, end):

        return (0.0, )
    
    def name(self):

        return ""
    
    def numSamples(self):

        return 0
    

class Agent(Prim, PackedPrim):


    def clipCatalog(self):

        return (AgentClip, )
    
    def clips(self):

        return (AgentClip, )
    
    def clipTimes(self):

        return (0.0, )
    
    def clipWeights(self):

        return (0.0, )
    
    def collisionLayer(self):

        return AgentLayer
    
    def currentLayer(self):

        return AgentLayer
    
    def definition(self):

        return AgentDefinition
    
    def layers(self):

        return (AgentLayer, )
    
    def localTransform(self, transform):

        return Matrix4
    
    def rig(self):

        return AgentRig
    
    def setClips(self, clips):

        return None
    
    def setClipTimes(self, times):

        return None
    
    def setClipWeights(self, weights):

        return None
    
    def setCurrentLayer(self, layer):

        return None
    
    def setCollisionLayer(self, layer):

        return None
    
    def setDefinition(self, definition):

        return None
    
    def setLocalTransform(self, xform, index):

        return None
    
    def setWorldTransform(self, xform, index):

        return None
    
    def shapeLibrary(self):

        return AgentShapeLibrary
    
    def worldTransform(self, transform):

        return Matrix4
    

class AgentClip():


    def __init__(self, name, filename, rig, keep_external_ref=True):

        pass
    
    def __init__(self, name, chop, rig, frame=object):

        pass
    
    def __init__(self, clip, rig, name=object):

        pass
    
    def channelNames(self):

        return ("", )
    
    def data(self, binary, worldspace=True):

        return ""
    
    def length(self):

        return 0.0
    
    def name(self):

        return ""
    
    def sample(self, time, channel_name):

        return 0.0
    
    def sampleLocal(self, time, transform):

        return Matrix4
    
    def sampleRate(self):

        return 0.0
    
    def sampleWorld(self, time, transform):

        return Matrix4
    

class AgentDefinition():


    def __init__(self, rig, shapelib):

        pass
    
    def addClip(self, clip):

        return None
    
    def addLayer(self, layer):

        return None
    
    def addTransformGroup(self, group):

        return None
    
    def clips(self):

        return (AgentClip, )
    
    def findClip(self, name):

        return AgentClip
    
    def findLayer(self, name):

        return AgentLayer
    
    def findTransformGroup(self, name):

        return AgentTransformGroup
    
    def freeze(self, new_shapelib=None):

        return AgentDefinition
    
    def layers(self):

        return (AgentLayer, )
    
    def rig(self):

        return AgentRig
    
    def shapeLibrary(self):

        return AgentShapeLibrary
    
    def transformGroups(self):

        return (AgentTransformGroup, )
    

class AgentLayer():


    def __init__(self, filename, rig, shapelib, keep_external_ref=True):

        pass
    
    def __init__(self, name, rig, shapelib, shape_bindings, source_layer=None):

        pass
    
    def asJSON(self):

        return ""
    
    def bindings(self, transform=None):

        return (AgentShapeBinding, )
    
    def deformingBindings(self):

        return (AgentShapeBinding, )
    
    def name(self):

        return ""
    
    def staticBindings(self):

        return (AgentShapeBinding, )
    

class AgentRig():


    def __init__(self, filename, keep_external_ref=True):

        pass
    
    def __init__(self, name, transform_names, hierarchy):

        pass
    
    def asJSON(self):

        return ""
    
    def childIndices(self, transform):

        return (0, )
    
    def findTransform(self, transform_name):

        return 0
    
    def name(self):

        return ""
    
    def parentIndex(self, transform):

        return 0
    
    def transformCount(self):

        return 0
    
    def transformName(self, transform):

        return ""
    

class AgentShape():


    def geometry(self):

        return Geometry
    
    def name(self):

        return ""
    
    def uniqueId(self):

        return 0
    

class AgentShapeBinding():


    def __init__(self, transform, shape, deforming, bounds_scale=object):

        pass
    
    def boundsScale(self):

        return 0.0
    
    def isDeforming(self):

        return True
    
    def shape(self):

        return AgentShape
    
    def shapeId(self):

        return 0
    
    def shapeName(self):

        return ""
    
    def transformId(self):

        return 0
    

class AgentShapeLibrary():


    def __init__(self):

        pass
    
    def __init__(self, filename, keep_external_ref=True):

        pass
    
    def addShape(self, name, geometry):

        return AgentShape
    
    def data(self):

        return Geometry
    
    def freeze(self, keep_external_ref=True):

        return AgentShapeLibrary
    
    def findShape(self, shape_name):

        return AgentShape
    
    def name(self):

        return ""
    
    def shapes(self):

        return (AgentShape, )
    

class AgentTransformGroup():


    def __init__(self, filename, rig, keep_external_ref):

        pass
    
    def __init__(self, name, transforms, rig):

        pass
    
    def __init__(self, name, transforms, rig, weights):

        pass
    
    def asJSON(self):

        return ""
    
    def name(self):

        return ""
    
    def transformIndices(self):

        return (0, )
    
    def weights(self):

        return (0.0, )
    

class DopData():


    def subData(self):

        return {"": DopData}
    
    def findSubData(self, data_spec):

        return DopData
    
    def findAllSubData(self, data_spec, recurse=True):

        return {"": DopData}
    
    def freeze(self):

        return DopData
    
    def isFrozen(self):

        return True
    
    def path(self):

        return ""
    
    def selectionPath(self):

        return ""
    
    def dataType(self):

        return ""
    
    def recordTypes(self):

        return ("", )
    
    def record(self, record_type, record_index=object):

        return DopRecord
    
    def records(self, record_type):

        return (DopRecord, )
    
    def options(self):

        return DopRecord
    
    def dopNetNode(self):

        return Node
    
    def simulation(self):

        return DopSimulation
    
    def creator(self):

        return DopNode
    
    def id(self):

        return ""
    
    def createSubData(self, data_name, data_type=object, avoid_name_collisions=True):

        return DopData
    
    def attachSubData(self, data, new_data_name, avoid_name_collisions=True):

        return None
    
    def removeSubData(self, data_spec):

        return None
    
    def copyContentsFrom(self, data):

        return None
    

class DopNode(NetworkItem, NetworkMovableItem, Node):


    def processedObjects(self):

        return (DopObject, )
    
    def createdObjects(self):

        return (DopObject, )
    
    def dopNetNode(self):

        return Node
    
    def simulation(self):

        return DopSimulation
    
    def isDisplayFlagSet(self):

        return True
    
    def displayNode(self):

        return Node
    
    def setDisplayFlag(self, on):

        return None
    
    def isTemplateFlagSet(self):

        return True
    
    def setTemplateFlag(self, on):

        return None
    
    def bypass(self, on):

        return None
    
    def isBypassed(self):

        return True
    
    def objectsToProcess(self):

        return (DopObject, )
    
    def pythonSolverData(self):

        return DopData
    

class DopObject(DopData):


    def name(self):

        return ""
    
    def matches(self, pattern):

        return True
    
    def objid(self):

        return 0
    
    def transform(self, include_geometry_transform=True):

        return Matrix4
    
    def geometry(self, name=object):

        return Geometry
    
    def editableGeometry(self, name=object):

        return EditableDopGeometryGuard
    

class DopRecord():


    def field(self):

        return object
    
    def fieldNames(self):

        return ("", )
    
    def fieldType(self, field_name):

        return EnumValue
    
    def recordIndex(self):

        return 0
    
    def recordType(self):

        return ""
    
    def setField(self, field_name, value):

        return None
    
    def setFieldBool(self, field_name, value):

        return None
    

class DopRelationship(DopData):


    def name(self):

        return ""
    
    def matches(self, pattern):

        return True
    
    def setGroup(self, objects):

        return None
    
    def setAffectorGroup(self, objects):

        return None
    

class DopSimulation():


    def findData(self, data_spec):

        return DopData
    
    def findAllData(self, data_spec):

        return (DopData, )
    
    def objects(self):

        return (DopData, )
    
    def findObject(self, obj_spec):

        return DopObject
    
    def findAllObjects(self, obj_spec):

        return (DopObject, )
    
    def relationships(self):

        return (DopRelationship, )
    
    def findRelationship(self, rel_spec):

        return DopRelationship
    
    def findAllRelationships(self, rel_spec):

        return (DopRelationship, )
    
    def dopNetNode(self):

        return Node
    
    def time(self):

        return None
    
    def memoryUsage(self):

        return None
    
    def createObject(self, name, solve_on_creation_frame):

        return DopObject
    
    def removeObject(self, object):

        return None
    
    def createRelationship(self, name):

        return DopRelationship
    
    def removeRelationship(self, rel):

        return None
    

class Error():


    def description(self):

        return ""
    
    def exceptionTypeName(self):

        return ""
    
    def instanceMessage(self):

        return ""
    

class GeometryPermissionError(Error):

    pass

class InitScriptFailed(Error):

    pass

class InvalidInput(Error):

    pass

class InvalidNodeType(Error):

    pass

class InvalidSize(Error):

    pass

class KeyframeValueNotSet(Error):

    pass

class LoadWarning(Error):

    pass

class MatchDefinitionError(Error):

    pass

class NodeError(Error):

    pass

class NodeWarning(Error):

    pass

class NotAvailable(Error):

    pass

class ObjectWasDeleted(Error):

    pass

class OperationFailed(Error):

    pass

class OperationInterrupted(Error):

    pass

class PermissionError(Error):

    pass

class SystemExit(Error):


    def code(self):

        return 0
    

class TypeError(Error):

    pass

class ValueError(Error):

    pass

class EnumValue():


    def name(self):

        return ""
    

class InterruptableOperation():


    def __init__(self, operation_name, long_operation_name=None, open_interrupt_dialog=True):

        pass
    
    def updateLongProgress(self, percentage=object, long_op_status=None):

        return None
    
    def updateProgress(self, percentage=object):

        return None
    

class RedrawBlock():


    def __init__(self):

        pass
    

class UndosDisabler():

    pass

class UndosGroup():


    def label(self):

        return None
    

class Attrib():


    def name(self):

        return ""
    
    def type(self):

        return EnumValue
    
    def dataType(self):

        return EnumValue
    
    def isArrayType(self):

        return True
    
    def qualifier(self):

        return ""
    
    def size(self):

        return 0
    
    def setSize(self):

        return None
    
    def defaultValue(self):

        return object
    
    def strings(self):

        return ("", )
    
    def indexPairPropertyTables(self):

        return (IndexPairPropertyTable, )
    
    def geometry(self):

        return Geometry
    
    def isTransformedAsNormal(self):

        return True
    
    def destroy(self):

        return None
    
    def options(self):

        return {"": True}
    
    def option(self, name):

        return object
    
    def optionType(self, name):

        return EnumValue
    
    def setOption(self, name, value, type_hint=object):

        return None
    
    def removeOption(self, name):

        return None
    

class Edge():


    def points(self):

        return (Point, )
    
    def geometry(self):

        return Geometry
    
    def prims(self):

        return (Prim, )
    
    def edgeId(self):

        return ""
    
    def length(self):

        return 0.0
    

class EdgeGroup():


    def name(self):

        return None
    
    def geometry(self):

        return Geometry
    
    def edges(self):

        return (Edge, )
    
    def contains(self, edge):

        return True
    
    def add(self, edge_or_list_or_edge_group):

        return None
    
    def remove(self, edge_or_list_or_edge_group):

        return None
    
    def clear(self):

        return None
    
    def destroy(self):

        return None
    

class Face(Prim):


    def addVertex(self, point):

        return Vertex
    
    def isClosed(self):

        return True
    
    def setIsClosed(self, on):

        return None
    
    def normal(self):

        return Vector3
    
    def positionAt(self, u):

        return Vector3
    
    def attribValueAt(self, attrib_or_name, u, du=object):

        return object
    

class Geometry():


    def findPointAttrib(self, name):

        return Attrib
    
    def findPrimAttrib(self, name):

        return Attrib
    
    def findVertexAttrib(self, name):

        return Attrib
    
    def findGlobalAttrib(self, name):

        return Attrib
    
    def pointAttribs(self):

        return (Attrib, )
    
    def primAttribs(self):

        return (Attrib, )
    
    def vertexAttribs(self):

        return (Attrib, )
    
    def globalAttribs(self):

        return (Attrib, )
    
    def addAttrib(self, type, name, default_value, transform_as_normal=True, create_local_variable=True):

        return Attrib
    
    def addArrayAttrib(self, type, name, data_type, tuple_size=object):

        return Attrib
    
    def attribValue(self, name_or_attrib):

        return object
    
    def floatAttribValue(self, name_or_attrib):

        return 0.0
    
    def floatListAttribValue(self, name_or_attrib):

        return (0.0, )
    
    def intAttribValue(self, name_or_attrib):

        return 0
    
    def intListAttribValue(self, name_or_attrib):

        return (0, )
    
    def stringAttribValue(self, name_or_attrib):

        return ""
    
    def stringListAttribValue(self, name_or_attrib):

        return (0, )
    
    def setGlobalAttribValue(self, name_or_attrib, attrib_value):

        return None
    
    def attribType(self):

        return EnumValue
    
    def renamePointAttrib(self, old_name, new_name):

        return None
    
    def renamePrimAttrib(self, old_name, new_name):

        return None
    
    def renameVertexAttrib(self, old_name, new_name):

        return None
    
    def renameGlobalAttrib(self, old_name, new_name):

        return None
    

class IndexPairPropertyTable():


    def attrib(self):

        return Attrib
    
    def numIndices(self):

        return 0
    
    def propertyNames(self):

        return ("", )
    
    def propertyDataType(self, property_name):

        return EnumValue
    
    def propertySize(self, property_name):

        return 0
    
    def floatPropertyValueAtIndex(self, property_name, row):

        return 0.0
    
    def floatListPropertyValueAtIndex(self, property_name, row):

        return (0.0, )
    
    def intPropertyValueAtIndex(self, property_name, row):

        return 0
    
    def intListPropertyValueAtIndex(self, property_name, row):

        return (0, )
    
    def stringPropertyValueAtIndex(self, property_name, row):

        return ""
    
    def stringListPropertyValueAtIndex(self, property_name, row):

        return ("", )
    

class PackedFragment(Prim, PackedPrim):


    def setEmbeddedGeometry(self, geo, attrib, name):

        return None
    

class PackedGeometry(Prim, PackedPrim):


    def setEmbeddedGeometry(self, geo):

        return None
    

class Point():


    def attribValue(self, name_or_attrib):

        return object
    
    def floatAttribValue(self, name_or_attrib):

        return 0.0
    
    def floatListAttribValue(self, name_or_attrib):

        return (0.0, )
    
    def intAttribValue(self, name_or_attrib):

        return 0
    
    def intListAttribValue(self, name_or_attrib):

        return (0, )
    
    def stringAttribValue(self, name_or_attrib):

        return ""
    
    def stringListAttribValue(self, name_or_attrib):

        return ("", )
    
    def position(self):

        return Vector3
    
    def weight(self):

        return 0.0
    
    def setAttribValue(self, name_or_attrib, attrib_value):

        return None
    
    def setPosition(self, position):

        return None
    
    def setWeight(self, weight):

        return None
    
    def attribType(self):

        return EnumValue
    
    def geometry(self):

        return Geometry
    
    def number(self):

        return 0
    

class PointGroup():


    def name(self):

        return None
    
    def geometry(self):

        return Geometry
    
    def points(self):

        return (Point, )
    
    def contains(self, point):

        return True
    
    def add(self, point_or_list_or_point_group):

        return None
    
    def remove(self, point_or_list_or_point_group):

        return None
    
    def clear(self):

        return None
    
    def destroy(self):

        return None
    
    def options(self):

        return {"": True}
    
    def option(self, name):

        return object
    
    def optionType(self, name):

        return EnumValue
    
    def setOption(self, name, value, type_hint=object):

        return None
    
    def removeOption(self, name):

        return None
    

class Polygon(Prim, Face):

    pass

class PrimGroup():


    def name(self):

        return None
    
    def geometry(self):

        return Geometry
    
    def prims(self):

        return (Prim, )
    
    def contains(self, prim):

        return True
    
    def add(self, prim_or_list_or_prim_group):

        return None
    
    def remove(self, prim_or_list_or_prim_group):

        return None
    
    def clear(self):

        return None
    
    def destroy(self):

        return None
    
    def options(self):

        return {"": True}
    
    def option(self, name):

        return object
    
    def optionType(self, name):

        return EnumValue
    
    def setOption(self, name, value, type_hint=object):

        return None
    
    def removeOption(self, name):

        return None
    

class Quadric(Prim):


    def transform(self):

        return Matrix3
    

class Selection():


    def __init__(self, selection_type):

        pass
    
    def __init__(self, geo, selection_type, selection_string):

        pass
    
    def __init__(self, prims):

        pass
    
    def __init__(self, points):

        pass
    
    def __init__(self, vertices):

        pass
    
    def __init__(self, edges):

        pass
    
    def freeze(self):

        return Selection
    
    def invert(self, geo):

        return None
    
    def convert(self, geo, selection_type):

        return None
    
    def boundary(self, geo, uv_connectivity=True):

        return None
    
    def grow(self, geo, uv_connectivity=True):

        return None
    
    def shrink(self, geo, uv_connectivity=True):

        return None
    
    def combine(self, geo, selection, modifier):

        return None
    
    def clear(self):

        return None
    
    def selectionType(self):

        return None
    
    def numSelected(self):

        return None
    
    def prims(self, goe):

        return (Prim, )
    
    def points(self, goe):

        return (Point, )
    
    def vertices(self, goe):

        return (Vertex, )
    
    def edges(self, goe):

        return (Edge, )
    
    def selectionString(self, geo, force_numeric=True, collapse_where_possible=True, asterisk_to_select_all=True):

        return ""
    

class SopNode(NetworkItem, NetworkMovableItem, Node):


    def geometry(self, output_index=object):

        return Geometry
    
    def geometryAtFrame(self, frame, output_index=object):

        return Geometry
    
    def inputGeometry(self, index):

        return Geometry
    
    def inputGeometryAtFrame(self, frame, index):

        return Geometry
    
    def selection(self, selection_type):

        return Selection
    
    def setSelection(self, selection):

        return None
    
    def curPoint(self):

        return Point
    
    def setCurPoint(self, point_or_none):

        return None
    
    def curPrim(self):

        return Prim
    
    def setCurPrim(self, prim_or_none):

        return None
    
    def curVertex(self):

        return Vertex
    
    def setCurVertex(self, vertex_or_none):

        return None
    
    def displayNode(self):

        return Node
    
    def renderNode(self):

        return Node
    
    def isBypassed(self):

        return True
    
    def bypass(self, on):

        return None
    
    def isDisplayFlagSet(self):

        return True
    
    def setDisplayFlag(self, on):

        return None
    
    def isRenderFlagSet(self):

        return True
    
    def setRenderFlag(self, on):

        return None
    
    def isHighlightFlagSet(self):

        return True
    
    def setHighlightFlag(self, on):

        return None
    
    def isTemplateFlagSet(self):

        return True
    
    def setTemplateFlag(self, on):

        return None
    
    def isSelectableTemplateFlagSet(self):

        return True
    
    def setSelectableTemplateFlag(self, on):

        return None
    
    def isHardLocked(self):

        return True
    
    def setHardLocked(self, on):

        return None
    
    def isSoftLocked(self):

        return True
    
    def setSoftLocked(self, on):

        return None
    
    def isUnloadFlagSet(self):

        return True
    
    def setUnloadFlag(self, on):

        return None
    
    def hasVerb(self):

        return True
    
    def verb(self):

        return SopVerb
    

class SopVerb(NetworkItem, NetworkMovableItem, Node):


    def execute(self, destgeo, inputgeolist):

        return None
    
    def loadParmsFromNode(self, sopnode):

        return None
    
    def parms(self):

        return {}
    
    def setParms(self, parmdictionary):

        return None
    
    def minNumInputs(self):

        return 0
    

class Surface(Prim):


    def numCols(self):

        return None
    
    def numRows(self):

        return None
    
    def vertex(self, u_index, v_index):

        return None
    
    def verticesInCol(self, u_index):

        return None
    
    def verticesInRow(self, v_index):

        return None
    
    def addCol(self, after=object):

        return None
    
    def addRow(self, after=object):

        return None
    
    def positionAt(self, u, v):

        return Vector3
    
    def normalAt(self, u, v):

        return Vector3
    
    def attribValueAt(self, attrib_or_name, u, v, du=object, dv=object):

        return object
    
    def isClosedInU(self):

        return None
    
    def isClosedInV(self):

        return None
    

class VDB(Prim):


    def sample(self, position):

        return 0.0
    
    def gradient(self, position):

        return Vector3
    
    def voxel(self, index):

        return 0.0
    
    def resolution(self):

        return Vector3
    
    def indexToPos(self, index):

        return Vector3
    
    def posToIndex(self, position):

        return (0, )
    
    def isSDF(self):

        return True
    
    def transform(self):

        return Matrix3
    
    def taper(self):

        return 0
    
    def isEmpty(self):

        return True
    
    def activeVoxelCount(self):

        return 0
    
    def activeVoxelBoundingBox(self):

        return BoundingBox
    
    def voxelSize(self):

        return Vector3
    
    def dataType(self):

        return vdbData
    
    def voxelRange(self, range):

        return (True, )
    
    def voxelRangeAsBool(self, range):

        return (True, )
    
    def voxelRangeAsFloat(self, range):

        return (0.0, )
    
    def voxelRangeAsInt(self, range):

        return (0, )
    
    def voxelRangeAsVector3(self, range):

        return (Vector3, )
    

class Vertex():


    def attribValue(self, name_or_attrib):

        return object
    
    def floatAttribValue(self, name_or_attrib):

        return 0.0
    
    def floatListAttribValue(self, name_or_attrib):

        return (0.0, )
    
    def intAttribValue(self, name_or_attrib):

        return 0
    
    def intListAttribValue(self, name_or_attrib):

        return (0, )
    
    def stringAttribValue(self, name_or_attrib):

        return ""
    
    def stringListAttribValue(self, name_or_attrib):

        return ("", )
    
    def setAttribValue(self, name_or_attrib, attrib_value):

        return None
    
    def attribType(self):

        return EnumValue
    
    def point(self):

        return Point
    
    def prim(self):

        return Prim
    
    def geometry(self):

        return Geometry
    
    def number(self):

        return 0
    
    def linearNumber(self):

        return 0
    

class PathBasedPaneTab(Pane):


    def cd(self, path):

        return None
    
    def currentNode(self):

        return Node
    
    def pwd(self):

        return Node
    
    def setCurrentNode(self, node, pick_node=True):

        return None
    
    def setPwd(self, node):

        return None
    

class Volume(Prim):


    def resolution(self):

        return Vector3
    
    def sample(self, position):

        return 0.0
    
    def gradient(self, position):

        return Vector3
    
    def voxel(self, index):

        return 0.0
    
    def setVoxel(self, index, value):

        return None
    
    def allVoxels(self):

        return (0.0, )
    
    def allVoxelsAsString(self):

        return ""
    
    def setAllVoxels(self, values):

        return None
    
    def setAllVoxelsFromString(self, values):

        return None
    
    def voxelSlice(self, plane, index):

        return (0.0, )
    
    def voxelSliceAsString(self, plane, index):

        return ""
    
    def setVoxelSlice(self, values, plane, index):

        return None
    
    def setVoxelSliceFromString(self, values, plane, index):

        return None
    
    def posToIndex(self, position):

        return (0, )
    
    def indexToPos(self, index):

        return Vector3
    
    def isValidIndex(self, index):

        return True
    
    def isSDF(self):

        return True
    
    def isHeightField(self):

        return True
    
    def volumeAverage(self):

        return 0.0
    
    def volumeMin(self):

        return 0.0
    
    def volumeMax(self):

        return 0.0
    
    def transform(self):

        return Matrix3
    
    def setTransform(self, matrix4):

        return None
    

class CompositorViewer(Pane, PathBasedPaneTab):


    def currentState(self):

        return ""
    
    def enterViewState(self, wait_for_exit=True):

        return None
    
    def setCurrentState(self, state, wait_for_exit=True):

        return None
    

class CopNode(NetworkItem, NetworkMovableItem, Node):


    def planes(self):

        return ("", )
    
    def components(self, plane):

        return ("", )
    
    def xRes(self):

        return None
    
    def yRes(self):

        return None
    
    def imageBounds(self, plane=object):

        return (0, )
    
    def depth(self, plane):

        return EnumValue
    
    def maskInputIndex(self):

        return 0
    
    def allPixels(self, plane=object, component=None, interleaved=True, time=object):

        return (0.0, )
    
    def allPixelsAsString(self, plane=object, component=None, interleaved=True, time=object, depth=None):

        return ""
    
    def setPixelsOfCookingPlane(self, values, component=None, interleaved=True, flip_vertically=True):

        return None
    
    def setPixelsOfCookingPlaneFromString(self, values, component=None, interleaved=True, depth=None, flip_vertically=True):

        return None
    
    def saveImage(self, file_name, frame_range=tuple()):

        return None
    
    def getPixelByUV(self, plane, u, v, component=None, interpolate=True):

        return (0.0, )
    
    def getPixelHSVByUV(self, u, v, interpolate=True):

        return (0.0, )
    
    def getPixelLuminanceByUV(self, u, v, interpolate=True):

        return 0.0
    
    def isSingleImage(self):

        return True
    
    def sequenceStartFrame(self):

        return 0.0
    
    def sequenceEndFrame(self):

        return 0.0
    
    def sequenceFrameLength(self):

        return 0.0
    
    def setDisplayFlag(self, on):

        return None
    
    def isDisplayFlagSet(self):

        return True
    
    def setRenderFlag(self, on):

        return None
    
    def isRenderFlagSet(self):

        return True
    
    def setTemplateFlag(self, on):

        return None
    
    def isTemplateFlagSet(self):

        return True
    
    def setCompressFlag(self, on):

        return None
    
    def isCompressFlagSet(self):

        return True
    
    def bypass(self, on):

        return None
    
    def isBypassed(self):

        return True
    
    def hasMetaData(self, metadata_name):

        return True
    
    def getMetaDataInt(self, metadata_name, index=object):

        return 0
    
    def getMetaDataFloat(self, metadata_name, index=object):

        return 0.0
    
    def getMetaDataString(self, metadata_name):

        return ""
    
    def getMetaDataIntArray(self, metadata_name):

        return (0, )
    
    def getMetaDataFloatArray(self, metadata_name):

        return (0.0, )
    

class IndirectInput(NetworkItem, NetworkMovableItem):


    def outputs(self):

        return (Node, )
    
    def outputConnections(self):

        return (NodeConnection, )
    
    def input(self):

        return Node
    
    def inputOutputIndex(self):

        return 0
    
    def inputItem(self):

        return NetworkMovableItem
    
    def inputItemOutputIndex(self):

        return 0
    

class NetworkDot(NetworkItem, NetworkMovableItem, IndirectInput):


    def setPinned(self, pinned):

        return None
    
    def isPinned(self):

        return True
    
    def setInput(self, item_to_become_input, output_index=object):

        return None
    
    def setInput(self, input_index, item_to_become_input, output_index=object):

        return None
    
    def insertInput(self, input_index, item_to_become_input, output_index=object):

        return None
    
    def inputConnections(self):

        return (NodeConnection, )
    
    def destroy(self):

        return None
    

class NodeConnection(NetworkItem):


    def outputNode(self):

        return Node
    
    def outputItem(self):

        return NetworkMovableItem
    
    def inputNode(self):

        return Node
    
    def outputIndex(self):

        return 0
    
    def inputIndex(self):

        return 0
    
    def outputName(self):

        return ""
    
    def outputLabel(self):

        return ""
    
    def outputDataType(self):

        return ""
    
    def inputName(self):

        return ""
    
    def inputLabel(self):

        return ""
    
    def inputDataType(self):

        return ""
    
    def subnetIndirectInput(self):

        return SubnetIndirectInput
    
    def inputItem(self):

        return NetworkMovableItem
    
    def inputItemOutputIndex(self):

        return 0
    
    def isSelected(self):

        return True
    
    def setSelected(self, selected, clear_all_selected=True):

        return None
    

class NodeInfoTree():


    def name(self):

        return ""
    
    def infoType(self):

        return ""
    
    def branchOrder(self):

        return ("", )
    
    def branches(self):

        return {"": NodeInfoTree}
    
    def headings(self):

        return ("", )
    
    def rows(self):

        return (object, )
    

class NodeType():


    def name(self):

        return ""
    
    def nameComponents(self):

        return ("", )
    
    def nameWithCategory(self):

        return ""
    
    def namespaceOrder(self):

        return ("", )
    
    def description(self):

        return ""
    
    def instances(self):

        return (Node, )
    
    def category(self):

        return NodeTypeCategory
    
    def parmTemplateGroup(self):

        return ParmTemplateGroup
    
    def parmTemplates(self):

        return (ParmTemplate, )
    
    def definition(self):

        return HDADefinition
    
    def allInstalledDefinitions(self):

        return (HDADefinition, )
    
    def hdaModule(self):

        return HDAModule
    
    def aliases(self):

        return ("", )
    
    def addAlias(self, alias):

        return None
    
    def removeAlias(self, alias):

        return None
    
    def hidden(self):

        return True
    
    def setHidden(self, hidden):

        return None
    
    def deprecated(self):

        return True
    
    def deprecationInfo(self):

        return {"": ""}
    
    def minNumInputs(self):

        return 0
    
    def maxNumInputs(self):

        return 0
    
    def maxNumOutputs(self):

        return 0
    
    def hasPermanentUserDefaults(self):

        return True
    
    def hasUnorderedInputs(self):

        return True
    
    def isGenerator(self):

        return True
    
    def isManager(self, include_management_types=True):

        return True
    
    def icon(self):

        return ""
    
    def source(self):

        return EnumValue
    
    def sourcePath(self):

        return ""
    
    def sourceNetwork(self):

        return Node
    
    def uninstallFromPath(self):

        return None
    
    def isReadable(self):

        return True
    
    def isWritable(self):

        return True
    
    def areContentsViewable(self):

        return True
    
    def containedNodeTypes(self):

        return ("", )
    
    def childTypeCategory(self):

        return NodeTypeCategory
    
    def embeddedHelp(self):

        return ""
    
    def helpUrl(self):

        return ""
    
    def defaultHelpUrl(self):

        return ""
    
    def defaultColor(self):

        return Color
    
    def setDefaultColor(self, color):

        return None
    
    def defaultShape(self):

        return ""
    
    def setDefaultShape(self, shape):

        return None
    

class PopNetNode(NetworkItem, NetworkMovableItem, Node):


    def displayNode(self):

        return Node
    
    def renderNode(self):

        return Node
    

class PopNode(NetworkItem, NetworkMovableItem, Node):


    def bypass(self, on):

        return None
    
    def curPoint(self):

        return Point
    
    def displayNode(self):

        return Node
    
    def isBypassed(self):

        return True
    
    def isDisplayFlagSet(self):

        return True
    
    def isRenderFlagSet(self):

        return True
    
    def isTemplateFlagSet(self):

        return True
    
    def renderNode(self):

        return Node
    
    def setDisplayFlag(self, on):

        return None
    
    def setRenderFlag(self, on):

        return None
    
    def setTemplateFlag(self, on):

        return None
    

class SopNodeType(NodeType):


    def selectors(self, selector_indices=tuple()):

        return (Selector, )
    
    def addSelector(self, name, selector_type, prompt=object, primitive_types=tuple(), group_parm_name=None, group_type_parm_name=None, input_index=object, input_required=True, allow_dragging=True, empty_string_selects_all=True):

        return Selector
    

class SubnetIndirectInput(NetworkItem, NetworkMovableItem, IndirectInput):


    def number(self):

        return 0
    
    def input(self):

        return Node
    
    def inputConnections(self):

        return (NodeConnection, )
    

class VopNetNode(NetworkItem, NetworkMovableItem, Node):


    def definedType(self):

        return NodeType
    
    def shaderType(self):

        return EnumValue
    
    def vexContext(self):

        return VexContext
    

class NodeTypeCategory():


    def loadDSO(self, dso_path):

        return None
    
    def label(self):

        return ""
    
    def name(self):

        return ""
    
    def nodeTypes(self):

        return {"": NodeType}
    
    def nodeType(self, type_name):

        return NodeType
    
    def nodeVerbs(self):

        return {"": SopVerb}
    
    def nodeVerb(self, name):

        return SopVerb
    
    def viewerStates(self, viewer_type):

        return (ViewerState, )
    
    def hasSubNetworkType(self):

        return True
    
    def defaultColor(self):

        return Color
    
    def clearDefaultColors(self):

        return None
    
    def setDefaultColor(self, color):

        return None
    
    def defaultShape(self):

        return ""
    
    def clearDefaultShapes(self):

        return None
    
    def setDefaultShape(self, shape):

        return None
    
    def defaultWireStyle(self):

        return ""
    
    def setDefaultWireStyle(self, wirestyle):

        return None
    

class ObjNode(NetworkItem, NetworkMovableItem, Node):


    def origin(self):

        return Vector3
    
    def localTransform(self):

        return Matrix4
    
    def localTransformAtTime(self, time):

        return Matrix4
    
    def worldTransform(self):

        return Matrix4
    
    def worldTransformAtTime(self, time):

        return Matrix4
    
    def setWorldTransform(self, matrix, fail_on_locked_parms=True):

        return None
    
    def parmTransform(self):

        return Matrix4
    
    def setParmTransform(self, matrix, fail_on_locked_parms=True):

        return None
    
    def parentAndSubnetTransform(self):

        return Matrix4
    

class NetworkBox(NetworkItem, NetworkMovableItem):


    def addItem(self, item):

        return None
    
    def addNetworkBox(self, netbox):

        return None
    
    def addNode(self, node):

        return None
    
    def addStickyNote(self, stickynote):

        return None
    
    def addSubnetIndirectInput(self, indirect):

        return None
    
    def asCode(self, brief=True, recurse=True, save_box_contents=True, save_channels_only=True, save_creation_commands=True, save_keys_in_frames=True, save_parm_values_only=True, save_spare_parms=True, function_name=None):

        return ""
    
    def autoFit(self):

        return True
    
    def comment(self):

        return ""
    
    def destroy(self, destroy_contents=True):

        return None
    
    def fitAroundContents(self):

        return None
    
    def isMinimized(self):

        return True
    
    def items(self, recurse=True):

        return (NetworkMovableItem, )
    
    def minimizedSize(self):

        return Vector2
    
    def nodes(self, recurse=True):

        return (Node, )
    
    def networkBoxes(self, recurse=True):

        return (NetworkBox, )
    
    def removeAllItems(self):

        return None
    
    def removeAllNodes(self):

        return None
    
    def removeItem(self, item):

        return None
    
    def removeNetworkBox(self, netbox):

        return None
    
    def removeNode(self, node):

        return None
    
    def removeStickyNote(self, stickynote):

        return None
    
    def removeSubnetIndirectInput(self, indirect):

        return None
    
    def resize(self, vector2):

        return None
    
    def restoredSize(self):

        return Vector2
    
    def setAutoFit(self, auto_fit):

        return None
    
    def setBounds(self, bounds):

        return None
    
    def setComment(self, comment):

        return None
    
    def setMinimized(self, on):

        return None
    
    def setSize(self, size):

        return None
    
    def stickyNotes(self, recurse=True):

        return (StickyNote, )
    
    def subnetIndirectInputs(self, recurse=True):

        return (SubnetIndirectInput, )
    

class NodeBundle():


    def name(self):

        return ""
    
    def setName(self, name):

        return None
    
    def destroy(self):

        return None
    
    def pattern(self):

        return ""
    
    def setPattern(self, pattern_or_none):

        return None
    
    def findBestFilter(self):

        return EnumValue
    
    def filter(self):

        return EnumValue
    
    def setFilter(self, node_type_filter):

        return None
    
    def nodes(self):

        return (Node, )
    
    def containsNode(self, node):

        return True
    
    def addNode(self, node):

        return None
    
    def removeNode(self, node):

        return None
    
    def clear(self):

        return None
    
    def isSelected(self):

        return True
    
    def setSelected(self, on, clear_all_selected=True):

        return None
    
    def convertToNormalBundle(self):

        return None
    
    def convertToSmartBundle(self):

        return None
    

class NodeGroup():


    def name(self):

        return ""
    
    def parent(self):

        return Node
    
    def nodes(self):

        return (Node, )
    
    def addNode(self, node):

        return None
    
    def removeNode(self, node):

        return None
    
    def clear(self):

        return None
    
    def destroy(self):

        return None
    
    def asCode(self, save_creation_commands=True, function_name=None):

        return ""
    

class StickyNote(NetworkItem, NetworkMovableItem):


    def asCode(self, brief=True, recurse=True, save_box_contents=True, save_channels_only=True, save_creation_commands=True, save_keys_in_frames=True, save_parm_values_only=True, save_spare_parms=True, function_name=None):

        return ""
    
    def destroy(self):

        return None
    
    def drawBackground(self):

        return True
    
    def isMinimized(self):

        return True
    
    def minimizedSize(self):

        return Vector2
    
    def resize(self, vector2):

        return None
    
    def restoredSize(self):

        return Vector2
    
    def setBounds(self, bounds):

        return None
    
    def setMinimized(self, on):

        return None
    
    def setDrawBackground(self, on):

        return None
    
    def setSize(self, size):

        return None
    
    def setText(self, str):

        return None
    
    def setTextColor(self, color):

        return None
    
    def setTextSize(self, size):

        return None
    
    def text(self):

        return ""
    
    def textColor(self):

        return Color
    
    def textSize(self):

        return 0.0
    

class Parm():


    def alias(self):

        return ""
    
    def setAlias(self, alias_name):

        return None
    
    def isAutoscoped(self):

        return True
    
    def deleteAllKeyframes(self):

        return None
    
    def deleteKeyframeAtFrame(self, frame):

        return None
    
    def keyframes(self):

        return (BaseKeyframe, )
    
    def keyframesAfter(self, frame):

        return (BaseKeyframe, )
    
    def keyframesBefore(self, frame):

        return (BaseKeyframe, )
    
    def keyframeExtrapolation(self, before):

        return parmExtrapolate
    
    def keyframesInRange(self, start_frame, end_frame):

        return (BaseKeyframe, )
    
    def keyframesRefit(self, refit, refit_tol, refit_preserve_extremas, refit_bezier, resample, resample_rate, resample_tol, range, range_start, range_end, bake_chop):

        return None
    
    def isScoped(self):

        return True
    
    def setScope(self, on):

        return None
    
    def setAutoscope(self, on):

        return None
    
    def setKeyframe(self, keyframe):

        return None
    
    def setKeyframes(self, keyframes):

        return None
    
    def setKeyframeExtrapolation(self, before, extrapol):

        return None
    
    def setPending(self, value):

        return None
    

class ParmTemplate():


    def clone(self):

        return ParmTemplate
    
    def name(self):

        return ""
    
    def setName(self, name):

        return None
    
    def label(self):

        return ""
    
    def setLabel(self, label):

        return None
    
    def type(self):

        return EnumValue
    
    def dataType(self):

        return EnumValue
    
    def numComponents(self):

        return 0
    
    def setNumComponents(self, num_components):

        return 0
    
    def namingScheme(self):

        return EnumValue
    
    def setNamingScheme(self, naming_scheme):

        return None
    
    def look(self):

        return EnumValue
    
    def setLook(self, look):

        return None
    
    def help(self):

        return ""
    
    def setHelp(self, help):

        return None
    
    def isHidden(self):

        return True
    
    def hide(self, on):

        return None
    
    def isLabelHidden(self):

        return True
    
    def hideLabel(self, on):

        return None
    
    def joinsWithNext(self):

        return True
    
    def joinWithNext(self):

        return True
    
    def setJoinWithNext(self, on):

        return None
    
    def disableWhen(self):

        return ""
    
    def setDisableWhen(self, disable_when):

        return None
    
    def conditionals(self):

        return {EnumValue: ""}
    
    def setConditional(self, type, conditional):

        return None
    
    def tags(self):

        return {"": ""}
    
    def scriptCallback(self):

        return ""
    
    def setScriptCallback(self, script_callback):

        return None
    
    def scriptCallbackLanguage(self):

        return EnumValue
    
    def setScriptCallbackLanguage(self, script_callback_language):

        return None
    
    def setTags(self, tags):

        return None
    
    def asCode(self, function_name=None, variable_name=None):

        return ""
    

class ParmTuple():


    def __getitem__(self, index):

        return Parm
    
    def __len__(self):

        return 0
    

class ButtonParmTemplate(ParmTemplate):


    def __init__(self, name, label, disable_when=None, is_hidden=True, is_label_hidden=True, join_with_next=True, help=None, script_callback=None, script_callback_language=object, tags={}):

        pass
    

class DataParmTemplate(ParmTemplate):


    def __init__(self, name, label, num_components, look=object, naming_scheme=object, disable_when=None, is_hidden=True, is_label_hidden=True, join_with_next=True, help=None, script_callback=None, script_callback_language=object, tags={}, default_expression=tuple(), default_expression_language=tuple()):

        pass
    
    def defaultExpression(self):

        return ("", )
    
    def dataParmType(self):

        return EnumValue
    
    def setDataParmType(self, data_parm_type):

        return None
    
    def setDefaultExpression(self, default_expression):

        return None
    
    def defaultExpressionLanguage(self):

        return (scriptLanguage, )
    
    def setDefaultExpressionLanguage(self, default_expression_language):

        return None
    

class FloatParmTemplate(ParmTemplate):


    def __init__(self, name, label, num_components, default_value=tuple(), min=object, max=object, min_is_strict=True, max_is_strict=True, look=object, naming_scheme=object, disable_when=None, is_hidden=True, is_label_hidden=True, join_with_next=True, help=None, script_callback=None, script_callback_language=object, tags={}, default_expression=tuple(), default_expression_language=tuple()):

        pass
    
    def defaultValue(self):

        return (0.0, )
    
    def setDefaultValue(self, default_value):

        return None
    
    def defaultExpression(self):

        return ("", )
    
    def setDefaultExpression(self, default_expression):

        return None
    
    def defaultExpressionLanguage(self):

        return (scriptLanguage, )
    
    def setDefaultExpressionLanguage(self, default_expression_language):

        return None
    
    def minValue(self):

        return 0.0
    
    def setMinValue(self, min_value):

        return None
    
    def maxValue(self):

        return 0.0
    
    def setMaxValue(self, max_value):

        return None
    
    def minIsStrict(self):

        return True
    
    def setMinIsStrict(self, on):

        return None
    
    def maxIsStrict(self):

        return True
    
    def setMaxIsStrict(self, on):

        return None
    

class FolderParmTemplate(ParmTemplate):


    def __init__(self, name, label, parm_templates=tuple(), folder_type=object, is_hidden=True, ends_tab_group=True, tags={}):

        pass
    
    def parmTemplates(self):

        return (ParmTemplate, )
    
    def addParmTemplate(self, parm_template):

        return None
    
    def setParmTemplates(self, parm_templates):

        return None
    
    def folderType(self):

        return EnumValue
    
    def setFolderType(self, folder_type):

        return None
    
    def isActualFolder(self):

        return True
    
    def defaultValue(self):

        return 0
    
    def setDefaultValue(self, default_value):

        return None
    
    def endsTabGroup(self):

        return True
    

class FolderSetParmTemplate(ParmTemplate):


    def __init__(self, name, folder_names, folder_type=object, tags={}):

        pass
    
    def folderNames(self):

        return ("", )
    
    def setFolderNames(self, folder_names):

        return None
    
    def folderType(self):

        return EnumValue
    
    def setFolderType(self, folder_type):

        return None
    
    def folderStyle(self):

        return EnumValue
    

class IntParmTemplate(ParmTemplate):


    def __init__(self, name, label, num_components, default_value=tuple(), min=object, max=object, min_is_strict=True, max_is_strict=True, naming_scheme=object, menu_items=tuple(), menu_labels=tuple(), icon_names=tuple(), item_generator_script=None, item_generator_script_language=None, menu_type=object, disable_when=None, is_hidden=True, is_label_hidden=True, join_with_next=True, help=None, script_callback=None, script_callback_language=object, tags={}, default_expression=tuple(), default_expression_language=tuple()):

        pass
    
    def defaultValue(self):

        return (0, )
    
    def setDefaultValue(self, default_value):

        return None
    
    def defaultExpression(self):

        return ("", )
    
    def setDefaultExpression(self, default_expression):

        return None
    
    def defaultExpressionLanguage(self):

        return (scriptLanguage, )
    
    def setDefaultExpressionLanguage(self, default_expression_language):

        return None
    
    def minValue(self):

        return 0
    
    def setMinValue(self, min_value):

        return None
    
    def maxValue(self):

        return 0
    
    def setMaxValue(self, max_value):

        return None
    
    def minIsStrict(self):

        return True
    
    def setMinIsStrict(self, on):

        return None
    
    def maxIsStrict(self):

        return True
    
    def setMaxIsStrict(self, on):

        return None
    
    def menuItems(self):

        return ("", )
    
    def setMenuItems(self, menu_items):

        return None
    
    def menuLabels(self):

        return ("", )
    
    def menuLabels(self):

        return ("", )
    
    def iconNames(self):

        return ("", )
    
    def setIconNames(self, icon_names):

        return None
    
    def itemGeneratorScript(self):

        return ""
    
    def setItemGeneratorScript(self, item_generator_script):

        return None
    
    def itemGeneratorScriptLanguage(self):

        return EnumValue
    
    def setItemGeneratorScriptLanguage(self, language):

        return None
    
    def menuType(self):

        return EnumValue
    
    def setMenuType(self, menu_type):

        return None
    

class LabelParmTemplate(ParmTemplate):


    def __init__(self, name, label, column_labels=tuple(), is_hidden=True, is_label_hidden=True, join_with_next=True, help=None, tags={}):

        pass
    
    def columnLabels(self):

        return ("", )
    
    def setColumnLabels(self, column_labels):

        return None
    

class MenuParmTemplate(ParmTemplate):


    def __init__(self, name, label, menu_items, menu_labels=tuple(), default_value=object, icon_names=tuple(), item_generator_script=object, item_generator_script_language=None, disable_when=None, menu_type=object, is_hidden=True, is_label_hidden=True, join_with_next=True, help=None, script_callback=None, script_callback_language=object, tags={}, default_expression=object, default_expression_language=object, store_default_value_as_string=True):

        pass
    
    def menuItems(self):

        return ("", )
    
    def setMenuItems(self, menu_items):

        return None
    
    def menuLabels(self):

        return ("", )
    
    def setMenuLabels(self, menu_labels):

        return None
    
    def defaultValue(self):

        return 0
    
    def setDefaultValue(self, default_value):

        return None
    
    def defaultExpression(self):

        return ""
    
    def setDefaultExpression(self, default_expression):

        return None
    
    def defaultExpressionLanguage(self):

        return (scriptLanguage, )
    
    def setDefaultExpressionLanguage(self, default_expression_language):

        return None
    
    def defaultValueAsString(self):

        return ""
    
    def iconNames(self):

        return ("", )
    
    def setIconNames(self, icon_names):

        return None
    
    def itemGeneratorScript(self):

        return ""
    
    def setItemGeneratorScript(self, item_generator_script):

        return None
    
    def itemGeneratorScriptLanguage(self):

        return EnumValue
    
    def setItemGeneratorScriptLanguage(self, language):

        return None
    
    def menuType(self):

        return EnumValue
    
    def setMenuType(self, menu_type):

        return None
    

class ParmTemplateGroup():


    def __init__(self, parm_templates=tuple()):

        pass
    
    def find(self, name):

        return ParmTemplate
    
    def findIndices(self, name_or_parm_template):

        return (0, )
    
    def findFolder(self, label_or_labels):

        return FolderParmTemplate
    
    def findIndicesForFolder(self, label_or_labels):

        return (0, )
    
    def entryAtIndices(self, indices):

        return ParmTemplate
    
    def containingFolder(self, name_or_parm_template):

        return FolderParmTemplate
    
    def containingFolderIndices(self, name_or_parm_template_or_indices):

        return (0, )
    
    def entries(self):

        return (ParmTemplate, )
    
    def parmTemplates(self):

        return (ParmTemplate, )
    
    def entriesWithoutFolders(self):

        return (ParmTemplate, )
    
    def replace(self, name_or_parm_template_or_indices, parm_template):

        return None
    
    def insertBefore(self, name_or_parm_template_or_indices, parm_template):

        return None
    
    def insertAfter(self, name_or_parm_template_or_indices, parm_template):

        return None
    
    def append(self, parm_template):

        return None
    
    def addParmTemplate(self, parm_template):

        return None
    
    def appendToFolder(self, label_or_labels_or_parm_template_or_indices, parm_template):

        return None
    
    def remove(self, name_or_parm_template_or_indices):

        return None
    
    def hide(self, name_or_parm_template_or_indices, on):

        return None
    
    def hideFolder(self, label_or_labels, on):

        return None
    
    def isHidden(self, name_or_parm_template_or_indices):

        return True
    
    def isFolderHidden(self, label_or_labels):

        return True
    
    def clear(self):

        return None
    
    def asDialogScript(self, rename_conflicting_parms=True, full_info=True):

        return None
    
    def setToDialogScript(self, dialog_script):

        return None
    
    def asCode(self, function_name=None, variable_name=None):

        return None
    
    def sourceNode(self):

        return Node
    
    def sourceNodeType(self):

        return NodeType
    

class RampParmTemplate(ParmTemplate):


    def __init__(self, name, label, ramp_parm_type, default_value=object, default_basis=None, show_controls=True, color_type=None, disable_when=None, is_hidden=True, help=None, script_callback=None, script_callback_language=object, tags={}, default_expression_language=object):

        pass
    
    def defaultValue(self):

        return 0
    
    def setDefaultValue(self, default_value):

        return None
    
    def defaultExpression(self):

        return ""
    
    def setDefaultExpression(self, default_expression):

        return None
    
    def defaultExpressionLanguage(self):

        return (scriptLanguage, )
    
    def setDefaultExpressionLanguage(self, default_expression_language):

        return None
    
    def showsControls(self):

        return True
    
    def setShowsControls(self, on):

        return None
    
    def parmType(self):

        return EnumValue
    
    def setParmType(self, ramp_parm_type):

        return None
    
    def defaultBasis(self):

        return EnumValue
    
    def setDefaultBasis(self, ramp_basis):

        return None
    
    def colorType(self):

        return EnumValue
    
    def setColorType(self, color_type):

        return None
    

class SeparatorParmTemplate(ParmTemplate):


    def __init__(self, name, is_hidden=True, tags={}):

        pass
    

class StringParmTemplate(ParmTemplate):


    def __init__(self, name, label, num_components, default_value=tuple(), naming_scheme=object, string_type=object, file_type=object, menu_items=tuple(), menu_labels=tuple(), icon_names=tuple(), item_generator_script=None, item_generator_script_language=None, menu_type=object, disable_when=None, is_hidden=True, is_label_hidden=True, join_with_next=True, help=None, script_callback=None, script_callback_language=object, tags={}, default_expression=tuple(), default_expression_language=tuple()):

        pass
    
    def defaultValue(self):

        return ("", )
    
    def setDefaultValue(self, default_value):

        return None
    
    def defaultExpression(self):

        return ("", )
    
    def setDefaultExpression(self, default_expression):

        return None
    
    def defaultExpressionLanguage(self):

        return (scriptLanguage, )
    
    def setDefaultExpressionLanguage(self, default_expression_language):

        return None
    
    def stringType(self):

        return EnumValue
    
    def setStringType(self, string_type):

        return None
    
    def fileType(self):

        return EnumValue
    
    def setFileType(self, file_type):

        return None
    
    def menuItems(self):

        return ("", )
    
    def setMenuItems(self, menu_items):

        return None
    
    def menuLabels(self):

        return ("", )
    
    def menuLabels(self):

        return ("", )
    
    def iconNames(self):

        return ("", )
    
    def setIconNames(self, icon_names):

        return None
    
    def itemGeneratorScript(self):

        return ""
    
    def setItemGeneratorScript(self, item_generator_script):

        return None
    
    def itemGeneratorScriptLanguage(self):

        return EnumValue
    
    def setItemGeneratorScriptLanguage(self, language):

        return None
    
    def menuType(self):

        return EnumValue
    
    def setMenuType(self, menu_type):

        return None
    

class ToggleParmTemplate(ParmTemplate):


    def __init__(self, name, label, default_value=True, disable_when=None, is_hidden=True, is_label_hidden=True, join_with_next=True, help=None, script_callback=None, script_callback_language=object, tags={}, default_expression=object, default_expression_language=object):

        pass
    
    def defaultValue(self):

        return True
    
    def setDefaultValue(self, default_value):

        return None
    
    def defaultExpression(self):

        return ""
    
    def setDefaultExpression(self, default_expression):

        return None
    
    def defaultExpressionLanguage(self):

        return (scriptLanguage, )
    
    def setDefaultExpressionLanguage(self, default_expression_language):

        return None
    

class PerfMonEvent():


    def id(self):

        return 0
    
    def isAutoNestEnabled(self):

        return True
    
    def isRunning(self):

        return True
    
    def isTiming(self):

        return True
    
    def name(self):

        return ""
    
    def object(self):

        return ""
    
    def startTime(self):

        return 0.0
    
    def stop(self):

        return None
    

class PerfMonProfile():


    def cancel(self):

        return None
    
    def exportAsCSV(self, file_path):

        return None
    
    def id(self):

        return 0
    
    def isActive(self):

        return True
    
    def isRecordingCookStats(self):

        return True
    
    def isRecordingDrawStats(self):

        return True
    
    def isRecordingErrors(self):

        return True
    
    def isRecordingFrameStats(self):

        return True
    
    def isRecordingGPUDrawStats(self):

        return True
    
    def isRecordingRenderStats(self):

        return True
    
    def isRecordingScriptStats(self):

        return True
    
    def isRecordingSolveStats(self):

        return True
    
    def isRecordingThreadStats(self):

        return True
    
    def isRecordingViewportStats(self):

        return True
    
    def isPaused(self):

        return True
    
    def pause(self):

        return None
    
    def resume(self):

        return None
    
    def save(self, file_path):

        return None
    
    def stats(self):

        return None
    
    def stop(self):

        return None
    
    def title(self):

        return ""
    

class PerfMonRecordOptions():


    def recordCookStats(self):

        return True
    
    def recordDrawStats(self):

        return True
    
    def recordErrors(self):

        return True
    
    def recordFrameStats(self):

        return True
    
    def recordGPUDrawStats(self):

        return True
    
    def recordMemoryStats(self):

        return True
    
    def recordRenderStats(self):

        return True
    
    def recordScriptStats(self):

        return True
    
    def recordSolveStats(self):

        return True
    
    def recordThreadStats(self):

        return True
    
    def recordViewportStats(self):

        return True
    
    def setRecordCookStats(self, record):

        return None
    
    def setRecordDrawStats(self, record):

        return None
    
    def setRecordErrors(self, record):

        return None
    
    def setRecordFrameStats(self, record):

        return None
    
    def setRecordGPUDrawStats(self, record):

        return None
    
    def setRecordMemoryStats(self, record):

        return None
    
    def setRecordRenderStats(self, record):

        return None
    
    def setRecordScriptStats(self, record):

        return None
    
    def setRecordSolveStats(self, record):

        return None
    
    def setRecordThreadStats(self, record):

        return None
    
    def setRecordViewportStats(self, record):

        return None
    

class RadialSubmenu(RadialItem):


    def label(self):

        return ""
    
    def setLabel(self):

        return None
    
    def item(self, radialItemLocation):

        return RadialItem
    
    def items(self):

        return {radialItemLocation: RadialItem}
    
    def createSubmenu(self, radialItemLocation, label=None):

        return RadialSubmenu
    
    def createScriptItem(self, radialItemLocation, label=None, icon=None, check=None, script=None):

        return RadialScriptItem
    

class RadialItem():


    def destroy(self):

        return None
    
    def type(self):

        return radialItemType
    

class RadialMenu(RadialItem, RadialSubmenu):


    def name(self):

        return ""
    
    def categories(self):

        return ""
    
    def setCategories(self, categories):

        return None
    
    def sourceFile(self):

        return ""
    
    def save(self, filename):

        return None
    

class RadialScriptItem(RadialItem):


    def label(self):

        return ""
    
    def setLabel(self):

        return None
    
    def icon(self):

        return ""
    
    def setIcon(self):

        return None
    
    def check(self):

        return ""
    
    def setCheck(self):

        return None
    
    def script(self):

        return ""
    
    def setScript(self):

        return None
    

class RopNode(NetworkItem, NetworkMovableItem, Node):


    def bypass(self, on):

        return None
    
    def inputDependencies(self):

        return (RopNode, ((0.0,),))
    
    def isBypassed(self):

        return True
    
    def isLocked(self):

        return True
    
    def setLocked(self, on):

        return None
    
    def render(self, frame_range=tuple(), res=tuple(), output_file=None, output_format=None, to_flipbook=True, quality=object, ignore_inputs=True, method=RopByRop, ignore_bypass_flags=True, ignore_lock_flags=True, verbose=True, output_progress=True):

        return None
    
    def setLocked(self, on):

        return None
    

class ShellIO():


    def addDataForReading(self, data):

        return None
    
    def addEOFForReading(self):

        return None
    
    def addCloseCallback(self, callback):

        return None
    
    def closeCallbacks(self):

        return (object, )
    
    def getAndClearWrittenData(self):

        return ""
    
    def interruptShellThread(self):

        return None
    
    def isatty(self):

        return True
    
    def isWaitingForCommand(self):

        return True
    
    def readline(self, size=object):

        return ""
    
    def removeCloseCallback(self, callback):

        return None
    
    def setIsWaitingForCommand(self, on):

        return None
    
    def write(self, data):

        return None
    

class Gallery():


    def createEntry(self, entry_name, node=None):

        return GalleryEntry
    
    def deleteEntry(self, entry_name):

        return None
    
    def galleryEntries(self, name_pattern=None, label_pattern=None, keyword_pattern=None, category=None, node_type=None):

        return (GalleryEntry, )
    

class GalleryEntry():


    def allowIconRegeneration(self):

        return True
    
    def applyToNode(self, node):

        return None
    
    def bestNodeType(self):

        return NodeType
    
    def canApplyToNode(self, node):

        return True
    
    def canCreateChildNode(self, parent):

        return True
    
    def categories(self):

        return ("", )
    
    def createChildNode(self, parent):

        return Node
    
    def description(self):

        return ""
    
    def helpURL(self):

        return ""
    
    def icon(self):

        return ""
    
    def keywords(self):

        return ("", )
    
    def label(self):

        return ""
    
    def name(self):

        return ""
    
    def nodeTypeCategory(self):

        return NodeTypeCategory
    
    def nodeTypeNames(self):

        return ("", )
    
    def requiredHDAFile(self):

        return ""
    
    def script(self):

        return ""
    
    def setAllowIconRegeneration(self, allow):

        return None
    
    def setCategories(self, categories):

        return None
    
    def setContentsFromNode(self, node):

        return None
    
    def setDescription(self, description):

        return None
    
    def setEqual(self, entry):

        return None
    
    def setHelpURL(self, helpurl):

        return None
    
    def setIcon(self, icon):

        return None
    
    def setKeywords(self, keywords):

        return None
    
    def setLabel(self, label):

        return None
    
    def setName(self, name):

        return None
    
    def setNodeTypeCategory(self, category):

        return None
    
    def setNodeTypeNames(self, nodetypes):

        return None
    
    def setRequiredHDAFile(self, hda_file):

        return None
    
    def setScript(self, script):

        return None
    
    def setScriptFromNode(self, node):

        return None
    

class ShopNode(NetworkItem, NetworkMovableItem, Node):


    def definingVopNetNode(self):

        return VopNetNode
    
    def coshaderNodes(self, parm_name):

        return (ShopNode, )
    
    def shaderName(self, as_otl_path=True, shader_type_name=None):

        return ""
    
    def shaderString(self, render_type=None):

        return ""
    
    def shaderCode(self, shader_type=object):

        return ""
    
    def shaderType(self):

        return EnumValue
    
    def supportedRenderers(self):

        return ("", )
    

class ShelfElement():


    def setFilePath(self, file_path):

        return None
    
    def filePath(self):

        return ""
    
    def setName(self, name):

        return None
    
    def name(self):

        return ""
    
    def setLabel(self, label):

        return None
    
    def label(self):

        return ""
    
    def setReadOnly(self, on):

        return None
    
    def isReadOnly(self):

        return True
    

class StyleSheet():


    def __init__(self):

        pass
    
    def __init__(self, json_text):

        pass
    
    def clone(self):

        return StyleSheet
    
    def cloneWithObject(self, object):

        return StyleSheet
    
    def cloneWithPrim(self, prim):

        return StyleSheet
    
    def cloneWithShape(self, shape_name, prim):

        return StyleSheet
    
    def cloneWithAddedStyleSheet(self, stylesheet, target):

        return StyleSheet
    
    def errors(self):

        return ""
    
    def asJSON(self):

        return ""
    

class Shelf(ShelfElement):


    def destroy(self):

        return None
    
    def setTools(self, tools):

        return None
    
    def tools(self):

        return (Tool, )
    

class ShelfDock():


    def iconsize(self):

        return (0, 0,)
    
    def shelfSets(self):

        return (ShelfSet, )
    
    def show(self, on):

        return None
    

class ShelfSet(ShelfElement):


    def destroy(self):

        return None
    
    def setShelves(self, shelves):

        return None
    
    def shelves(self):

        return (Shelf, )
    

class Tool(ShelfElement):


    def destroy(self):

        return None
    
    def setData(self, script=object, language=object, icon=object, help=object, help_url=object, network_categories=tuple(), viewer_categories=tuple(), cop_viewer_categories=tuple(), network_op_type=object, viewer_op_type=object, locations=tuple()):

        return None
    

class PaneTab():


    def name(self):

        return ""
    
    def setName(self, name):

        return None
    
    def type(self):

        return EnumValue
    
    def setType(self, type):

        return PaneTab
    
    def close(self):

        return None
    
    def pane(self):

        return Pane
    
    def floatingPanel(self):

        return FloatingPanel
    
    def isCurrentTab(self):

        return True
    
    def setIsCurrentTab(self):

        return None
    
    def isFloating(self):

        return True
    
    def clone(self):

        return PaneTab
    
    def linkGroup(self):

        return EnumValue
    
    def setLinkGroup(self, group):

        return None
    
    def isPin(self):

        return True
    
    def setPin(self, pin):

        return None
    

class Take():


    def isCurrent(self):

        return True
    
    def name(self):

        return None
    
    def setName(self, name):

        return None
    
    def addChildTake(self, name):

        return Take
    
    def addNodeDisplayFlag(self, node):

        return None
    
    def removeNodeDisplayFlag(self, node):

        return None
    
    def addNodeBypassFlag(self, node):

        return None
    
    def removeNodeBypassFlag(self, node):

        return None
    
    def addNodeRenderFlag(self, node):

        return None
    
    def removeNodeRenderFlag(self, node):

        return None
    
    def parmTuples(self):

        return (ParmTuple, )
    
    def hasParmTuple(self, parm_tuple):

        return True
    
    def addParmTuple(self, parm_tuple):

        return None
    
    def removeParmTuple(self, parm_tuple):

        return None
    
    def addParmTuplesFromTake(self, take, overwrite_existing=True):

        return None
    
    def addParmTuplesFromNode(self, node):

        return None
    
    def removeParmTuplesFromNode(self, node):

        return None
    
    def children(self):

        return (Take, )
    
    def destroy(self, recurse=True):

        return None
    
    def parent(self):

        return Take
    
    def path(self):

        return ""
    
    def insertTakeAbove(self, name):

        return Take
    
    def moveUnderTake(self, take):

        return None
    
    def saveToFile(self, filename, recurse=True):

        return None
    
    def loadChildTakeFromFile(self, filename):

        return (Take, )
    

class DataTree(PaneTab):


    def treeTypes(self):

        return ("", )
    
    def treeType(self):

        return ""
    
    def setTreeType(self, tree_type):

        return True
    
    def currentPath(self):

        return ""
    
    def clearCurrentPath(self):

        return ""
    
    def setCurrentPath(self, path, multi=True, index=object):

        return None
    
    def setCurrentPaths(self, paths, expand):

        return None
    
    def setCurrentNodeExpanded(self, expanded):

        return None
    
    def setTreeExpanded(self, expanded):

        return None
    

class Desktop():


    def name(self):

        return ""
    
    def setAsCurrent(self):

        return None
    
    def panes(self):

        return (Pane, )
    
    def floatingPanels(self):

        return (FloatingPanel, )
    
    def paneTabs(self):

        return (PaneTab, )
    
    def currentPaneTabs(self):

        return (PaneTab, )
    
    def floatingPaneTabs(self):

        return (PaneTab, )
    
    def paneTabOfType(self, type, index=object):

        return PaneTab
    
    def findPaneTab(self, name):

        return PaneTab
    
    def createFloatingPaneTab(self, pane_tab_type, position=tuple(), size=tuple(), python_panel_interface=None):

        return PaneTab
    
    def createFloatingPanel(self, pane_tab_type, position=tuple(), size=tuple(), python_panel_interface=None):

        return FloatingPanel
    
    def shelfDock(self):

        return ShelfDock
    
    def displayHelp(self, node_type):

        return None
    
    def displayHelpPath(self, help_path):

        return None
    
    def displayHelpPyPanel(self, interface_name):

        return None
    
    def displaySideHelp(self, show=True):

        return PaneTab
    
    def paneUnderCursor(self):

        return None
    
    def paneTabUnderCursor(self):

        return None
    

class Dialog():


    def addCallback(self, name, callback):

        return None
    
    def callbacks(self, name):

        return (object, )
    
    def destroy(self):

        return None
    
    def enableValue(self, name, onoff):

        return None
    
    def menuItems(self, name):

        return ("", )
    
    def removeCallback(self, name, callback):

        return None
    
    def setMenuItems(self, name, items):

        return None
    
    def setValue(self, name, value):

        return None
    
    def value(self, name):

        return None
    
    def waitForValueToChangeTo(self, name, new_value):

        return None
    

class FloatingPanel():


    def name(self):

        return ""
    
    def setName(self, name):

        return None
    
    def panes(self):

        return (Pane, )
    
    def paneTabs(self):

        return (PaneTab, )
    
    def paneTabOfType(self, type, index=object):

        return PaneTab
    
    def findPaneTab(self, name):

        return PaneTab
    
    def close(self):

        return None
    
    def isAttachedToDesktop(self):

        return True
    
    def attachToDesktop(self, on):

        return None
    
    def containsPlaybar(self):

        return True
    
    def setContainsPlaybar(self, on):

        return None
    
    def containsShelf(self):

        return True
    
    def setContainsShelf(self, on):

        return None
    
    def containsStatusBar(self):

        return True
    
    def setContainsStatusBar(self, on):

        return None
    
    def containsMenuBar(self):

        return True
    
    def setContainsMenuBar(self, on):

        return None
    
    def isFullscreen(self):

        return True
    
    def setIsFullscreen(self, on):

        return None
    
    def position(self):

        return Vector2
    
    def setPosition(self, position):

        return None
    
    def size(self):

        return Vector2
    
    def setSize(self, size):

        return None
    

class HelpBrowser(PaneTab):


    def displayHelp(self, node_type):

        return None
    
    def displayHelpPath(self, help_path):

        return None
    
    def displayHelpPyPanel(self, interface_name):

        return None
    
    def homePage(self):

        return ""
    
    def setHomePage(self, home_page):

        return None
    
    def setUrl(self, url):

        return None
    
    def showUI(self, show):

        return None
    
    def url(self):

        return ""
    

class IPRViewer(Pane):


    def isPaused(self):

        return True
    
    def isRendering(self):

        return True
    
    def isActive(self):

        return True
    
    def killRender(self):

        return None
    
    def pauseRender(self):

        return None
    
    def resumeRender(self):

        return None
    
    def startRender(self):

        return None
    
    def isPreviewOn(self):

        return True
    
    def setPreview(self, on):

        return None
    
    def isAutoSaveOn(self):

        return True
    
    def setAutoSave(self, on):

        return None
    
    def autoSavePath(self):

        return ""
    
    def setAutoSavePath(self, path):

        return None
    
    def autoSaveTime(self):

        return 0.0
    
    def setAutoSaveTime(self, float):

        return None
    
    def isAutoUpdateOn(self):

        return True
    
    def setAutoUpdate(self, on):

        return None
    
    def delay(self):

        return 0.0
    
    def setDelay(self, time):

        return None
    
    def updateTime(self):

        return 0.0
    
    def setUpdateTime(self, time):

        return None
    
    def lastClickLocation(self):

        return (0, 0,)
    
    def ropNode(self):

        return RopNode
    
    def setRopNode(self, rop_node):

        return None
    
    def imageResolution(self):

        return (0, 0,)
    
    def cropRegion(self):

        return (0.0, 0.0, 0.0, 0.0,)
    
    def planes(self):

        return ("", )
    
    def pixel(self, plane_name, x, y):

        return (0.0, )
    
    def pixels(self, plane_name):

        return (object, )
    
    def evaluatedStyleSheetJSON(self, x, y):

        return ""
    
    def evaluatedStyleSheetPaths(self, x, y):

        return ("", )
    
    def saveFrame(self, file_path, snapshot=object, xres=object, yres=object, color=object, alpha=object, scope=object, lut=object, gamma=object, convert=True):

        return True
    
    def objectNode(self, x, y):

        return ObjNode
    
    def prim(self, x, y):

        return Prim
    
    def materialNode(self, x, y):

        return ShopNode
    

class NetworkAnimValue():


    def __init__(self, value):

        pass
    
    def __init__(self, duration, value_start, value_end):

        pass
    

class NetworkEditor(Pane, PathBasedPaneTab):


    def cursorPosition(self, confine_to_view=True):

        return Vector2
    
    def isShowingConnectors(self):

        return True
    
    def isPosInside(self, pos):

        return True
    
    def setCursorPosition(self, pos):

        return None
    
    def screenBounds(self):

        return BoundingRect
    
    def visibleBounds(self):

        return BoundingRect
    
    def setVisibleBounds(self, bounds, transition_time=object, max_scale=object, set_center_when_scale_rejected=True):

        return None
    
    def setLocatingEnabled(self, enabled):

        return None
    
    def locatingEnabled(self):

        return True
    
    def lengthToScreen(self, len):

        return 0.0
    
    def lengthFromScreen(self, len):

        return 0.0
    
    def sizeToScreen(self, size):

        return Vector2
    
    def sizeFromScreen(self, size):

        return Vector2
    
    def posToScreen(self, pos):

        return Vector2
    
    def posFromScreen(self, pos):

        return Vector2
    
    def overviewPosToScreen(self, pos):

        return Vector2
    
    def overviewPosFromScreen(self, pos):

        return Vector2
    
    def overviewVisible(self):

        return True
    
    def overviewVisibleIfAutomatic(self):

        return True
    

class NetworkFootprint():


    def __init__(self, condition, color, ring, use_minimum_size):

        pass
    

class NetworkImage():


    def __init__(self, path, rect):

        pass
    
    def path(self):

        return ""
    
    def setPath(self, path):

        return None
    
    def relativeToPath(self):

        return ""
    
    def setRelativeToPath(self, path):

        return None
    
    def rect(self):

        return BoundingRect
    
    def setRect(self, rect):

        return None
    
    def brightness(self):

        return 0.0
    
    def setBrightness(self, brightness):

        return None
    

class NetworkShape():

    pass

class NetworkShapeBox():


    def __init__(self, rect, color=Color, alpha=object, fill=True, screen_space=True, smooth=True):

        pass
    

class NetworkShapeConnection():


    def __init__(self, input_pos, input_dir, output_pos, output_dir, color=Color, alpha=object, fade_factor=object, smooth=True, dashed=True):

        pass
    

class NetworkShapeLine():


    def __init__(self, start, end, color=Color, alpha=object, width=object, screen_space=True, smooth=True, dashed=True):

        pass
    

class NetworkShapeNodeShape():


    def __init__(self, rect, shape, color=Color, alpha=object, fill=True, screen_space=True, smooth=True):

        pass
    

class PerformanceMonitor(PaneTab):


    def enableLiveUpdates(self, on):

        return None
    
    def isLiveUpdatesEnabled(self):

        return True
    
    def isRecording(self):

        return True
    
    def isSamplingCookStats(self):

        return True
    
    def isSamplingErrors(self):

        return True
    
    def isSamplingFrameStats(self):

        return True
    
    def isSamplingObjectDrawStats(self):

        return True
    
    def isSamplingObjectGPUDrawStats(self):

        return True
    
    def isSamplingRenderStats(self):

        return True
    
    def isSamplingScriptStats(self):

        return True
    
    def isSamplingSolveStats(self):

        return True
    
    def isSamplingThreadStats(self):

        return True
    
    def isSamplingViewportStats(self):

        return True
    
    def objectView(self):

        return EnumValue
    
    def sampleCookStats(self, on):

        return None
    
    def sampleErrors(self, on):

        return None
    
    def sampleFrameStats(self, on):

        return None
    
    def sampleObjectDrawStats(self, on):

        return None
    
    def sampleObjectGPUDrawStats(self, on):

        return None
    
    def sampleRenderStats(self, on):

        return None
    
    def sampleScriptStats(self, on):

        return None
    
    def sampleSolveStats(self, on):

        return None
    
    def sampleThreadStats(self, on):

        return None
    
    def sampleViewportStats(self, on):

        return None
    
    def setObjectView(self, view):

        return None
    
    def setTimeFormat(self, format):

        return None
    
    def startRecording(self):

        return None
    
    def stopRecording(self):

        return None
    
    def timeFormat(self):

        return EnumValue
    

class PythonPanel(PaneTab):


    def isToolbarExpanded(self):

        return True
    
    def isToolbarShown(self):

        return True
    
    def activeInterface(self):

        return PythonPanelInterface
    
    def activeInterfaceRootWidget(self):

        return QWidget
    
    def setActiveInterface(self, interface):

        return None
    
    def showToolbar(self, show):

        return None
    
    def expandToolbar(self, expand):

        return None
    

class PythonPanelInterface():


    def id(self):

        return 0
    
    def setId(self, id):

        return None
    
    def name(self):

        return ""
    
    def setName(self, name):

        return None
    
    def label(self):

        return ""
    
    def setLabel(self, label):

        return None
    
    def icon(self):

        return ""
    
    def setIcon(self, icon):

        return None
    
    def script(self):

        return ""
    
    def setScript(self, script):

        return None
    
    def filePath(self):

        return ""
    
    def setFilePath(self, script):

        return None
    

class BoundingBox():


    def __init__(self, xmin=object, ymin=object, zmin=object, xmax=object, ymax=object, zmax=object):

        pass
    
    def setTo(self, bounds_sequence):

        return None
    
    def minvec(self):

        return Vector3
    
    def maxvec(self):

        return Vector3
    
    def sizevec(self):

        return Vector3
    
    def center(self):

        return Vector3
    
    def enlargeToContain(self, point_or_bbox):

        return None
    
    def contains(self, point):

        return None
    
    def isAlmostEqual(self, bbox, tolerance=object):

        return True
    
    def isValid(self):

        return True
    
    def __mul__(self, matrix4):

        return BoundingBox
    

class BoundingRect():


    def __init__(self, x1, y1, x2, y2):

        pass
    
    def __init__(self, p1, p2):

        pass
    
    def setTo(self, bounds_sequence):

        return None
    
    def isValid(self):

        return True
    
    def isAlmostEqual(self, rect, tolerance=object):

        return True
    
    def min(self):

        return Vector2
    
    def max(self):

        return Vector2
    
    def size(self):

        return Vector2
    
    def center(self):

        return Vector2
    
    def contains(self, point):

        return True
    
    def contains(self, rect):

        return True
    
    def intersects(self, point0, point1):

        return True
    
    def intersects(self, point0, point1, point2):

        return True
    
    def intersects(self, rect):

        return True
    
    def closestPoint(self, point):

        return Vector2
    
    def getOffsetToAvoid(self, bounds, direction=None):

        return Vector2
    
    def translate(self, offset):

        return None
    
    def scale(self, scale):

        return None
    
    def expand(self, offset):

        return None
    
    def enlargeToContain(self, point_or_rect):

        return None
    
    def intersect(self, rect):

        return None
    

class Color():


    def __init__(self, rgb_tuple):

        pass
    
    def rgb(self):

        return (0.0, 0.0, 0.0,)
    
    def setRGB(self, tuple):

        return None
    
    def hsv(self):

        return (0.0, 0.0, 0.0,)
    
    def setHSV(self, tuple):

        return None
    
    def hsl(self):

        return (0.0, 0.0, 0.0,)
    
    def setHSL(self, tuple):

        return None
    
    def lab(self):

        return (0.0, 0.0, 0.0,)
    
    def setLAB(self, tuple):

        return None
    
    def tmi(self):

        return (0.0, 0.0, 0.0,)
    
    def setTMI(self, tuple):

        return None
    
    def xyz(self):

        return (0.0, 0.0, 0.0,)
    
    def setXYZ(self, tuple):

        return None
    
    def ocio_spaces(self):

        return None
    

class Matrix2():


    def __init__(self, values):

        pass
    
    def isAlmostEqual(self, matrix2, tolerance=object):

        return True
    
    def at(self, row, col):

        return 0.0
    
    def setAt(self, row, col, value):

        return None
    
    def asTuple(self):

        return (0.0, )
    
    def asTupleOfTuples(self):

        return (object, )
    
    def setTo(self, tuple):

        return None
    
    def setToIdentity(self):

        return None
    
    def setToZero(self):

        return None
    
    def __add__(self, matrix2):

        return Matrix2
    
    def __sub__(self, matrix2):

        return Matrix2
    
    def __mul__(self, matrix2_or_scalar):

        return Matrix2
    
    def preMult(self, matrix2):

        return Matrix2
    
    def transposed(self):

        return Matrix2
    
    def inverted(self):

        return Matrix2
    
    def determinant(self):

        return 0.0
    

class Matrix3():


    def __init__(self, values):

        pass
    
    def at(self, row, col):

        return 0.0
    
    def setAt(self, row, col, value):

        return None
    
    def asTuple(self):

        return (0.0, )
    
    def asTupleOfTuples(self):

        return (object, )
    
    def setTo(self, tuple):

        return None
    
    def setToIdentity(self):

        return None
    
    def setToZero(self):

        return None
    
    def __add__(self, matrix3):

        return Matrix3
    
    def __sub__(self, matrix3):

        return Matrix3
    
    def __mul__(self, matrix3_or_scalar):

        return Matrix3
    
    def preMult(self, matrix3):

        return Matrix3
    
    def determinant(self):

        return 0.0
    
    def extractRotates(self, rotate_order=object):

        return Vector3
    
    def inverted(self):

        return Matrix3
    
    def transposed(self):

        return Matrix3
    
    def isAlmostEqual(self, matrix3, tolerance=object):

        return True
    

class Matrix4():


    def __init__(self, values):

        pass
    
    def at(self, row, col):

        return 0.0
    
    def setAt(self, row, col, value):

        return None
    
    def asTuple(self):

        return (0.0, )
    
    def asTupleOfTuples(self):

        return (object, )
    
    def setTo(self, sequence):

        return None
    
    def setToIdentity(self):

        return None
    
    def setToZero(self):

        return None
    
    def __add__(self, matrix4):

        return Matrix4
    
    def __sub__(self, matrix4):

        return Matrix4
    
    def __mul__(self, matrix4_or_scalar):

        return Matrix4
    
    def preMult(self, matrix4):

        return Matrix4
    
    def determinant(self):

        return 0.0
    
    def explode(self, transform_order=object, rotate_order=object, pivot=Vector3(), pivot_rotate=Vector3()):

        return {"": Vector3}
    
    def extractTranslates(self, transform_order=object, pivot_rotate=Vector3()):

        return Vector3
    
    def extractRotates(self, transform_order=object, rotate_order=object, pivot=Vector3(), pivot_rotate=Vector3()):

        return Vector3
    
    def extractScales(self, transform_order=object, pivot=Vector3(), pivot_rotate=Vector3()):

        return Vector3
    
    def extractShears(self, transform_order=object, pivot=Vector3(), pivot_rotate=Vector3()):

        return Vector3
    
    def extractRotationMatrix3(self):

        return Matrix3
    
    def inverted(self):

        return Matrix4
    
    def transposed(self):

        return Matrix4
    
    def isAlmostEqual(self, matrix4, tolerance=object):

        return True
    

class OrientedBoundingRect():


    def __init__(self, points):

        pass
    
    def isAlmostEqual(self, brect, tolerance=object):

        return True
    
    def sizevec(self):

        return Vector2
    
    def center(self):

        return Vector2
    
    def orientation(self):

        return Matrix2
    

class Quaternion():


    def __init__(self):

        pass
    
    def extractRotationMatrix3(self):

        return Matrix3
    
    def extractAngleAxis(self):

        return (0.0, Vector3,)
    
    def extractEulerRotates(self, rotate_order=object):

        return Vector3
    
    def rotate(self, vec):

        return Vector3
    
    def slerp(self, other, fraction):

        return Quaternion
    
    def setToRotationMatrix(self, matrix3_or_matrix4):

        return None
    
    def setToAngleAxis(self, angle_in_deg, axis):

        return None
    
    def setToVectors(self, a, b):

        return None
    
    def setToEulerRotates(self, angles_in_deg, rotate_order=object):

        return None
    
    def setTo(self, tuple):

        return None
    
    def isAlmostEqual(self, quaternion, tolerance=object):

        return True
    
    def conjugate(self):

        return Quaternion
    
    def inverse(self):

        return Quaternion
    
    def normalized(self):

        return Quaternion
    
    def length(self):

        return 0.0
    
    def dot(self, other):

        return 0.0
    
    def __getitem__(self, index):

        return 0.0
    
    def __setitem__(self, index, value):

        return None
    
    def __len__(self):

        return 0
    
    def __add__(self, quaternion):

        return Quaternion
    
    def __sub__(self, quaternion):

        return Quaternion
    
    def __mul__(self, quaternion_or_scalar):

        return Quaternion
    

class Ramp():


    def __init__(self, basis, keys, values):

        pass
    
    def isColor(self):

        return True
    
    def colorType(self):

        return object
    
    def setColorType(self, colorType):

        return None
    
    def lookup(self, interpolant):

        return object
    
    def basis(self):

        return (EnumValue, )
    
    def keys(self):

        return (0.0, )
    
    def values(self):

        return (0.0, )
    

class ShopNodeType(NodeType):


    def renderMask(self):

        return ""
    
    def shaderType(self):

        return EnumValue
    

class Vector2():


    def __init__(self, values):

        pass
    
    def __getitem__(self, index):

        return 0.0
    
    def __setitem__(self, index, value):

        return None
    
    def setTo(self, sequence):

        return None
    
    def __len__(self):

        return 0
    
    def __add__(self, vector2):

        return Vector2
    
    def __sub__(self, vector2):

        return Vector2
    
    def __neg__(self):

        return Vector2
    
    def __mul__(self, scalar_or_matrix2):

        return Vector2
    
    def __rmul__(self, scalar):

        return Vector2
    
    def __div__(self, scalar):

        return Vector2
    
    def length(self):

        return 0.0
    
    def lengthSquared(self):

        return 0.0
    
    def normalized(self):

        return Vector2
    
    def distanceTo(self, vector2):

        return 0.0
    
    def dot(self, vector2):

        return 0.0
    
    def isAlmostEqual(self, vector2, tolerance=object):

        return True
    
    def x(self):

        return 0.0
    
    def y(self):

        return 0.0
    

class Vector3():


    def __init__(self, values):

        pass
    
    def __getitem__(self, index):

        return 0.0
    
    def __setitem__(self, index, value):

        return None
    
    def setTo(self, sequence):

        return None
    
    def __len__(self):

        return 0
    
    def __add__(self, vector3):

        return Vector3
    
    def __sub__(self, vector3):

        return Vector3
    
    def __neg__(self):

        return Vector3
    
    def __mul__(self, scalar_or_matrix4):

        return Vector3
    
    def __rmul__(self, scalar):

        return Vector3
    
    def __div__(self, scalar):

        return Vector3
    
    def length(self):

        return 0.0
    
    def lengthSquared(self):

        return 0.0
    
    def normalized(self):

        return Vector3
    
    def multiplyAsDir(self, matrix4):

        return Vector3
    
    def distanceTo(self, vector3):

        return 0.0
    
    def dot(self, vector3):

        return 0.0
    
    def cross(self, vector3):

        return Vector3
    
    def angleTo(self, vector3):

        return 0.0
    
    def matrixToRotateTo(self, vector3):

        return Matrix4
    
    def isAlmostEqual(self, vector3, tolerance=object):

        return True
    
    def smoothRotation(self, reference, rotate_order=object):

        return Vector3
    
    def ocio_transform(self, src_space, dest_space):

        return Vector3
    
    def x(self):

        return 0.0
    
    def y(self):

        return 0.0
    
    def z(self):

        return 0.0
    

class Vector4():


    def __init__(self, values):

        pass
    
    def __getitem__(self, index):

        return 0.0
    
    def __setitem__(self, index, value):

        return None
    
    def setTo(self, sequence):

        return None
    
    def __len__(self):

        return 0
    
    def __add__(self, vector4):

        return Vector4
    
    def __sub__(self, vector4):

        return Vector4
    
    def __mul__(self, scalar_or_matrix4):

        return Vector4
    
    def __rmul__(self, scalar):

        return Vector4
    
    def __div__(self, scalar):

        return Vector4
    
    def length(self):

        return 0.0
    
    def lengthSquared(self):

        return 0.0
    
    def normalized(self):

        return Vector4
    
    def dot(self, vector4):

        return 0.0
    
    def isAlmostEqual(self, vector4, tolerance=object):

        return True
    
    def ocio_transform(self, src_space, dest_space):

        return Vector4
    
    def x(self):

        return 0.0
    
    def y(self):

        return 0.0
    
    def z(self):

        return 0.0
    
    def w(self):

        return 0.0
    

class VopNodeType(NodeType):


    def renderMask(self):

        return ""
    
    def shaderType(self):

        return EnumValue
    
    def inputTags(self, input_name):

        return {"": ""}
    
    def outputTags(self, output_name):

        return {"": ""}
    

class VexContext():


    def name(self):

        return ""
    
    def nodeTypeCategory(self):

        return NodeTypeCategory
    
    def pathsToLoadedVexFunctions(self):

        return {"": ""}
    
    def shaderType(self):

        return EnumValue
    

class VopNode(NetworkItem, NetworkMovableItem, Node):


    def shaderName(self, as_otl_path=True, shader_type_name=None):

        return ""
    
    def shaderCode(self, shader_type=object):

        return ""
    
    def shaderLanguageName(self):

        return ""
    
    def shaderString(self, render_type=None, shader_type=object, as_encapsulated=True):

        return ""
    
    def code(self):

        return ""
    
    def outerCode(self):

        return ""
    

class ConstructionPlane():


    def sceneViewer(self):

        return SceneViewer
    
    def isVisible(self):

        return True
    
    def setIsVisible(self, on):

        return None
    
    def transform(self):

        return Matrix4
    
    def setTransform(self, matrix):

        return None
    
    def cellSize(self):

        return (0.0, )
    
    def setCellSize(self, size):

        return None
    
    def numberOfCells(self):

        return (0, )
    
    def setNumberOfCells(self, number):

        return None
    
    def numberOfCellsPerRulerLine(self):

        return (0, )
    
    def setNumberOfCellsPerRulerLine(self, number):

        return None
    

class ContextViewer(Pane, PathBasedPaneTab):


    def compositorViewer(self):

        return CompositorViewer
    
    def sceneViewer(self):

        return SceneViewer
    

class FlipbookSettings():


    def stash(self):

        return FlipbookSettings
    
    def copy(self, from_settings):

        return None
    

class GeometrySelection():


    def connectivity(self):

        return EnumValue
    
    def geometryType(self):

        return EnumValue
    
    def mergedNode(self, parent, creator_name, force_keep_original_objects=True, display_original_objects=True):

        return Node
    
    def mergedSelectionString(self, empty_string_selects_all=True, force_numeric=True):

        return ""
    
    def shrinkSelection(self, checkuv=True):

        return None
    
    def growSelection(self):

        return None
    
    def needsMergedNode(self, parent):

        return True
    
    def nodes(self):

        return (Node, )
    
    def ordered(self):

        return True
    
    def primitiveTypes(self):

        return (EnumValue, )
    
    def selections(self):

        return (Selection, )
    
    def selectionStrings(self, empty_string_selects_all=True, force_numeric=True):

        return ("", )
    
    def setConnectivity(self, connectivity):

        return None
    
    def setGeometryType(self, type):

        return None
    
    def setPrimitiveTypes(self, primitive_types):

        return None
    

class GeometryViewport():


    def home(self):

        return None
    
    def homeAll(self):

        return None
    
    def homeSelected(self):

        return None
    
    def homeGrid(self):

        return None
    
    def homeNonTemplated(self):

        return None
    
    def frameAll(self):

        return None
    
    def frameBoundingBox(self, bbox):

        return None
    
    def frameSelected(self):

        return None
    
    def frameGrid(self):

        return None
    
    def frameNonTemplated(self):

        return None
    
    def viewTransform(self):

        return None
    
    def viewPivot(self):

        return None
    

class GeometryViewportDisplaySet():


    def displaySetType(self):

        return displaySetType
    
    def isShowingPointMarkers(self):

        return True
    
    def isShowingPointNumbers(self):

        return True
    
    def isShowingPointNormals(self):

        return True
    
    def isShowingPointUVs(self):

        return True
    
    def isShowingPointPositions(self):

        return True
    
    def isShowingPointTrails(self):

        return True
    
    def isShowingCoincidentPoints(self):

        return True
    
    def isShowingPrimHulls(self):

        return True
    
    def isShowingPrimNormals(self):

        return True
    
    def isShowingPrimNumbers(self):

        return True
    
    def isShowingPrimBreakpoints(self):

        return True
    
    def isShowingPrimProfiles(self):

        return True
    
    def isShowingPrimProfileNumbers(self):

        return True
    
    def isShowingVertexMarkers(self):

        return True
    
    def isShowingVertexNumbers(self):

        return True
    
    def isShowingVertexNormals(self):

        return True
    
    def isShowingVertexUVs(self):

        return True
    
    def isShowingUVBackfaces(self):

        return True
    
    def isShowingUVOverlap(self):

        return True
    
    def showPointMarkers(self, on):

        return None
    
    def showPointNumbers(self, on):

        return None
    
    def showPointNormals(self, on):

        return None
    
    def showPointTextureCoordinates(self, on):

        return None
    
    def showPointPositions(self, on):

        return None
    
    def showPointTrails(self, on):

        return None
    
    def showCoincidentPoints(self, on):

        return None
    
    def showPrimHulls(self, on):

        return None
    
    def showPrimNumbers(self, on):

        return None
    
    def showPrimNormals(self, on):

        return None
    
    def showPrimBreakpoints(self, on):

        return None
    
    def showPrimProfiles(self, on):

        return None
    
    def showPrimProfileNumbers(self, on):

        return None
    
    def showVertexMarkers(self, on):

        return None
    
    def showVertexNumbers(self, on):

        return None
    
    def showVertexNormals(self, on):

        return None
    
    def showVertexTextureCoordinates(self, on):

        return None
    
    def showUVBackfaces(self, on):

        return None
    
    def showUVOverlap(self, on):

        return None
    
    def setPointMarkerVisibility(self, visibility):

        return None
    
    def setPointNumberVisibility(self, visibility):

        return None
    
    def setPointNormalVisibility(self, visibility):

        return None
    
    def setPointUVVisibility(self, visibility):

        return None
    
    def setPointPositionVisibility(self, visibility):

        return None
    
    def setPointTrailVisibility(self, visibility):

        return None
    
    def setPrimNumberVisibility(self, visibility):

        return None
    
    def setPrimNormalVisibility(self, visibility):

        return None
    
    def setPrimBreakpointVisibility(self, visibility):

        return None
    
    def setVertexMarkerVisibility(self, visibility):

        return None
    
    def setVertexNumberVisibility(self, visibility):

        return None
    
    def setVertexNormalVisibility(self, visibility):

        return None
    
    def setVertexUVVisibility(self, visibility):

        return None
    
    def pointMarkerVisibility(self):

        return markerVisibility
    
    def pointNumberVisibility(self):

        return markerVisibility
    
    def pointNormalVisibility(self):

        return markerVisibility
    
    def pointUVVisibility(self):

        return markerVisibility
    
    def pointPositionVisibility(self):

        return markerVisibility
    
    def pointTrailVisibility(self):

        return markerVisibility
    
    def primNumberVisibility(self):

        return markerVisibility
    
    def primNormalVisibility(self):

        return markerVisibility
    
    def primBreakpointVisibility(self):

        return markerVisibility
    
    def vertexMarkerVisibility(self):

        return markerVisibility
    
    def vertexNumberVisibility(self):

        return markerVisibility
    
    def vertexNormalVisibility(self):

        return markerVisibility
    
    def vertexUVVisibility(self):

        return markerVisibility
    
    def shadedMode(self):

        return glShadingType
    
    def isShadingModeLocked(self):

        return True
    
    def isUsingGhostedLook(self):

        return True
    
    def isUsingFadedLook(self):

        return True
    
    def isUsingXRay(self):

        return True
    
    def isUsingLighting(self):

        return True
    
    def isShowingBoundaries(self):

        return boundaryDisplay
    
    def isToolbarLinked(self):

        return True
    
    def linkedToDisplaySet(self):

        return displaySetType
    
    def isUniqueDisplaySet(self):

        return True
    
    def setShadedMode(self, shaded_mode):

        return None
    
    def setShadingModeLocked(self, on):

        return None
    
    def useGhostedLook(self, on):

        return None
    
    def useFadedLook(self, on):

        return None
    
    def useXRay(self, on):

        return None
    
    def useLighting(self, on):

        return None
    
    def setShowingBoundaries(self, view_boundary_mode):

        return None
    
    def setToolbarLinked(self, on):

        return None
    
    def setLinkToDisplaySet(self, view_display_set):

        return None
    
    def setUniqueDisplaySet(self, on):

        return None
    

class GeometryViewportSettings():


    def displaySet(self, display_set):

        return GeometryViewportDisplaySet
    
    def camera(self):

        return ObjNode
    
    def normalScale(self):

        return 0.0
    
    def saveViewToCamera(self, camera_node):

        return None
    
    def sceneAntialias(self):

        return None
    
    def setCamera(self, camera_node):

        return None
    
    def setNormalScale(self, normal_scale):

        return None
    
    def setSceneAntialias(self, aalevel):

        return None
    
    def viewAspectRatio(self, masked=True):

        return None
    
    def viewportType(self):

        return EnumValue
    
    def enableGuide(self, viewportGuide, on):

        return None
    
    def enableGuide(self, viewportGuide):

        return True
    
    def vectorScale(self):

        return 0.0
    
    def setVectorScale(self, scale):

        return None
    
    def pointMarkerSize(self):

        return 0.0
    
    def setPointMarkerSize(self, point_size):

        return None
    
    def originGnomonSize(self):

        return 0.0
    
    def setOriginGnomonSize(self, size):

        return None
    
    def geometryInfo(self):

        return viewportGeometryInfo
    
    def geometryInfo(self, viewportGeometryInfo):

        return None
    
    def handleHighlight(self):

        return viewportHandleHighlight
    
    def handleHighlight(self, viewportHandleHighlight):

        return None
    
    def closureSelection(self):

        return viewportClosureSelection
    
    def closureSelection(self, viewportClosureSelection):

        return None
    
    def guideFontSize(self):

        return viewportGuideFont
    
    def guideFontSize(self, viewportGuideFont):

        return None
    
    def levelOfDetail(self, value):

        return None
    
    def levelOfDetail(self):

        return 0.0
    
    def volumeQuality(self, viewportVolumeQuality):

        return None
    
    def volumeQuality(self):

        return viewportVolumeQuality
    
    def volumeWireAsPoints(self, as_points):

        return None
    
    def volumeWireAsPoints(self):

        return True
    
    def polygonConvexQuality(self, quality):

        return None
    
    def polygonConvexQuality(self):

        return True
    
    def wireWidth(self, width):

        return None
    
    def wireWidth(self):

        return 0.0
    
    def wireBlend(self, blend):

        return None
    
    def wireBlend(self):

        return 0.0
    
    def interiorWireAlpha(self, alpha):

        return None
    
    def interiorWireAlpha(self):

        return 0.0
    
    def shadeOpenCurves(self, shade):

        return None
    
    def shadeOpenCurves(self):

        return True
    
    def selectWireframeAsSolid(self, as_solid):

        return None
    
    def selectWireframeAsSolid(self):

        return True
    
    def particleDisplayType(self, viewportParticleDisplay):

        return None
    
    def particleDisplayType(self):

        return viewportParticleDisplay
    
    def allowParticleSprites(self, sprites):

        return None
    
    def allowParticleSprites(self):

        return True
    
    def particlePointSize(self, size):

        return None
    
    def particlePointSize(self):

        return 0.0
    
    def particleDiscSize(self, size):

        return None
    
    def particleDiscSize(self):

        return 0.0
    
    def orientDiscToNormal(self, n_orient):

        return None
    
    def orientDiscToNormal(self):

        return True
    
    def spriteTextureLimit(self, max_res):

        return None
    
    def spriteTextureLimit(self):

        return (0, )
    
    def pointInstancing(self, enable):

        return None
    
    def pointInstancing(self):

        return True
    
    def pointInstancingPercent(self, show_instances):

        return None
    
    def pointInstancingPercent(self):

        return 0.0
    
    def pointInstancingLimit(self, millions_of_instances):

        return None
    
    def pointInstancingLimit(self):

        return 0
    
    def instanceStandInGeometry(self, viewportStandInGeometry):

        return None
    
    def instanceStandInGeometry(self):

        return viewportStandInGeometry
    
    def autoGenerateVertexNormals(self, vertex):

        return None
    
    def autoGenerateVertexNormals(self):

        return True
    
    def vertexNormalCuspAngle(self, angle):

        return None
    
    def vertexNormalCuspAngle(self):

        return 0.0
    
    def vertexNormalLimit(self, millions_of_polys):

        return None
    
    def vertexNormalLimit(self):

        return 0
    
    def uvDisplayAttribute(self, uv):

        return None
    
    def uvDisplayAttribute(self):

        return ""
    
    def uvAutoAttribute(self, detect):

        return None
    
    def uvAutoAttribute(self):

        return True
    
    def uvVertexType(self, is_vertex_uv):

        return None
    
    def uvVertexType(self):

        return True
    

class SceneViewer(Pane, PathBasedPaneTab):


    def selectObjects(self, prompt=object, sel_index=object, allow_drag=True, quick_select=True, use_existing_selection=True, allow_multisel=True, allowed_types=None, icon=None, label=None, prior_selection_paths=object, prior_selection_ids=object, prior_selections=object):

        return (Node, )
    
    def selectGeometry(self, prompt=object, sel_index=object, allow_drag=True, quick_select=True, use_existing_selection=True, initial_selection=None, initial_selection_type=None, ordered=True, geometry_types=tuple(), primitive_types=tuple(), allow_obj_sel=True, icon=None, label=None, prior_selection_paths=object, prior_selection_ids=object, prior_selections=object, allow_other_sops=True, consume_selections=True):

        return GeometrySelection
    
    def selectPositions(self, prompt=object, number_of_positions=object, connect_positions=True, show_coordinates=True, bbox=BoundingBox(), position_type=object, icon=None, label=None):

        return (Vector3, )
    
    def selectDynamics(self, prompt=object, sel_index=object, allow_objects=True, allow_modifiers=True, quick_select=True, use_existing_selection=True, allow_multisel=True, icon=None, label=None, prior_selection_paths=object, prior_selection_ids=object, prior_selections=object):

        return (DopData, )
    
    def selectDynamicsPoints(self, prompt=object, sel_index=object, quick_select=True, use_existing_selection=True, allow_multisel=True, only_select_points=True, object_based_point_selection=True, use_last_selected_object=True, icon=None, label=None, prior_selection_paths=object, prior_selection_ids=object, prior_selections=object):

        return ((DopData, GeometrySelection,),)
    
    def selectDynamicsPolygons(self, prompt=object, sel_index=object, quick_select=True, use_existing_selection=True, object_based_point_selection=True, use_last_selected_object=True, icon=None, label=None, prior_selection_paths=object, prior_selection_ids=object, prior_selections=object):

        return ((DopData, GeometrySelection,),)
    

class Selector():


    def nodeType(self):

        return NodeType
    
    def destroy(self):

        return None
    
    def name(self):

        return ""
    
    def selectorType(self):

        return ""
    
    def prompt(self):

        return ""
    
    def primitiveTypes(self):

        return (EnumValue, )
    
    def groupParmName(self):

        return ""
    
    def groupTypeParmName(self):

        return ""
    
    def inputIndex(self):

        return 0
    
    def inputRequired(self):

        return True
    
    def allowDragging(self):

        return True
    
    def emptyStringSelectsAll(self):

        return True
    
    def extraInfo(self):

        return ""
    
    def geometryTypes(self):

        return (EnumValue, )
    
    def groupTypeParmValues(self):

        return (0, )
    
    def ordered(self):

        return True
    

class ViewerState():


    def categories(self):

        return (NodeTypeCategory, )
    
    def description(self):

        return ""
    
    def icon(self):

        return ""
    
    def isHidden(self):

        return True
    
    def name(self):

        return ""
    
    def nodeType(self):

        return NodeType
    

class ViewportVisualizer():


    def name(self):

        return ""
    
    def setName(self, name):

        return None
    
    def label(self):

        return ""
    
    def setLabel(self, label):

        return None
    
    def icon(self):

        return ""
    
    def setIcon(self, icon):

        return None
    
    def isActive(self, viewport=None):

        return True
    
    def setIsActive(self, on, viewport=None):

        return None
    
    def type(self):

        return ViewportVisualizerType
    
    def setType(self, type):

        return None
    
    def category(self):

        return viewportVisualizerCategory
    
    def categoryNode(self):

        return Node
    
    def scope(self):

        return viewportVisualizerScope
    
    def setScope(self, scope):

        return None
    
    def isShownInToolbar(self):

        return True
    
    def showInToolbar(self, on):

        return None
    
    def isActiveWhenUnselected(self):

        return True
    
    def setIsActiveWhenUnselected(self, on):

        return None
    
    def isActiveWhenSelected(self):

        return True
    
    def setIsActiveWhenSelected(self, on):

        return None
    
    def isActiveWhenGhosted(self):

        return True
    
    def setIsActiveWhenGhosted(self, on):

        return None
    
    def isActiveWhenDisplayed(self):

        return True
    
    def setIsActiveWhenDisplayed(self, on):

        return None
    
    def isActiveWhenCurrent(self):

        return True
    
    def setIsActiveWhenCurrent(self, on):

        return None
    
    def isActiveWhenTemplated(self):

        return True
    
    def setIsActiveWhenTemplated(self, on):

        return None
    
    def parmNames(self):

        return ("", )
    
    def evalParm(self, parm_name):

        return object
    
    def evalParmAsFloat(self, parm_name):

        return 0.0
    
    def evalParmAsInt(self, parm_name):

        return 0
    
    def evalParmAsString(self, parm_name):

        return 0
    
    def evalParmAsRamp(self):

        return Ramp
    
    def setParm(self, parm_name, value):

        return None
    
    def destroy(self):

        return None
    

class ViewportVisualizerType():


    def name(self):

        return ""
    
    def description(self):

        return ""
    
    def icon(self):

        return ""
    

class audio():


    def setAudioFileName(self, path):

        return None
    
    def setChopPath(self, path):

        return None
    
    def useAudioFile(self):

        return None
    
    def useChops(self):

        return None
    
    def setMono(self, on):

        return None
    
    def setLeftVolume(self, value):

        return None
    
    def setRightVolume(self, value):

        return None
    
    def setVolumeTied(self, on):

        return None
    
    def setMeter(self, on):

        return None
    
    def setAudioOffset(self, offset):

        return None
    
    def setAudioFrame(self, frame):

        return None
    
    def useTestMode(self):

        return None
    
    def useTimeLineMode(self):

        return None
    
    def useTimeSliceMode(self):

        return None
    
    def turnOffAudio(self):

        return None
    
    def play(self):

        return None
    
    def stop(self):

        return None
    
    def reverse(self):

        return None
    
    def setLooping(self, on):

        return None
    
    def setRewind(self, on):

        return None
    
    def setScrubRate(self, value):

        return None
    
    def setScrubRepeat(self, on):

        return None
    
    def setScrubSustain(self, value):

        return None
    

class crowds():


    def computeRotationLimits(self, rig, clips, transform, parent_transform):

        return {"": object}
    
    def findAgentDefinitions(self, geometry, group=object):

        return (AgentDefinition, )
    
    def replaceAgentDefinitions(self, geometry, new_definition_map, group=object):

        return None
    

class dop():


    def isScriptSolverRunning(self):

        return True
    
    def scriptSolverData(self):

        return DopData
    
    def scriptSolverNetwork(self):

        return Node
    
    def scriptSolverSimulation(self):

        return DopSimulation
    
    def scriptSolverObjects(self):

        return (DopObject, )
    
    def scriptSolverNewObjects(self):

        return (DopObject, )
    
    def scriptSolverTimestepSize(self):

        return 0.0
    

class galleries():


    def createGalleryEntry(self, gallery_path, entry_name, node):

        return GalleryEntry
    
    def galleries(self):

        return (Gallery, )
    
    def galleryEntries(self, name_pattern=None, label_pattern=None, keyword_pattern=None, category=None, node_type=None):

        return (GalleryEntry, )
    
    def installGallery(self, gallery_path):

        return Gallery
    
    def removeGallery(self, gallery_path):

        return True
    

class hda():


    def definitionsInFile(self, file_path):

        return (HDADefinition, )
    
    def installFile(self, file_path, oplibraries_file=None, change_oplibraries_file=True, force_use_assets=True):

        return None
    
    def uninstallFile(self, file_path, oplibraries_file=None, change_oplibraries_file=True):

        return None
    
    def reloadFile(self, file_path):

        return None
    
    def reloadAllFiles(self, rescan=True):

        return None
    
    def reloadNamespaceOrder(self):

        return None
    
    def loadedFiles(self):

        return ("", )
    
    def expandToDirectory(self, file_path, directory_path):

        return None
    
    def collapseFromDirectory(self, file_path, directory_path):

        return None
    
    def renameSource(self, oplibraries_file, source_name=None):

        return None
    
    def encryptAsset(self, node, file_path, email, password, company, license_names, compile_basic=True, compile_vopnets=True, compile_channels=True, compile_nodenames=True):

        return None
    
    def createEntitlement(self, email, password, company, license_name, server_code, entitled_email, license_type=object, expiry=object):

        return None
    
    def availableEntitlements(self, email, password):

        return ("", )
    
    def redeemEntitlements(self, email, password, license_file=None, entitlements=tuple()):

        return None
    
    def componentsFromFullNodeTypeName(self, node_type_name):

        return ("", )
    
    def fullNodeTypeNameFromComponents(self, scope_node_type, name_space, name, version):

        return ""
    
    def reloadHDAModule(self, hda_module):

        return None
    
    def safeguardHDAs(self):

        return True
    
    def setSafeguardHDAs(self, on):

        return None
    

class hipFile():


    def basename(self):

        return ""
    
    def name(self):

        return ""
    
    def path(self):

        return ""
    
    def hasUnsavedChanges(self):

        return True
    
    def load(self, file_name, suppress_save_prompt=True, ignore_load_warnings=True):

        return None
    
    def save(self, file_name=None, save_to_recent_files=True):

        return None
    
    def setName(self, file_name):

        return None
    
    def saveAndIncrementFileName(self):

        return None
    
    def saveAsBackup(self):

        return None
    
    def clear(self, suppress_save_prompt=True):

        return None
    
    def merge(self, file_name, node_pattern=object, overwrite_on_conflict=True, ignore_load_warnings=True):

        return None
    
    def collisionNodesIfMerged(self, file_name, node_pattern=object):

        return (Node, )
    
    def isLoadingHipFile(self):

        return True
    
    def isShuttingDown(self):

        return True
    
    def groupColorTable(self):

        return {"": Color}
    
    def setGroupColorTable(self, color_table):

        return None
    
    def saveMode(self):

        return saveMode
    
    def setSaveMode(self, save_mode):

        return None
    
    def importFBX(self, file_name, suppress_save_prompt=True, merge_into_scene=True, import_cameras=True, import_joints_and_skin=True, import_geometry=True, import_lights=True, import_animation=True, import_materials=True, resample_animation=True, resample_interval=object, override_framerate=True, framerate=object, hide_joints_attached_to_skin=True, convert_joints_to_zyx_rotation_order=True, material_mode=object, compatibility_mode=object, single_precision_vertex_caches=True, triangulate_nurbs=True, triangulate_patches=True, import_global_ambient_light=True, import_blend_deformers_as_blend_sops=True, segment_scale_already_baked_in=True, convert_file_paths_to_relative=True, unlock_geometry=True, unlock_deformations=True, import_nulls_as_subnets=True, import_into_object_subnet=True, convert_into_y_up_coordinate_system=True):

        return (ObjNode, "",)
    
    def addEventCallback(self, callback):

        return None
    
    def removeEventCallback(self, callback):

        return None
    
    def clearEventCallbacks(self):

        return None
    
    def eventCallbacks(self):

        return (object, )
    

class hmath():


    def buildTranslate(self, values):

        return Matrix4
    
    def buildRotateAboutAxis(self, axis, angle_in_deg):

        return Matrix4
    
    def buildRotate(self, values, order=object):

        return Matrix4
    
    def buildScale(self, values):

        return Matrix4
    
    def buildShear(self, values):

        return Matrix4
    
    def buildTransform(self, values_dict, transform_order=object, rotate_order=object):

        return Matrix4
    
    def identityTransform(self):

        return Matrix4
    
    def degToRad(self, degrees):

        return 0.0
    
    def radToDeg(self, radians):

        return 0.0
    
    def clamp(self, value, min, max):

        return 0.0
    
    def wrap(self, value, min, max):

        return None
    
    def sign(self, value):

        return 0
    
    def smooth(self, value, min, max):

        return 0.0
    
    def fit(self, value, old_min, old_max, new_min, new_max):

        return 0.0
    
    def fit01(self, value, new_min, new_max):

        return 0.0
    
    def fit10(self, value, new_min, new_max):

        return 0.0
    
    def fit11(self, value, new_min, new_max):

        return 0.0
    
    def rand(self, seed):

        return 0.0
    
    def noise1d(self, pos):

        return 0.0
    
    def noise3d(self, pos):

        return Vector3
    
    def orient2d(self, pa, pb, point):

        return 0.0
    
    def orient3d(self, pa, pb, pc, point):

        return 0.0
    
    def inCircle(self, pa, pb, pc, point):

        return 0.0
    
    def inSphere(self, pa, pb, pc, pd, point):

        return 0.0
    

class perfMon():


    def isRecording(self):

        return True
    
    def loadProfile(self, file_path):

        return PerfMonProfile
    
    def activeProfile(self):

        return PerfMonProfile
    

class playbar():


    def addEventCallback(self, callback):

        return None
    
    def areKeysShown(self):

        return True
    
    def areTicksShown(self):

        return True
    
    def clearEventCallbacks(self):

        return None
    
    def eventCallbacks(self):

        return (object, )
    
    def frameIncrement(self):

        return 0.0
    
    def isAudioShown(self):

        return True
    
    def isRangeSliderShown(self):

        return True
    
    def isPlaying(self):

        return True
    
    def isRangeRestricted(self):

        return True
    
    def isRealTime(self):

        return True
    
    def isRealTimeSkipping(self):

        return True
    
    def jumpToNextKeyframe(self):

        return None
    
    def jumpToPreviousKeyframe(self):

        return None
    
    def moveToBottom(self):

        return None
    
    def moveToPane(self, pane):

        return None
    
    def play(self):

        return None
    
    def playbackRange(self):

        return Vector2
    
    def playMode(self):

        return playMode
    
    def realTimeFactor(self):

        return 0.0
    
    def removeEventCallback(self, callback):

        return None
    
    def reverse(self):

        return None
    
    def selectedKeyframes(self):

        return {Parm: (BaseKeyframe, )}
    
    def selectionRange(self):

        return Vector2
    
    def selectionRanges(self):

        return (Vector2, )
    
    def setFrameIncrement(self, increment):

        return None
    
    def setPlaybackRange(self, start, end):

        return None
    
    def setPlayMode(self, mode):

        return None
    
    def setRealTime(self, on):

        return None
    
    def setRealTimeFactor(self, factor):

        return None
    
    def setRealTimeSkipping(self, on):

        return None
    
    def setRestrictRange(self, on):

        return None
    
    def setUseIntegerFrames(self, on):

        return None
    
    def showAudio(self, on):

        return None
    
    def showKeys(self, on):

        return None
    
    def showRangeSlider(self, on):

        return None
    
    def showTicks(self, on):

        return None
    
    def stop(self):

        return None
    
    def usesIntegerFrames(self):

        return True
    

class properties():


    def classes(self, tags=None):

        return ("", )
    
    def classLabel(self, class_name):

        return ""
    
    def categories(self, class_name):

        return ("", )
    
    def parameters(self, class_name, category_name):

        return ("", )
    
    def parmTemplate(self, class_name, parm_name):

        return ParmTemplate
    

class pypanel():


    def installFile(self, file_path):

        return None
    
    def interfacesInFile(self, file_path):

        return (PythonPanelInterface, )
    
    def interfaces(self):

        return {"": PythonPanelInterface}
    
    def menuInterfaces(self):

        return ("", )
    
    def setMenuInterfaces(self, names):

        return None
    

class qt():


    def createDialog(self):

        return QWidget
    
    def createMenu(self):

        return QMenu
    
    def createToolTip(self):

        return QWidget
    
    def createWindow(self):

        return QWidget
    

class session():

    pass

class shelves():


    def defaultFilePath(self):

        return ""
    
    def newShelf(self, file_path=None, name=None, label=None):

        return Shelf
    
    def newShelfSet(self, file_path=None, name=None, label=None):

        return ShelfSet
    
    def newTool(self, file_path=None, name=None, label=None, script=None, language=object, icon=None, help=None, help_url=None, network_categories=tuple(), viewer_categories=tuple(), cop_viewer_categories=tuple(), network_op_type=None, viewer_op_type=None, locations=tuple()):

        return Tool
    
    def loadFile(self, file_path):

        return None
    
    def reloadShelfFiles(self):

        return None
    
    def runningTool(self):

        return Tool
    
    def shelfSets(self):

        return {"": ShelfSet}
    
    def shelves(self):

        return {"": Shelf}
    
    def tools(self):

        return {"": Tool}
    
    def tool(self, tool_name):

        return Tool
    
    def beginChangeBlock(self):

        return None
    
    def endChangeBlock(self):

        return None
    

class styles():


    def hasStyle(self, name):

        return True
    
    def styles(self):

        return ("", )
    
    def description(self, name):

        return ""
    
    def stylesheet(self, name):

        return ""
    
    def errors(self, name):

        return ""
    
    def addStyle(self, name, description, stylesheet):

        return None
    
    def renameStyle(self, old_name, new_name):

        return None
    
    def reorderStyles(self, names):

        return None
    
    def removeStyle(self, name):

        return None
    
    def removeAll(self):

        return None
    

class takes():


    def takes(self):

        return (Take, )
    
    def currentTake(self):

        return Take
    
    def setCurrentTake(self, take):

        return None
    
    def rootTake(self):

        return Take
    
    def findTake(self, take_name):

        return Take
    
    def defaultTakeName(self):

        return None
    
    def setDefaultTakeName(self):

        return None
    

class ui():


    def curDesktop(self):

        return Desktop
    
    def desktop(self, name):

        return Desktop
    
    def desktops(self):

        return (Desktop, )
    
    def radialMenu(self, name):

        return RadialMenu
    
    def radialMenus(self):

        return (RadialMenu, )
    
    def createRadialMenu(self, name, label):

        return (RadialMenu, )
    
    def paneTabs(self):

        return (PaneTab, )
    
    def currentPaneTabs(self):

        return (PaneTab, )
    
    def floatingPaneTabs(self):

        return (PaneTab, )
    
    def paneTabOfType(self, type, index=object):

        return PaneTab
    
    def findPaneTab(self, name):

        return PaneTab
    
    def floatingPanels(self):

        return (FloatingPanel, )
    

class undos():


    def areEnabled(self):

        return True
    
    def disabler(self):

        return UndosDisabler
    
    def group(self, label):

        return UndosGroup
    
    def clear(self):

        return None
    
    def memoryUsage(self):

        return 0
    
    def memoryUsageLimit(self):

        return 0
    
    def performUndo(self):

        return None
    
    def performRedo(self):

        return None
    
    def undoLabels(self):

        return ("", )
    
    def redoLabels(self):

        return ("", )
    

class viewportVisualizers():


    def visualizers(self, category=object, node=None):

        return (ViewportVisualizer, )
    
    def createVisualizer(self, type, category=object, node=None):

        return ViewportVisualizer
    
    def copyVisualizer(self, source):

        return ViewportVisualizer
    
    def types(self):

        return (ViewportVisualizerType, )
    
    def type(self, name):

        return ViewportVisualizerType
    
    def isCategoryActive(self, category, node=None, viewport=None):

        return True
    
    def setIsCategoryActive(self, on, category, node=None, viewport=None):

        return True
    

def addNodeBundle(name=None):
    
    return NodeBundle


def allowEnvironmentToOverwriteVariable(name, onoff):
    
    return None


def almostEqual(x, y):
    
    return True


def appendSessionModuleSource(source):
    
    return None


def applicationCompilationDate():
    
    return ""


def applicationName():
    
    return ""


def applicationPlatformInfo():
    
    return ""


def applicationVersion():
    
    return (object, )


def applicationVersionString():
    
    return ""


def bezier():
    
    return 0.0


def cd(path):
    
    return None


def ch(path):
    
    return object


def chopExportConflictResolutionPattern():
    
    return ""


def chopNetNodeTypeCategory():
    
    return NodeTypeCategory


def chopNodeTypeCategory():
    
    return NodeTypeCategory


def chsop(path):
    
    return ""


def chsoplist(path):
    
    return ""


def clearAllSelected():
    
    return None


def commitPendingKeyframes():
    
    return None


def constant():
    
    return 0.0


def cop2NetNodeTypeCategory():
    
    return NodeTypeCategory


def cop2NodeTypeCategory():
    
    return NodeTypeCategory


def copyNodesTo(nodes, destination_node):
    
    return (Node, )


def copyNodesToClipboard(nodes):
    
    return None


def cubic():
    
    return 0.0


def currentDopNet():
    
    return Node


def currentSimulation():
    
    return DopNetNode


def cycle(start_frame, end_frame):
    
    return 0.0


def cycleoffset(start_frame, end_frame):
    
    return 0.0


def cycleoffsett(start_time, end_time):
    
    return 0.0


def cyclet(start_time, end_time):
    
    return 0.0


def defaultColor(color_item):
    
    return Color


def dopNodeTypeCategory():
    
    return NodeTypeCategory


def ease():
    
    return 0.0


def easein():
    
    return 0.0


def easeinp(ease_speed):
    
    return 0.0


def easeout():
    
    return 0.0


def easeoutp(ease_speed):
    
    return 0.0


def easep(ease_bias):
    
    return 0.0


def evalParm(path):
    
    return object


def evalParmTuple(path):
    
    return (0, )


def evaluatingParm():
    
    return Parm


def exit(exit_code=object, suppress_save_prompt=True):
    
    return None


def expandString(str):
    
    return ""


def expandStringAtFrame(str, frame_number):
    
    return ""


def expressionGlobals():
    
    return {}


def fileReferences(project_dir_variable=object, include_all_refs=True):
    
    return (Parm, )


def findDirectories(directory_name):
    
    return ("", )


def findDirectory(directory_name):
    
    return ""


def findFile(file_name):
    
    return ""


def findFiles(file_name):
    
    return ("", )


def findFilesWithExtension(file_extension, subdirectory=None):
    
    return ("", )


def fps():
    
    return 0.0


def frame():
    
    return 0.0


def frameToTime(frame):
    
    return 0.0


def getenv(name, default_value=None):
    
    return ""


def hdaDefinition(node_type_category, name, lib_path):
    
    return HDADefinition


def helpServerUrl():
    
    return ""


def homeHoudiniDirectory():
    
    return ""


def houdiniPath(path_variable=None):
    
    return ("", )


def hscript(command):
    
    return ("", )


def hscriptCommandHelp(command_name):
    
    return ""


def hscriptExpandString(str):
    
    return ""


def hscriptExpression(expression_string):
    
    return object


def hscriptFloatExpression(expression):
    
    return 0.0


def hscriptMatrixExpression(expression):
    
    return (object, )


def hscriptStringExpression(expression):
    
    return ""


def hscriptVectorExpression(expression):
    
    return (0.0, )


def imageResolution(image_file_name):
    
    return (0, )


def intFrame():
    
    return 0


def isApprentice():
    
    return True


def isUIAvailable():
    
    return True


def item(path):
    
    return NetworkMovableItem


def itemBySessionId(item_type, session_id):
    
    return NetworkMovableItem


def item(path_tuple):
    
    return (NetworkMovableItem, )


def licenseCategory():
    
    return EnumValue


def linear():
    
    return 0.0


def loadCPIODataFromString(data):
    
    return (("", "",),)


def loadIndexDataFromFile(file_path):
    
    return {}


def loadIndexDataFromString(data):
    
    return {}


def lvar(name):
    
    return 0.0


def managerNodeTypeCategory():
    
    return NodeTypeCategory


def match():
    
    return 0.0


def matchin():
    
    return 0.0


def matchout():
    
    return 0.0


def maxThreads():
    
    return 0


def moveNodesTo(nodes, destination_node):
    
    return (Node, )


def networkBoxBySessionId(session_id):
    
    return NetworkBox


def networkDotBySessionId(session_id):
    
    return NetworkDot


def node(path):
    
    return Node


def nodeBundle(name):
    
    return NodeBundle


def nodeBundles():
    
    return (NodeBundle, )


def nodeBySessionId(session_id):
    
    return Node


def nodeConnectionBySessionId(session_id, input_index):
    
    return NodeConnection


def nodeType(category, name):
    
    return NodeType


def nodeTypeCategories():
    
    return {"": NodeTypeCategory}


def nodes(path_tuple):
    
    return (Node, )


def objNodeTypeCategory():
    
    return NodeTypeCategory


def parent():
    
    return Node


def parm(path):
    
    return Parm


def parmClipboardContents():
    
    return (object, )


def parmTuple(path):
    
    return ParmTuple


def pasteNodesFromClipboard(destination_node):
    
    return None


def patternMatch(pattern_string, input_string, ignore_case=True):
    
    return 0


def phm():
    
    return HDAModule


def popNetNodeTypeCategory():
    
    return NodeTypeCategory


def popNodeTypeCategory():
    
    return NodeTypeCategory


def preferredNodeType(name, parent_node=None):
    
    return NodeType


def putenv(name, value):
    
    return None


def pwd():
    
    return Node


def qlinear():
    
    return 0.0


def quintic():
    
    return 0.0


def readFile(file_path):
    
    return ""


def releaseLicense():
    
    return None


def repeat(start_frame, end_frame):
    
    return 0.0


def repeatt(start_time, end_time):
    
    return 0.0


def root():
    
    return Node


def rootNodeTypeCategory():
    
    return NodeTypeCategory


def ropNodeTypeCategory():
    
    return NodeTypeCategory


def runVex(vex_file, inputs):
    
    return {"": object}


def saveCPIODataToString(data_tuples):
    
    return ""


def saveImageDataToFile(color_and_alpha_data, width, height, file_name):
    
    return None


def saveIndexDataToFile(file_path, index_data):
    
    return None


def saveIndexDataToString(data_dict):
    
    return ""


def selectedConnections():
    
    return (NodeConnection, )


def selectedItems(include_hidden=True):
    
    return (NetworkMovableItem, )


def selectedNodeBundles():
    
    return (NodeBundle, )


def selectedNodes(include_hidden=True):
    
    return (Node, )


def sessionModuleSource():
    
    return ""


def setChopExportConflictResolutionPattern(pattern):
    
    return None


def setCurrentDopNet(dopnet):
    
    return None


def setDefaultColor(color_item, color):
    
    return None


def setFps(fps):
    
    return None


def setFrame(frame):
    
    return None


def setMaxThreads(max_threads):
    
    return None


def setPwd(node):
    
    return None


def setSessionModuleSource(source):
    
    return None


def setSimulationEnabled(enabled):
    
    return None


def setTime(time):
    
    return None


def updateModeSetting():
    
    return EnumValue


def shopNodeTypeCategory():
    
    return NodeTypeCategory


def simulationEnabled():
    
    return True


def sopNodeTypeCategory():
    
    return NodeTypeCategory


def sortedNodePaths(path_tuple):
    
    return ("", )


def sortedNodePaths(node_tuple):
    
    return (Node, )


def spline():
    
    return 0.0


def stickyNoteBySessionId(session_id):
    
    return StickyNote


def subnetIndirectInputBySessionId(session_id):
    
    return SubnetIndirectInput


def time():
    
    return 0.0


def timeToFrame(time):
    
    return 0.0


def unsetenv(name):
    
    return None


def updateModeSetting():
    
    return EnumValue


def updateProgressAndCheckForInterrupt(percentage=object):
    
    return True


def vexContextForNodeTypeCategory(node_type_category):
    
    return VexContext


def vexContextForShaderType(shader_type):
    
    return VexContext


def vexContexts():
    
    return (VexContext, )


def vmatch():
    
    return 0.0


def vmatchin():
    
    return 0.0


def vmatchout():
    
    return 0.0


def vopNetNodeTypeCategory():
    
    return NodeTypeCategory


def vopNodeTypeCategory():
    
    return NodeTypeCategory
