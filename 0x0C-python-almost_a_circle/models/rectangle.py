#!/usr/bin/python3
"""
module to create class Rectangle inheriting from base class
"""
from models.base import Base
import os
import json

class Rectangle(Base):
    """Rectangle class created"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization method for all the attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, valueWidth):
        """setter method for width"""
        if not isinstance(valueWidth, int):
            raise TypeError("width must be an integer")
        if valueWidth <= 0:
            raise ValueError("width must be > 0")
        self.__width = valueWidth

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, valueHeight):
        """setter method for height"""
        if not isinstance(valueHeight, int):
            raise TypeError("height must be an integer")
        if valueHeight <= 0:
            raise ValueError("height must be > 0")
        self.__height = valueHeight

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, valueX):
        """setter method for x"""
        if not isinstance(valueX, int):
            raise TypeError("x must be an integer")
        if valueX < 0:
            raise ValueError("x must be >= 0")
        self.__x = valueX

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, valueY):
        """setter method for y"""
        if not isinstance(valueY, int):
            raise TypeError("y must be an integer")
        if valueY < 0:
            raise ValueError("y must be >= 0")
        self.__y = valueY

    def area(self):
        """method returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """method to print the rectangle with '#' symbol"""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """method that outputs the args of the rectangle class"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """sets all the args in a ordered list"""
        if args:
            attri = ['id', 'width', 'height', 'x', 'y']
            for a, value in enumerate(args):
                if a < len(attri):
                    setattr(self, attri[a], value)
        else:
            for key, value in kwargs.items():
                if key in ['id', 'width', 'height', 'x', 'y']:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary of class rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            list_dicts = json.load(file)
        return [cls.create(**d) for d in list_dicts]
