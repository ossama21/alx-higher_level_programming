#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """Represents a MyInt"""
    def __eq__(self, __value: object) -> bool:
        """Checks for equality"""
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        """Checks for non equality"""
        return super().__eq__(__value)
