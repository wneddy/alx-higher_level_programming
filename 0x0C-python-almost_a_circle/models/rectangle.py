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
        return self.width

    @property
    def height(self):
        """get height"""
        return self.height

    @property
    def x(self):
        """get x"""
        return self.x

    @property
    def y(self):
        """get y"""
        return self.y
