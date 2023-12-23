#!/usr/bin/python3
def no_c(my_string):
    """
    no_c - removes all characters c and C from a string.
    @my_string: The string to check from

    return: The new string without C and c letters
    """
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i] != 'C' and my_string[i] != 'c':
            new_string += my_string[i]

    return (new_string)
