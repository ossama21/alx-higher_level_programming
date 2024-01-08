#!/usr/bin/python3
"""
Contains the is_same_class function
"""


def inherits_from(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
