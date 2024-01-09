#!/usr/bin/python3
"""
contains the function save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object in a file with json"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
