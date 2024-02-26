#!/usr/bin/python3
'''This module has a function which multiplies 2 matrices.
    By using the module NumPy
'''
import numpy as nmp


def lazy_matrix_mul(m_a, m_b):
    ''' multiplies 2 matrices

    Args:
        m_a (list of lists, int/float): The first matrix
        m_b (list of lists, int/float): The second matrix
    '''

    return (nmp.matmul(m_a, m_b))
