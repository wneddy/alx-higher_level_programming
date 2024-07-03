#!/usr/bin/python3
"""
module to Write a class MyInt that inherits from int
"""


class MyInt(int):
    """"class declared"""

    def __eq__(self, value):
        """inverting == and !="""
        return self.real != value

    def __ne__(self, value):
        """inverts != operator with == behavior."""
        return self.real == value
