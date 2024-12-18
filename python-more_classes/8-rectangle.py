#!/usr/bin/python3
"""Module for creating rectangle class"""

class Rectangle:
    """
    A class that defines a rectangle with width and height.

    Attributes:
        number_of_instances (int): The number of instances of Rectangle.
        print_symbol (str): The symbol used for string representation of a rectangle.

    Methods:
        area() -> int: Returns the area of the rectangle.
        perimeter() -> int: Returns the perimeter of the rectangle.
        __str__() -> str: Returns a string representation of the rectangle.
        __repr__() -> str: Returns a representation of the rectangle.
        __del__() -> None: Handles deletion of instances and decreases the count.
        bigger_or_equal(rect_1, rect_2) -> Rectangle: Compares two rectangles by area.
    """
    
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            result += self.__width * str(self.print_symbol)
            if i != self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
