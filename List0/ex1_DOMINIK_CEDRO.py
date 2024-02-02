# -*- coding: utf-8 -*-
"""
Exercise 1

Created on Fri Oct  6 08:27:10 2023

@author: Dominik
"""


#greeting
print("This function will print inverted isoceles. Please define your number, which will be the height of the structure.")
print()
def isoceles(number):
    '''

    Parameters
    ----------
    number : integer,
        defined by user height of printed isoceles

    Returns
    -------
    isoceles : string,
        inverted isoceles with height == number

    '''
    #below finds n-th odd number
    odd = 1
    for i in range(1,number):
        odd = odd + 2

    #below prints stars
    for k in range(number):
        print(" " * (k) + ("*" * (odd - 2*k)))
    

isoceles(int(input("What is your number?: ")))