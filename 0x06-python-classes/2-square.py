#!/usr/bin/python3
"""file contains class defination of Square."""


class Square:
    """Declared class Square."""

    def __init__(self, size=0):
        """method to assign initialize instances.

        Args:
            size (int): size of the square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

