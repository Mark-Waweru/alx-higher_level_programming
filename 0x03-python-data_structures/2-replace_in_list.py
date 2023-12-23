#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    replace_in_list - replaces an element of a list at a specific position
    @my_list: The list holding the values
    @idx: The index of the element you want to replace
    @element: The value you want to add to the list

    return: The list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)

    my_list[idx] = element
    return (my_list)
