#!/usr/bin/python3
"""
Module that defines a Rectangle class.

The Rectangle class represents a rectangle with methods to compute its area
and perimeter. It also includes property setters and getters for width and
height, with validation for the values. Additionally, it provides string

Example usage:
    rect = Rectangle(2, 4)
    print(rect.area())        # Outputs the area of the rectangle
    print(rect.perimeter())   # Outputs the perimeter of the rectangle
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

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
        Returns a string representation of the rectangle using '#' characters.

        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

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
