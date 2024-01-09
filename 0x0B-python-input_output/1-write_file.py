#!/usr/bin/python3
"""
contains the function write_file
"""


def write_file(filename="", text=""):
    """override a file or  create new one"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
