#!/usr/bin/python3
def element_at(my_list, idx):
    """
    element_at - It retrieves an element from a list
    @my_list: The list that holds the elements
    @idx: The index of the element to print

    return: None or the specified element
    """
    if idx < 0 or idx > len(my_list) - 1:
        return (None)

    return (my_list[idx])
