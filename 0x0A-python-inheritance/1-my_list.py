#!/usr/bin/python3
'''This module contains a function that prints a list items in ascending order
'''


class MyList(list):
    '''This class inherits from list class and has one method for printing
    list items in ascending order'''
    def print_sorted(self):
        '''prints a list items in ascending order'''
        print(sorted(self))
