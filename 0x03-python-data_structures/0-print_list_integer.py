#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    print_list_integer - prints all integers of a list
    @my_list: The list that holds the integers

    return: None
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]), end="\n")
