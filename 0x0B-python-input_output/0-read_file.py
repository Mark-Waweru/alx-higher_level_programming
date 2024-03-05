#!/usr/bin/python3
'''This module has a function read_file which reads the content of a file'''


def read_file(filename=""):
    '''Reads the content of a file

    Args:
        filename (object): The file to read content from
    '''
    with open(filename, encoding="UTF-8") as a_file:
        print("{}".format(a_file.read()), end="")
