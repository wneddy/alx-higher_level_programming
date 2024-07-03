#!/usr/bin/python3
"""
module to Write a class Square that inherits
from Rectangle (9-rectangle.py):
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """declared class square"""

    def __init__(self, size):
        """method to initilize instances"""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """method to get area"""
        return self.__size ** 2
