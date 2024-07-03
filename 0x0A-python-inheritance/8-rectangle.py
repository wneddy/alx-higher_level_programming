#!/usr/bin/python3
"""
module that creates class rectangle
that inherits from BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle declared"""

    def __init__(self, width, height):
        """method to initialize instances"""
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
