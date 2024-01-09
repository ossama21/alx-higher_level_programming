#!/usr/bin/python3
"""
Contains the function read_file
"""


def read_file(filename=""):
    """Reads a file and prints its content"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
