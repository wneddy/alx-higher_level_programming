#!/usr/bin/python3
"""
module to returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """method to perform operation"""
    return json.loads(my_str)
