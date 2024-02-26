#!/usr/bin/python3
'''This module has a function which splits text after each ".?:"'''


def text_indentation(text):
    '''Prints a text with 2 new lines after each ".?:"

        Args:
            text (str): The text to be splitted

        Raises:
            TypeError: text must be a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for word in text:
        if word == "." or word == "?" or word == ":":
            print(word + "\n\n", end="")
        else:
            print("{}".format(word), end="")
