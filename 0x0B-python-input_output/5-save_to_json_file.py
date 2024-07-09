#!/usr/bin/python3
"""
module to writes an Object to a text
file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """"method to perform the operation"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
