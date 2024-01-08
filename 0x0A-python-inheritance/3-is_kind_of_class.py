#!/usr/bin/python3
"""
Contains the is_same_class function
"""


def is_kind_of_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return isinstance(obj, a_class)
