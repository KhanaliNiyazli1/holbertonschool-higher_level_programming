#!/usr/bin/python3
"""
This module defines an empty class Square.
"""


class Square:
    """A class that defines a square with its size."""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square.

        Args:
            size: The size of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            pos_from_left, pos_from_top = value
            if isinstance(pos_from_left, int) and isinstance(pos_from_top, int):
                if pos_from_left >= 0 and pos_from_top >= 0:
                    self.__position = value
                else:
                    raise ValueError("positions must be >= 0")
            else:
                raise TypeError("positions must be integers")
        else:
            raise TypeError("position must be a tuple of two integers")

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")

            for i in range(self.__size):
                print(" " * self.__position[0] + "#"*self.__size)
                end = "\n"
