#!/usr/bin/python3
"""
module to returns the JSON representation
of an object (string)
"""
import json


def to_json_string(my_obj):
    """method to perform the operation"""
    return json.dumps(my_obj)
