class AttrGroup(object):
    Group_Attributes = 5
    Group_Last = 6
    Group_Matrix = 4
    Group_None = -1
    Group_Object = 3
    Group_Points = 2
    Group_Primitives = 0
    Group_Vertices = 1

class AttrType(object):
    eFloatAttrib = 0
    eIntAttrib = 5
    eInvalidAttrib = -1
    eMatrix3Attrib = 8
    eMatrix4Attrib = 9
    eNormalAttrib = 4
    ePointerAttrib = 7
    eStringAttrib = 6
    eVector2Attrib = 1
    eVector3Attrib = 2
    eVector4Attrib = 3

class AttribContext(object):
    attribute=None
    #The attribute itself.
    channel=None
    #The channel number for the underlying attribute.
    group=None
    #What this attribute applies to (points, vertices, faces, etc.).
    name=None
    #The name for the attribute.
    recursive=None
    #Boolean value to indicate whether or not the attribute is applied recursively.
    type=None
    #The type of the attribute values.
    varying=None
    #Boolean value to indicate whether or not the attribute varies.
    def empty(self):
        """Whether this attribute is empty, i.e.
        """
        pass

class Attribute(object):
    name=None
    #The name for the attribute.
    type=None
    #The type of the attribute values.
    def invalid(self):
        return True
    def valid(self):
        return True


class GeoInfo(object):
    def attribContext(self, name, group, type):
        """
Gets an attribute context for the named attribute of this object.
list of (x,y,z) tuples"""
        return  AttribContext()

    def normals(self):
        """
Gets the list of vertex normals for this object.
PointList"""
        return ((0,0,0),)

    def points(self):
        """
Gets the point list for this object.
list of point index lists"""
        return PointList()

    def primitives(self):
        """
Gets the list of primitives which make up this object.
4x4 tuple of floats"""
        return [1,]

    def transform(self):
        """
Gets the transform matrix from the objects local coordinate system to world coordinates.
"""
        return (0,)

class GeometryList(object):
    def __getitem__(self, x, y):
        pass

class PointList(object):
    def __getitem__(self, x, y):
        pass

class Primitive(object):

    def averageCenter(self, pointlist):
        """
Get the average x,y,z location of all points in this primitive.
(x, y, z) """
        return (0,0,0)

    def faceAverageCenter(self, faceIndex, pointlist):
        """
Get the average x,y,z location of all points in a particular face.
list of int"""
        return (0,0,0)

    def faceVertices(self, faceIndex):
        """
Get the list of point indexes for a particular face.
int 	"""
        return [0,]

    def faces(self):
        """
Get the number of sub-faces this primitive generates.
(x, y, z) """
        return (0,0,0)

    def normal(self):
        """
Get the normal for this primitive.
list of int"""
        return (0,0,0)

    def points(self):
        """
Get the list of point indexes for this primitive."""
        return [0,]