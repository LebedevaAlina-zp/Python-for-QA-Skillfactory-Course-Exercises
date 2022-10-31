# 16.9.1. Create a class of any of the shapes (for example, a rectangle), where the attributes are set in the constructor:
# the initial coordinates x, y, width and height (or others, depending on the selected shape).
# Create a method that returns the rectangle attributes as a string. For a rectangle object with attribute values
# x = 5, y = 10, width = 50, height = 100, the method should return the string "Rectangle : 5, 10, 50, 100".
# 16.9.2. Get the shape's area.

import math

class Ellipse:
    def __init__(self, center_x, center_y, a, b):
        self.center_x = center_x
        self.center_y = center_y
        self.a = a
        self.b = b

    def __str__(self):
        return f'Ellipse: {self.center_x}, {self.center_y}, {self.a}, {self.b}'

    def getArea(self):
        return math.pi*self.a*self.b

ellipse_1 = Ellipse(0, 0, 10, 20)
ellipse_2 = Ellipse(a=10, b=10, center_x=20, center_y=30)
print(ellipse_1, ellipse_2)
print(ellipse_2.getArea())