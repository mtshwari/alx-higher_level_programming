#!/usr/bin/python3
"""
A Rectangle Class with public class attributes, private instance attributes
(width, height), public methods, special methods,
static methods and class methods
"""


class Rectangle():
    """
    A Rectangle Class with public class attributes,
    private instance attributes width, height, public methods,
    special methods, static methods and class methods.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructor of the class Rectangle
          Args:
            - width (default = 0): int
            - heigth (default = 0): int
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Calculate the area of a Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter of a Rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Function to print a Square with the print_symbol
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        final = [str(self.print_symbol) * self.__width
                 for character in range(self.__height)]

        return '\n'.join(final)

    def __repr__(self):
        """Returns an “official” string representation of a Rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):

