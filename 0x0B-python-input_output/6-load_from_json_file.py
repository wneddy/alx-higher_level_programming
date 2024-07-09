#!/usr/bin/python3
"""
module to creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """method to perform the operation"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
