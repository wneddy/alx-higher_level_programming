#!/usr/bin/python3
"""module that prints a list in ascending order"""


class MyList(list):
    """declaration of class mylist"""
    def print_sorted(self):
        sortedList = sorted(self)
        return print(sortedList)
