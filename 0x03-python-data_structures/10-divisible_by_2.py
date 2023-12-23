#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    divisible_by_2 - finds all multiples of 2 in a list
    @my_list: The list to find the multiples of 2

    Return: True or False list
    """
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return(new_list)
