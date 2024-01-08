#!/usr/bin/python3
"""
contains the class BaseGeometry
"""


class BaseGeometry:
    """Represent a BaseGeometry"""

    def area(self):
        """Raises an Exception  when called"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates an integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
