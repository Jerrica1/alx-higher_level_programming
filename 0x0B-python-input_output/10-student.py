#!/usr/bin/python3
"""
class_to_json function module.
Define class_to_json function.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure (list,
    dict, str, int and bool) for JSON serialization of an object
    obj: an instance of a class.
    """
    return obj.__dict__
