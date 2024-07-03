#!/usr/bin/python3
"""
module to Write a class Square that inherits
from Rectangle (9-rectangle.py):
"""


class BaseGeometry:
    """class BaseGeometry declared"""

    def area(self):
        """method to raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """declared child class rectangle"""

    def __init__(self, width, height):
        """method to initialize the args"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area implementation"""
        return self.__width * self.__height

    def __str__(self):
        """str() and print() function implementation"""
        return f"[Rectangle] {self.__width}/{self.__height}"


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
