#!/usr/bin/python3
"""class that defines area of a square."""


class Square:
    """declared class square."""

    def __init__(self, size=0):
        """method to initialize instances.

        Args:
            size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method to calculate area of the square."""
        return (self.__size ** 2)
