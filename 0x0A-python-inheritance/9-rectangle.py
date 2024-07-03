#!/usr/bin/python3
"""
module to Write a class Rectangle that
inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """declared child class rectangle"""

    def __init__(self, width, height):
        """method to initialize the args"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area implemenation"""
        return self.__width * self.__height

    def __str__(self):
        """str() and print() function implemention"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
