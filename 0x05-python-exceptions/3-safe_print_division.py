#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        quontient = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        quontient = None
    finally:
        print("Inside result: {}".format(quontient))
        return quontient
