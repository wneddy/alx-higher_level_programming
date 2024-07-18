#!/usr/bin/python3
"""
class square and its methods
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class defination"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """method to get size"""
        return self.width

    @size.setter
    def size(self, valueSize):
        """method to set size"""
        self.width = valueSize
        self.height = valueSize

    def __str__(self):
        """returns the output of the attributes in aformated way"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.size}"
        )

    def update(self, *args, **kwargs):
        """method responsible for setting of args and kwargs"""
        if args:
            attri = ['id', 'size', 'x', 'y']
            for a, value in enumerate(args):
                if a < len(attri):
                    setattr(self, attri[a], value)
        else:
            for key, value in kwargs.items():
                if key in ['id', 'size', 'x', 'y']:
                    setattr(self, key, value)
