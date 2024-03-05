#!/usr/bin/python3
'''This module contains a function that
inserts a line of text to a file, after each line containing a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts a line of text to a file
    after each line containing a specific string

    Args:
        filename (object): The file path of the file to read from
        search_string (str): The string to search for
        new_string (str): The strings or line ot add to the file
    '''
    with open(filename, mode="r", encoding="UTF-8") as my_file:
        lines = my_file.readlines()

    with open(filename, mode="w", encoding="UTF-8") as my_file:
        for line in lines:
            my_file.write(line)

            if search_string in line:
                my_file.write(new_string)
