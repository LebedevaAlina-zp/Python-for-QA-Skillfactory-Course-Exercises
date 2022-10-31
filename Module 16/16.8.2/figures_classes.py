# Here are the created classes: Rectangle, Square and Circle, for each one can get its area.

import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
# Method to calculate the area
    def getArea(self):
        return self.width * self.height


class Square:
    def __init__(self, side):
        self.side = side

    def getArea_square(self):
        return self.side**2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea_circle(self):
        return math.pi*self.radius**2
