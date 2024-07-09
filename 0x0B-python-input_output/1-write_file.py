#!/usr/bin/python3
"""
module to that writes a string to a
text file (UTF8) and returns the number
of characters written"""


def write_file(filename="", text=""):
    """method to perfome the operation"""
    with open(filename, mode="w", encoding="utf-8") as f:
        output = f.write(text)
        return output
