#!/usr/bin/python3
import json


"""
save_to_json_file function module.
Define save_to_json_file function.
"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file as JSON string.
    my_obj: the string to dump to JSON.
    filename (str): the file to write to.
    """
    with open(filename, 'w', encoding="UTF-8") as myfile:
        myfile.write(json.dumps(my_obj))
