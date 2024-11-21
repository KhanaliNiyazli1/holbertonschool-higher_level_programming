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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
