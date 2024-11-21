#!/usr/bin/python3
"""
This module defines a class Square with size and position.
"""

class Square:
    """A class that defines a square with its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): A tuple of two integers representing the position (x, y) (default (0, 0)).
        """
        self.size = size  # Uses the setter to ensure validation
        self.position = position  # Uses the setter to ensure validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        # Validate that position is a tuple of exactly 2 integers
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        # Check that both values in the tuple are integers
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        # Check that both values in the tuple are positive integers
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters, with the specified position."""
        if self.__size == 0:
            print("")  # If size is 0, just print an empty line
        else:
            # Print the vertical position (number of empty lines before the square starts)
            for _ in range(self.__position[1]):
                print("")

            # Print the square with horizontal position (spaces before each line of the square)
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
#!/usr/bin/python3
"""
This module defines a class Square with size and position.
"""

class Square:
    """A class that defines a square with its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): A tuple of two integers representing the position (x, y) (default (0, 0)).
        """
        self.size = size  # Uses the setter to ensure validation
        self.position = position  # Uses the setter to ensure validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        # Validate that position is a tuple of exactly 2 integers
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        # Check that both values in the tuple are integers
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        # Check that both values in the tuple are positive integers
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters, with the specified position."""
        if self.__size == 0:
            print("")  # If size is 0, just print an empty line
        else:
            # Print the vertical position (number of empty lines before the square starts)
            for _ in range(self.__position[1]):
                print("")

            # Print the square with horizontal position (spaces before each line of the square)
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
