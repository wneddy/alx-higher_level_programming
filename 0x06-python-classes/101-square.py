#!/usr/bin/python3
"""printing square instance"""


class Square:
    """declared class square"""

    def __init__(self, size=0, position=(0, 0)):
        """initilizing instances"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieving self instance"""

        return self.__size

    @size.setter
    def size(self, value):
        """"setting up size to value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returning self instance"""

        return self.__position

    @position.setter
    def position(self, value):
        """setting up position to value"""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """method to get square area of the square"""

        return self.size ** 2

    def my_print(self):
        """method to print self instances"""

        if self.size == 0:
            print()
            return

        x, y = self.position
        for _ in range(y):
            print()

        for _ in range(self.size):
            print(" " * x + "#" * self.size)

    def __str__(self):
        """method to print"""

        return self.my_print()
