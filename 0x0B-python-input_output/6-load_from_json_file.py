#!/usr/bin/python3
"""
contains the function load_from_json_file
"""

import json


def load_from_json_file(filename):
    """reads objects from json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
