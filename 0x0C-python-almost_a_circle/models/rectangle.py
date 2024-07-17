#!/usr/bin/python3
"""
module to create class Rectangle inheriting from base class
"""
from models.base import Base


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
        for y in range(self.y):
            print()
        for h in range(self.height):
            print(' ' * self.x + "#" * self.width)

    def __str__(self):
        """method that outputs the args of the rectangle class"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args):
        """sets all the args in a ordered list"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
