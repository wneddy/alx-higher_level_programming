#!/usr/bin/python3
"""printing the square."""


class Square:
    """declared class square"""

    def __init__(self, size=0):
        """method to set instances

        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """method to retrieve self attribute."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """method to set size to value.

        Args:
            value (int): set value to size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method calculate area."""
        return (self.__size ** 2)

    def my_print(self):
        """method to prints the square."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
