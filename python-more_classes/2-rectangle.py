#!/usr/bin/python3
class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
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

# Test cases
if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area()))  # Expected output: "2 - 4 => 8"
    print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.perimeter()))  # Expected output: "2 - 4 => 12"

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.area()))  # Expected output: "10 - 3 => 30"
    print("{} - {} => {}".format(my_rectangle.width, my_rectangle.height, my_rectangle.perimeter()))  # Expected output: "10 - 3 => 26"
