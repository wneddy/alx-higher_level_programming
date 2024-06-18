#!/usr/bin/python3
"""coordination of a square"""


class Square:
    """declared class square"""

    def __init__(self, size=0, position=(0, 0)):
        """initilizine the instances.

        Agrs:
            size (int): size of the square.
            position (int): position coordinates.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """method to retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """method to set value to size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """method to retrive."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """method to set value to size"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """method to calculate area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """method to drawing art of the square with#"""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
