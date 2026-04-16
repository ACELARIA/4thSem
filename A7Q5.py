import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

rectangle = Rectangle(5, 10)
circle = Circle(7)

print(f"Rectangle Area: {rectangle.area()}") 
print(f"Rectangle Perimeter: {rectangle.perimeter()}")  

print(f"Circle Area: {circle.area()}") 
print(f"Circle Perimeter: {circle.perimeter()}")  
