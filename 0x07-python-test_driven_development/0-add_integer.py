#!/usr/bin/python3
"""function to add two integers"""

def add_integer(a, b=98):
    """function to return sum of a&b
    
    Args:
        a: first number.
        b: second number(dafault=98).

    Return:
        Sum of the two numbers in integer form.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    return int(a + b)
