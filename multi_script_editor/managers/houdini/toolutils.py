import hou

def sceneViewer():
    """ Returns an existing open Scene Viewer pane if there is one. A
        Context viewer is also acceptable is no dedicated scene viewer
        is found.
    """
    return hou.SceneViewer

def compositorViewer():
    """ Returns an existing open Compositing Viewer pane if there is one. A
        Context viewer is also acceptable is no dedicated compositing viewer
        is found.
    """
    return hou.CompositorViewer()

def activePane(scriptargs):
    """ Returns the current active pane. If the current tool was launched
        from a Tab menu, the "pane" scriptarg will be set, and indicates the
        active pane. Otherwise the tool was launched from the shelf and
        we have to look for an open viewer pane of the right type for the
        running tool.
    """
    return hou.SceneViewer()

def activeCompositorPane(scriptargs):
    return hou.CompositorViewer ()

def homeToSelectionNetworkEditorsFor(node):
    """ Homes to their selection all network editors to that are showing the 
    network that contains node. """
    pass
def selectionPrompt(nodetypecategory, multisel = True,
                    whichprompt = 0):
    """ Generates a generic selection prompt string when no specific prompt
        string is available in the toolprompts module.
    """
    return ''

def replaceOutputConnections(oldnode, oldoutputindex, newnode, newoutputindex):
    """ Stick the new node between the input node and all nodes it
        is connected to (insert operation).
    """
    pass

def connectInputsAndOutputs(newnode, branch,
                            inputnode, outputnode,
                            inputindex, outputindex):
    """ Wire the network so that new node has as its first input
        inputnode, using the outputindexth output of inputnode.
        outputnode has its inputindexth input wired into newnode.
        If branch is false, all of inputnode's outputs will be made
        newnode's outputs.  Both inputnode and outputnode are
        optional.
    """
    pass

def nodeTypeNameBase(node):
    """ Returns the node type base name (stripped of namespace or version).
    """
    return ('',)

def nodeTypeNameVersion(node):
    """ Returns the node type version component.
    """
    return ('',)

def nodeTypeNameMatches(node, matchtype):
    """ Returns true if the node's type base name matches the given type.
        A matchtype of None is assumed to match any node.
    """
    return True

def nodeTypeBaseNameMatches(node, matchtype):
    """ Returns true if the node's type base name matches the given type.
        A matchtype of None is assumed to match any node.
    """
    return True

def nodeTypeNameComponentsMatch(node, matchtype):
    """ Returns true if the node's type name components matches the given type.
        The components present in matchtype are checked against the node's type,
        and this function returns true if they do match.  Eg, 
        matchtype 'hda' will match 'hda', 'hda::1.5', 'userX::hda', etc
        matchtype 'userX::hda' will match 'userX::hda', 'userX::hda::1.5', etc
        matchtype 'hda::1.5' will match 'hda::1.5', 'userX::hda::1.5', etc
        matchtype '::hda' will match 'hda' and 'hda::1.5', but not 'userX::hda'
        matchtype 'hda::' will match 'hda' and 'userX::hda' but not 'hda::1.5'
        A matchtype of None is assumed to match any node.
    """
    return True

def __nodeMatches(node, matchtype, parmlist, basetypematch=False):
    """ True if node is of type matchtype and the parmlist dictionary
        matches our contents. 
        If basetypematch is true, only the node type's base name is checked, 
        ie, node type's namespace and version components are ignored
        when testing against the matchtype (eg, matchtype 'hda' will match
        node types 'hda', 'hda::1.5' and 'userx::hda', etc). Otherwise,
        the node type full name must match exactly the matchtype string.
    """
    return True

def findInputNodeOfTypeWithParms(endnode, nodetype, parmlist, 
                                includeme=False, seennodes=None,
                                basetypematch=False):
    """Finds any nodes that are an ancestor of endnode, match
        nodetype, and have the parameters & value pairs listed in the
        parmlist dictionary.
        If basetypematch is true, only the node type's base name is checked, 
        ie, node type's namespace and version components are ignored
        when testing against the matchtype (eg, matchtype 'hda' will match
        node types 'hda', 'hda::1.5' and 'userx::hda', etc). Otherwise,
        the node type name must match exactly the matchtype string.
    """

    return hou.Node()

def findGreatestCommonDescendent(endnode, searchnodes, seennodes=None):
    """ Starting from end node and heading up the input chain
        locate the first node that doesn't have all of searchnodes
        on the same input wire.
    """
    return hou.Node()

def findInputNode(endnode, searchnode, seennodes=None):
    """ This function searches the endnode's hierarchy to find if the
        given search node is connected
    """
    return hou.Node()

def findInputNodeOfType(endnode, nodetype, includeme=False, seennodes=None,
                        basetypematch=False):
    """ This function does a depth first traversal of the node input hierarchy
        to find the first node of a particular type.
        If basetypematch is true, only the node type's base name is checked, 
        ie, node type's namespace and version components are ignored
        when testing against the matchtype (eg, matchtype 'hda' will match
        node types 'hda', 'hda::1.5' and 'userx::hda', etc). Otherwise,
        the node type name must match exactly the matchtype string.
    """
    parmlist = {}
    return findInputNodeOfTypeWithParms(endnode, nodetype, parmlist,
                            includeme=includeme, seennodes=seennodes,
                            basetypematch=basetypematch)

