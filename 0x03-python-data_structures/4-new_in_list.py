#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    new_in_list - replaces an element in a list at a specific position
    without modifying the original list
    @my_list: The list holding the values
    @idx: The index position to replace the element
    @element: The element to put or replace

    Return: The new list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)

    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[i])

    new_list[idx] = element
    return (new_list)
