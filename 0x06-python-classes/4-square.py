#!/usr/bin/python3
"""methods to access and update attribute."""


class Square:
    """declared class square."""

    def __init__(self, size=0):
        """method to initialize instances.

        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """method to return size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setting the value in this method.

        Args:
            value (int): value to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """method to calculate area of the square."""
        return (self.__size ** 2)
