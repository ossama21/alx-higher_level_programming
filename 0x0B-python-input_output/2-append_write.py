#!/usr/bin/python3
"""
contains the function append_write
"""


def append_write(filename="", text=""):
    """appends  a text at the end of a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
