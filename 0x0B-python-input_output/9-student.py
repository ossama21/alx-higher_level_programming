#!/usr/bin/python3
"""
contains the class student
"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initialise a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dict representation of a student"""
        return self.__dict__