def findInputNodeOfBaseType(endnode, nodetype, includeme=False, seennodes=None):
    """ This function does a depth first traversal of the node input hierarchy
        to find the first node whose type's base name (ie, type name stripped of
        any namespace or version) matches the given type.
    """
    return findInputNodeOfType(endnode, nodetype, includeme, seennodes, 
                              basetypematch = True)

def findOutputNodeOfTypeWithParms(startnode, nodetype, parmlist, 
                                includeme=False, seennodes=None,
                                basetypematch=False, returnall=False):
    """ Finds any nodes that are a descendent of startnode, match
        nodetype, and have the parameters & value pairs listed in the
        parmlist dictionary.
        If basetypematch is true, only the node type's base name is checked, 
        ie, node type's namespace and version components are ignored
        when testing against the matchtype (eg, matchtype 'hda' will match
        node types 'hda', 'hda::1.5' and 'userx::hda', etc). Otherwise,
        the node type name must match exactly the matchtype string.
        If returnall is true, returns a list of all matches in depth
        first order, or an empty list if no matches are found.
    """
    return hou.Node()

def findOutputNodeOfType(startnode, nodetype, includeme=False, seennodes=None,
                         basetypematch=False, returnall=False):
    """ This function does a depth first traversal of the node output
        hierarchy to find the first node that matches our search.
        If basetypematch is true, only the node type's base name is checked, 
        ie, node type's namespace and version components are ignored
        when testing against the matchtype (eg, matchtype 'hda' will match
        node types 'hda', 'hda::1.5' and 'userx::hda', etc). Otherwise,
        the node type name must match exactly the matchtype string.
        If returnall is true, returns a list of all matches in depth
        first order, or an empty list if no matches are found.
    """
    parmlist = {}
    return findOutputNodeOfTypeWithParms(startnode, nodetype, parmlist,
                        includeme=False, seennodes=seennodes,
                        basetypematch=basetypematch, returnall=returnall)

def findOutputNodeOfBaseType(endnode, nodetype, includeme=False, 
                             seennodes=None, returnall=False):
    """ This function does a depth first traversal of the node input hierarchy
        to find the first node whose type's base name (ie, type name stripped of
        any namespace or version) matches the given type.
        If returnall is true, returns a list of all matches in depth
        first order, or an empty list if no matches are found.
    """
    return findOutputNodeOfType(endnode, nodetype, includeme, seennodes, 
                                basetypematch = True, returnall=returnall)

def findAllChildNodesOfTypeWithParms(parentnode, nodetype, parmlist,
                                 dorecurse=False, findfirst=False,
                                 basetypematch=False):
    """ Returns a list of all nodes contained in parent that match
        the nodetype & parmlist filters.
    """
    return []

def findAllChildNodesOfType(parentnode, nodetype,
                                 dorecurse=False, findfirst=False,
                                 basetypematch=False):
    """ Returns a list of all nodes contained in parent that match
        the nodetype.
    """
    return []

def findChildNodeOfTypeWithParms(parentnode, nodetype, parmlist,
                                 dorecurse=False, basetypematch=False):
    """ This function does a search of the node container hierarchy
        (rather than connection hierarchy) searching for a matching
        node type which also has the given parameter list match.
    """
    return hou.Node()

def findChildNodeOfType(parentnode, nodetype, dorecurse=False, basetypematch=False):
    """ This function does a search of the node container hierarchy
        (rather than connection hierarchy) searching for a matching
        node type.
    """
    return hou.Node()

def findAllChildNodesOfType(parentnode, nodetype, dorecurse=False, basetypematch=False):
    """ Returns a list of all child nodes that match the given node
        type
    """
    return hou.Node()

def findAncestorOfType(startnode, category, nodetype, basetypematch=False):
    """ Return closest ancestor (or self) of 'startnode' with the specified
        category and type.
    """
    return hou.Node()

def findAncestorOfBaseType(startnode, category, nodetype):
    """ Return closest ancestor (or self) of 'startnode' with the specified
        category and type.
    """
    return findAncestorOfType(startnode, category, nodetype,
                              basetypematch=True)

def chooseNode(possible_nodes, title, message):
    """ Prompts the user to select on of the given nodes. If there is only a
        single node, then that node is automatically returned. The title
        and message parameters determine what will show up in the prompt.
    """  
    return hou.Node()

def _askUserToSelectNode(nodes, title, message):
    return hou.Node()

class OrientInfo:
    def __init__(self, parmname, defaultup=hou.orientUpAxis.Y):
        self.parmname = parmname
        self.defaultup = defaultup

def setUpOrientation(node, parmname, defaultup):
    """ Assumes that the default value of the specified parameter in the given
        node corresponds to the orientation specified in defaultup and applies
        the necessary change to convert the node to the current orientation
        mode.
    """
    pass

