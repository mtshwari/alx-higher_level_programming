#!/usr/bin/python3
"""Module 8-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height.
    Attributes:
        number_of_instances: number of Rectangle instances,
        increments with every instantitation,
        decrements with every deletion
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:

