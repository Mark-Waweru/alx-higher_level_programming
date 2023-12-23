#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    print_reversed_list_integer - prints all integers of a list, in
    reverse order
    @my_list: The list that holds the values

    return: None or the list reversed
    """
    if not my_list:
        return (None)

    i = len(my_list)
    while i > 0:
        print("{:d}".format(i), end="\n")
        i -= 1
