#!/usr/bin/python3
"""
This is the "5-text_indentation" module
The 5-text_indentation module supplies one function, text_indentation(text).
"""

def text_indentation(text):
    """Indents a text"""
    result = []
    separator = ("?", ".", ":")
    new_word = ""
    if type(text) is not str:
        raise TypeError('text must be a string')
    for ch in text:
        if new_word == "" and ch == " ":
            continue
        if ch not in separator:
            new_word += ch
        else:
            if new_word:
                new_word += ch
                print("{}\n".format(new_word))
                new_word = ""
    
