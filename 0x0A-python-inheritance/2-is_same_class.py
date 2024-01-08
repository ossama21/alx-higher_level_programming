#!/usr/bin/python3
"""
Contains the is_same_class function
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return type(obj) is a_class
