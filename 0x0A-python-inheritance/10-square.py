#!/usr/bin/python3
"""
Contains the class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square"""
    def __init__(self, size):
        """Initialise the Square"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of a Square"""
        return self.__size ** 2
