# The task is to create a few figures of the classes imported from figure_classes file, place them into a list
# and print their areas with the methods of corresponding classes.

from figures_classes import Rectangle, Square, Circle

rect_1 = Rectangle(10,5)
rect_2 = Rectangle(12,15)

square_1 = Square(5)
square_2 = Square(6)

circle_1 = Circle(1)
circle_2 = Circle(10)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Rectangle):
        print(figure.getArea())
    elif isinstance(figure, Square):
        print(figure.getArea_square())
    else:
        print(figure.getArea_circle())

