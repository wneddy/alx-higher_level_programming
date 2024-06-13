#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    first = 0
    try:
        for elements in range(x):
            print("{:d}".format(my_list[elements]), end = "")
            first += 1
    except (ValueError, TypeError):
        pass
    print()
    return first
