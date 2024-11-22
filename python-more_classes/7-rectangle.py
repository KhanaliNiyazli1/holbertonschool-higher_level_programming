#!/usr/bin/python3
"""
Module that defines a Rectangle class.

The Rectangle class represents a rectangle with methods to compute its area
and perimeter. It also includes property setters and getters for width and
height, with validation for the values. Additionally, it provides string
representations of the rectangle and prints a message when an instance is deleted.
"""

class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (str): The symbol used to represent the rectangle when printed.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        __str__(): Returns a string representation of the rectangle using
                   the print_symbol.
        __repr__(): Returns the official string representation of the
                    rectangle.
        __del__(): Prints a message when the object is deleted.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
            If width or height is 0, the perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the print_symbol.

        Returns:
            str: A string representation of the rectangle, or an empty string if
            the rectangle has 0 width or 0 height.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.width] * self.height
        )

    def __repr__(self):
        """
        Returns the official string representation of the rectangle.

        Returns:
            str: The official string representation of the rectangle, suitable
            for recreating a new instance with eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Prints a message when the instance is deleted.

        This method is called when the object is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
