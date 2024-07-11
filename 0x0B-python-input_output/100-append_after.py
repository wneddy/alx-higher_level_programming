#!/usr/bin/python3
"""module to define a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """method to insert text into a line enatiling a given string file"""
    txt = ""
    with open(filename) as i:
        for line in i:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