def parseDialogScriptMenu(filename, defchoices=[]):
    """This function parses a disk file specified by the filename.
       The file is parsed such that comments ('#') are stripped and
       lines containing exactly 2 arguments are printed out.  Quotes
       are handled.

       The function can be used by dialog script menus which want to
       generate dynamic menus based on disk files.

       The dynamic menu should have the script:
            echo `pythonexprs("__import__('toolutils').parseDialogScriptMenu(filename, [('token1', 'label1'), ('token2', 'label2'), ...])")`
       the diskfile will be searched in the Houdini path.  If the disk
       file isn't found, the default choices will be used instead.
    """
    return ''  # Return a string of the menu choices

def updatePlaneType(planeindex, variable):
    """This function is intended to update deep raster plane parameters
       based on the newly set plane variable name.  Use this in a callback
       script as follows:

       callback "`pythonexprs(\"__import__('toolutils').updatePlaneType($script_multiparm_index, \'$script_value\')\")`"
    """
    pass

def mapTypeCategoriesToSubnetName(nodetypecategory, acceptedtypecategory):
    """This function returns a name of the subnet that accepts nodetypecategory
       as child type and can be created in a container whose child type is 
       acceptedtypecategory. 
       Returns None if these two categories are the same (ie, no need for 
       a subnet to accommodate nodetypecategory). Also returns None if
       the mapping has not been defined yet.
    """
    return ''

def removeDefaultGeometryObjectContents(objectnode):
    """ Destroy the File SOP that gets created inside a default Geometry
        Object.
    """
    pass

def createNodeInContainer(container, nodetypecategory, nodetypename, nodename,
                          exact_node_type):
    """This function attempts to create a node of a given type category and
       type name in a given container. If the container does not allow a given 
       type category, this funciton creates a network of a correct type first,
       and then creates the required node within that network.
       If exact_node_type is true, it attempts to create a node of the exact
       nodetypename; otherwise, the nodtypename may be resolved to the
       preferred namespace or version of that typename.
       It retuns a pair of nodes, the fist being the node created in the
       container and the second being the node of a required operator type
       (which in most cases will be the same nodes).
    """
    return (hou.Node(),hou.Node())

def reformatPermissionErrors(function):
    """This function decorator will trap any permission error exceptions and
       raise a different exception with a nicer message."""
    def new_func(*args, **kwargs):
        pass
    return new_func

@reformatPermissionErrors
def genericTool(scriptargs, nodetypename, nodename=None, nodetypecategory=None,
                exact_node_type=True):
    """ Handles the creation of any node in a Network Editor pane. 

        This function is intended to instantiate a node of a given type from
        shelf tools, and thus, if exact_node_type argument is True, it creates 
        the node of the exact type specified by nodetypename. 
        However, if exact_node_type argument is False, then the base type may 
        get resolved to another namespace or another version, and 
        the created node may be of that resolved type (eg 'hda' may resolve to 
        'mynamespace::hda::2.0').
    """
    return hou.Node()

def _getBranchMode(scriptargs):
    """Utility function to convert the "branch" key in scriptargs into a
       hou.stateGenerateMode enum.
    """
    if scriptargs.has_key("branch") and scriptargs["branch"]:
        return hou.stateGenerateMode.Branch
    else:
        return hou.stateGenerateMode.Insert

def _getRequestNew(scriptargs):
    """Utility function to convert the "requestnew" key in scriptargs into a
       boolean.
    """
    return scriptargs.has_key("requestnew") and scriptargs["requestnew"]

def genericStateTool(scriptargs, statename):
    """ Runs a specific state in an open viewer pane. """
    pass

def moveNodesToGoodPosition(movenodes):
    """ Moves a list of nodes to good positions. """
    pass

def generateToolScriptForNode(nodepath_or_list, input_nodepath = None, output_nodepath = None):
    return ''

def _createModule(module_name, source):
    """Create and return a module-like object with the given name from the
       given source code.  This module will not appear in sys.modules.  If
       the source code has a syntax error, an exception will be raised.
    """
    # Create a module-like object object and return it.
    class ModuleWrapper:
        pass
    module = ModuleWrapper()
    module.__dict__ = {}
    return module

def createModuleFromSection(module_name, node_type, section_name):
    """Create and return a module-like object with the given name from the
       contents of a section in an HDA.  This module will not appear in
       sys.modules.  If the source code has a syntax error, an exception will
       be raised.  Use this function to create submodules in the PythonModule
       section of an HDA.  For example:
           submod = toolutils.createModuleFromSection(
                'submod', kwargs['type'], 'PythonSubmod')
    """
    return _createModule(module_name,
        node_type.definition().sections()[section_name].contents())

def nodeNameFromTypeName(nodetypename):
    """Given an operator node type name, return a valid node name
       corresponding to that type. For example, if the type name contains
       any namespace or version components, they are stripped off.
       The returned node name contains only characters that are allowed
       to appear in the node names.
    """
    components = hou.hda.componentsFromFullNodeTypeName(nodetypename)
    return components[2]

def placeToolImmediately(kwargs):
    """ Returns true if the provided kwargs has a modifier key suggesting
        the tool be placed right away.  This is a ctrl click or a cmd click
        depending on the platform.
    """
    return False
