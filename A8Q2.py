import math

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def rotation(self):
        return math.degrees(math.atan2(self.y, self.x))
    
    @staticmethod
    def distance(v1, v2):
        return math.sqrt((v2.x - v1.x) ** 2 + (v2.y - v1.y) ** 2 + (v2.z - v1.z) ** 2)
    
    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
    
    @staticmethod
    def cross_product(v1, v2):
        if v1.z == 0 and v2.z == 0: 
            return v1.x * v2.y - v1.y * v2.x
        cx = v1.y * v2.z - v1.z * v2.y
        cy = v1.z * v2.x - v1.x * v2.z
        cz = v1.x * v2.y - v1.y * v2.x
        return Vector(cx, cy, cz)

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


def input_vector(dimensions):
    if dimensions == 2:
        x = int(input("Enter the x-component of the 2D vector: "))
        y = int(input("Enter the y-component of the 2D vector: "))
        return Vector(x, y)
    elif dimensions == 3:
        x = int(input("Enter the x-component of the 3D vector: "))
        y = int(input("Enter the y-component of the 3D vector: "))
        z = int(input("Enter the z-component of the 3D vector: "))
        return Vector(x, y, z)


vector_type = input("Enter vector type (2D/3D): ").strip().lower()

if vector_type == '2d':
    v1 = input_vector(2)
    v2 = input_vector(2)
elif vector_type == '3d':
    v1 = input_vector(3)
    v2 = input_vector(3)
else:
    print("Invalid vector type. Please enter '2D' or '3D'.")
    exit()

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")

print(f"Magnitude of v1: {v1.magnitude()}")
print(f"Rotation of v1: {v1.rotation()} degrees")
print(f"Distance between v1 and v2: {Vector.distance(v1, v2)}")
print(f"Dot product of v1 and v2: {Vector.dot_product(v1, v2)}")
print(f"Cross product of v1 and v2: {Vector.cross_product(v1, v2)}")
