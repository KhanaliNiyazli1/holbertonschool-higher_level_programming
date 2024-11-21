#!/usr/bin/python3
"""
This module defines an empty class Square.
"""


class Square:
    """A class that defines a square with its size."""
    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
            size: The size of the square.
        """
        self.__size = size

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

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#"*self.__size)
                end = "\n"
