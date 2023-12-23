#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    max_integer - finds the biggest integer of a list
    @my_list: The list holding the values

    Return: The biggest value in the list or None if empty
    """
    my_list.sort()
    end_num = len(my_list) - 1
    if len(my_list) == 0:
        return (None)
    else:
        return (my_list[end_num])
