#!/usr/bin/python3
def safe_print_integer(value):

    """ Prints an integer value to the console.

    Parameters:
        value (int): The integer value to be printed.

    Returns:
        bool: True if the value was successfully printed, False otherwise.
    """

    try:
        print("{:d}".format(value))
        print()
        return True
    except ValueError:
        return False
