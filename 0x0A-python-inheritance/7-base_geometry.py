#!/usr/bin/python3
"""
module to write class BaseGeo
metry (based on 6-base_geometry.py).
"""


class BaseGeometry():
    """class BaseGeometry declared"""
    pass

    def area(self):
        """method to raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
