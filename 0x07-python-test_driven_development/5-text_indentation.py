#!/usr/bin/python3
"""
This is the "5-text_indentation" module
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """Indents a text"""

    if type(text) is not str:
        raise TypeError('text must be a string')
    seperators = ['?', '.', ':']
    flag = 0
    for ch in text:
        if flag == 0:
            if ch == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if ch in seperators:
                print("{}\n".format(ch))
                flag = 0
            else:
                print("{}".format(ch), end="")
