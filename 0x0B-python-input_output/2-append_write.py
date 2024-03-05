#!/usr/bin/python3
'''This module contains a function append_write that appends text to a file'''


def append_write(filename="", text=""):
    '''Appends a text to a file

    Args:
        filename (object): The file to append text to
        text (atr): The text to be appended

    Returns:
        int: The number of characters added'''
    with open(filename, mode="a+", encoding="UTF-8") as a_file:
        return a_file.write(text)
