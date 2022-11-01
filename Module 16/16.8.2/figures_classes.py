# Here are the created classes: Rectangle, Square and Circle, for each one can get its area.
# Task 16.10.5. Add your own NonPositiveDigitException to the Square class constructor, inherited from ValueError, 
# which is triggered when the side of the square is less than or equal to 0.

import math

class NonPositiveDigitException(ValueError):
    pass

class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise NonPositiveDigitException("The rectangle's width and height can't take negative values or 0")
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
        if side <= 0:
            raise NonPositiveDigitException("The square's side can't take negative values or 0")
        self.side = side

    def getArea_square(self):
        return self.side**2


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise NonPositiveDigitException("The circle's radius can't take negative values or 0")
        self.radius = radius

    def getArea_circle(self):
        return math.pi*self.radius**2
