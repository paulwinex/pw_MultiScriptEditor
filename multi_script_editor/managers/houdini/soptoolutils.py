import hou
def scriptSopFilterTool(scriptargs,
                        nodetypename, 
                        nodename=None,
                        center_on_selection=False,
                        translate_parm_name=None,
                        connected_selection=True,
                        orient=None,
                        exact_node_type=True):
    """ Creates a new script operator (OTL) that operates on
        existing geometry.  This can be used when no generic tool exists
        for the desired operator.
    """
    pass

def findDeformTypeInputSop(endnode):
    """ This function does a depth first traversal of the node
        input hierarchy to find the first deform-type node.
        Returns the deform-type node.  Returns None if no such node exists.
    """
    return hou.Node()

def getGeometrySelections(sceneviewer, selectors, allow_obj_selection=True,
                          prompt = None):
    """ This function invokes a geometry selection for each
        selector in "selectors".  The selector is not started, but
        its properties are used when calling sceneviewer.selectGeometry().
    """
    return (None,[], hou.Node())

def setGroupParmsOnSopNode(node, selector, selection):
    """ Sets the group type and group parameters on the given node
        based on the selection info.
    """
    # Figure out the group type parameter value if we want it.
    pass

def initReusedSopFilterNode(reusednode, selections, container):
    pass
    
def initNewSopFilterNodeWithOutput(branch, newnode, selections,
                                   container, outputnode,
                                   force_keep_original_objects=False):
    pass
def initNewSopFilterNode(branch, newnode, selections, container,
                         force_keep_original_objects=False):
    pass

def createSopNodeContainer(sceneviewer, newobjectname, merge_context = False,
                           merge_creator = None):
    """ Creates a scene level object node to contain a new SOP node.
        This function may return an existing object node if the Model in
        Context option is turned on, or the merge_context parameter is
        set to True.
    """
    return hou.Node()

def createSopNodeFilter(container, nodetypename, nodename, exact_node_type):
    """ Creates a SOP node that takes an input. """
    # Look at the type of nodes that go inside the current node.
    return hou.Node()

def createSopNodeGenerator(container, nodetypename, nodename,
                           merge_context = False,
                           exact_node_type = True):
    """ Creates a SOP node that doesn't require an input. If the container
        already has nodes, this new SOP may be merged with the existing SOPs.
    """
    # Look at the type of nodes that go inside the current node.
    return hou.Node()

def genericSopNodeGeneratorTool(scriptargs, nodetypename, nodename,
                                merge_context = False,
                                prompt = None,
                                exact_node_type = True):
    """ A generic tool for instantiating SOP generator nodes such as Box and
        Sphere. The user is prompted to select a location in the viewport if
        the tool was not invoked with the Ctrl key. The new SOP may be merged
        into an existing scene level object depending onthe merge_context
        parameter value.
    """
    return hou.Node()

def genericSopNodeFilterTool(scriptargs, nodetypename, nodename,
                             isreusable=False, iscapture=False,
                             allow_obj_sel=True, selector_indices=(),
                             exact_node_type=True):
    """ A generic tool for creating a SOP node that takes another SOP node
        as input. The user is prompted for selections based on the selector
        bindings set in the OPbindings file.
    """
    return hou.Node()

def customSopNodeFilterTool(scriptargs, activepane, nodetypename,
                            prompt = None, exact_node_type = True):
    pass

def genericCaptureTool(scriptargs, nodetypename, nodename = None):
    """ Invokes a generic capture-type SOP tool. """
    return genericReusableTool(scriptargs, nodetypename, nodename, True)

def genericReusableTool(scriptargs, nodetypename, nodename = None,
                        iscapture = False):
    """ Invokes a generic reusable SOP tool.
        If iscapture is True, then the tool is considered to be a capture-type
        tool.  Capture-type tools will attempt to create new nodes before
        any deform-type SOPs in the network.
    """
    return genericTool(scriptargs, nodetypename, nodename, True, iscapture)

def customStateTool(scriptargs, nodetypename, nodename = None):
    """ Invokes a custom SOP tool. This differs from genericTool() in that the
        custom state has custom selectors. For filters, we prompt for a single
        object, then enter into it before entering the custom state.
    """
    return genericTool(scriptargs, nodetypename, nodename, custom=True)

def genericTool(scriptargs, nodetypename, nodename = None,
                isreusable = False, iscapture = False, allow_obj_sel=True,
                custom=False, merge_context=False, orient=None,
                exact_node_type = True,
                force_filter = False):
    """ Invokes a generic SOP tool.
        If isreusable is True, then the tool will try to reuse existing
        nodes of matching type in the network before creating any new nodes.
        If iscapture is True, then the tool is considered to be a capture-type
        tool.  Capture-type tools will attempt to create new nodes before
        any deform-type SOPs in the network.
        If merge_context is True, then we create the generator in context,
        while merging it together with the current display sop.
        If orient is set, it should be an instance of OrientInfo.
        If exact_node_type is True, it creates the node of the exact type 
        specified by nodetypename.  However, if exact_node_type is False, 
        then the base type may get resolved to another namespace or 
        another version, and the created node may be of that resolved type 
        (eg 'hda' may resolve to 'mynamespace::hda::2.0').
        If force_Filter is True, we will treat as a filter even if
        it can optionally have no inputs.
    """
    return hou.Node()

def chooseAndOpenGeoFile(scriptargs, click_to_place):
    """ Opens a file chooser that allows the user to select a geometry file(s).
    For each chosen file, a File SOP node is created to open that file.
    The 'click_to_place' determines whether the user needs to click on the
    construction plane to place the geometry, or whether it will be placed
    automatically at the world origin."""

    pass


def buildPaintNode(node, nextnode, parms, props):
    """ Finds a paint node at or prior to node which matches parms.
        If not found, builds one.  If the attribute does not exist,
        creates the attribute to paint.
        It will be inserted prior to nextnode if not none.
    """
    return hou.Node()

def chooseAndPaintObject(scriptargs, attribname, props, prompt=None, objfilter=None):
    """ Interactively selects an object in which to paint an attribute and
        enters the paint state.  Existing Paint SOPs will be reused.
        Otherwise, an Attribute Create SOP (if necessary) and a Paint SOP will
        be appended.
    """
    pass

def chooseAndPaintEaseInObject(scriptargs, attribname, props, prompt=None, objfilter=None):
    """ Interactively selects an object in which to paint an attribute with
        ease-in and ease-out properties.
    """
    pass
                
def chooseAndApplyTexture(scriptargs, attribname, props, prompt=None, objfilter=None):
    """ Interactively selects an object to apply fluid map operator on
    """
    pass
