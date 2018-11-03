class Matrix3(object):
    def set(self, v1,v2,v3,v4,v5,v6,v7,v8,v9):
        pass
    def makeIdentity(self):
        pass
    def rotateX(self, value):
        pass
    def rotateY(self, value):
        pass
    def rotateZ(self, value):
        pass
    def scale(self, x, y, z):
        return 0
    def scaling(self, x, y, z):
        return 0
    def transform(self, vector):
        pass
    def skew(self, value):
        pass
    def determinant(self):
        pass
    def identity(self):
        pass
    def inverse(self):
        return Matrix3()
    def rotate(self, vector_or_x, y=0, z=0, w=0):
        pass
    def rotation(self):
        pass
    def rotationX(self, value):
        pass
    def rotationY(self, value):
        pass
    def rotationZ(self, value):
        pass


class Matrix4(Matrix3):
    def set(self, v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16):
        pass
    def scaleOnly(self):
        pass
    def rotationOnly(self):
        pass
    def rotationsZXY(self):
        return (0,0,0)
    def mapQuadToUnitSquare(self, v1,v2,v3,v4,v5,v6,v7,v8,v9):
        pass
    def mapUnitSquareToQuad(self, v1,v2,v3,v4,v5,v6,v7,v8,v9):
        pass
    def ntransform(self, vector):
        return Vector3()
    def projection(self, v1, v2, v3, bol):
        pass
    def scaleAndRotationOnly(self):
        pass
    def skewXY(self):
        pass
    def translate(self):
        pass
    def transpose(self):
        pass
    def translationOnly(self):
        pass
    def vtransform(self, vector):
        return Vector3
    def xAxis(self):
        return Vector3
    def yAxis(self):
        return Vector3
    def zAxis(self):
        return Vector3

class Vector2(object):
    def __init__(self, x=0, y=0):
        pass
    def cross(self, vetor2):
        return Vector2()
    def distanceBetween(self):
        pass
    def distanceSquared(self):
        pass
    def dot(self):
        return 0
    def length(self):
        pass
    def lengthSquared(self):
        pass
    def negate(self):
        pass
    def normalize(self):
        pass
    def set(self):
        pass
    def x(self):
        pass
    def y(self):
        pass

class Vector3(Vector2):
    def __init__(self, x=0, y=0, z=0):
        super(Vector3, self).__init__()
        pass
    def distanceFromPlane(self):
        pass
    def fast_normalize(self):
        pass
    def maximum(self):
        pass
    def minimum(self):
        pass
    def reflect(self):
        pass
    def cross(self, vector3):
        return Vector3()

class Vector4(object):
    def x(self):
        pass
    def y(self):
        pass
    def z(self):
        pass
    def w(self):
        pass

class Quaternion(object):
    s=0.0
    vx=0.0
    vy=0.0
    vz=0.0
    def addInverse(self):
        pass
    def conjugate(self):
        pass
    def magnitude(self):
        pass
    def matrix(self):
        return Matrix4()
    def multInverse(self):
        return Quaternion()
    def set(self):
        pass
    def slerp(self):
        pass
