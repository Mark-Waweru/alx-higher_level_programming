#!/usr/bin/python3
'''This module has a function write_file that writes text to a file'''


def write_file(filename="", text=""):
    '''Writes text to a file

    Args:
        filename (object): The file to write the text to
        text (str): The strings of text to write to the file

    Returns:
        int : The number of characters written
    '''
    with open(filename, mode="w", encoding="UTF-8") as a_file:
        return a_file.write(text)
