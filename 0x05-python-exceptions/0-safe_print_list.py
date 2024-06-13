#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    element = 0
    try:
        for count in range(x):
            print(my_list[count], end="")
            element += 1
    except IndexError:
        pass
    print()
    return element
