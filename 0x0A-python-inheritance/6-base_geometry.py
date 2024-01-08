#!/usr/bin/python3
"""
contains the class BaseGeometry
"""


class BaseGeometry:
    """Represent a BaseGeometry"""
    def __init__(self):
        """
            initialise the BaseGeometry
        """
        pass

    def area(self):
        """Raises an Exception  when called"""
        raise Exception('area() is not implemented')
