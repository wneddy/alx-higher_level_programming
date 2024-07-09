#!/usr/bin/python3
""""
module to read a text file
and print it out to stdout
"""


def read_file(filename=""):
    """method perform the operation"""
    with open(filename, encoding="utf-8") as f:
        output = f.read()
        print(output, end="")
