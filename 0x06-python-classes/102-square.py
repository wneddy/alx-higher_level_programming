#!/usr/bin/python3
"""compare 2 squares"""


class Square:
    """declared class square"""

    def __init__(self, size=0):
        """method to initialize"""
        self.__size = size

    @property
    def size(self):
        """method to retrieve self size instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """ method to set size to value"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method to get area"""
        return (self.__size ** 2)

    def _equal(self, _2nd_sq):
        """method to return if comparison is equals"""
        if not isinstance(_2nd_sq, Square):
            return NotImplemented
        return self.area() == _2nd_sq.area()

    def _not_equal(self, _2nd_sq):
        """method to return if comparison is not equal"""
        if not isinstance(_2nd_sq, Square):
            return NotImplemented
        return self.area() != _2nd_sq.area()

    def _greater(self, _2nd_sq):
        """method to return if comparison is greater"""
        if not isinstance(_2nd_sq, Square):
            return NotImplemented
        return self.area() > _2nd_sq.area()

    def _greaterEqualto(self, _2nd_sq):
        """method to return if comparison is geater or equals to"""
        if not isinstance(_2nd_sq, Square):
            return NotImplemented
        return self.area() >= _2nd_sq.area()

    def _lessEqualto(self, _2nd_sq):
        """method to return if comparison is less than or equals to."""
        if not isinstance(_2nd_sq, Square):
            return NotImplemented
        return self.area() <= _2nd_sq.area()

    def _lessThan(self, _2nd_sq):
        """method to return if comparison is less than"""
        if not isinstance(_2nd_sq, Square):
            return NotImplemented
        return self.area() < _2nd_sq.area()
