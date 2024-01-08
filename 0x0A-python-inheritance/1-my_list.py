#!/usr/bin/python3
"""
Contains MyList class
"""


class MyList(list):
    """MyList class inheriting from list"""
    def __init__(self):
        """Initialise the class"""
        pass

    def print_sorted(self):
        """Prints the list in ascending order"""
        new_list = self.copy()
        new_list.sort(reverse=False)
        print(new_list)
