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
        self.height = ValueSize

    def __str__(self):
        """returns the output of the attributes in aformated way"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.size}"
        )
