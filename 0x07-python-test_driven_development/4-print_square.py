#!/usr/bin/python3
"""modeule to print a square."""


def print_square(size):
    """priting square function"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")

    for _ in range(size):
        print('#' * size)
