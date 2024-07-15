#!/usr/bin/python3
"""
module to create class Rectangle inheriting from base class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class created"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization method for all the attributes"""
        self.__width = width
        self.__height = height
        self. __x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        if type(value) != int:
            raise("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y"""
        if type(value) != int:
            raise("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
