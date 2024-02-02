# -*- coding: utf-8 -*-
"""
Exercise 3

Created on Sun Oct  8 17:52:19 2023

@author: Dominik
"""

def fibbonaci(n):
    '''
    It is a simple function that gives n-th number in fibbonaci sequence. I used reccuring method to simplify code.

    Parameters
    ----------
    n : integer
       Describes position of searched item in fibbonaci sequence

    Returns
    -------
    result : integer
        fibbonaci number on n-th place

    '''
    #very simple code, few conditions at first, so recurring function won't run forever
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result =  fibbonaci(n-1) + fibbonaci(n-2)
    return result
   
    
print(fibbonaci(11))