# -*- coding: utf-8 -*-
"""
Excercise 2

Created on Sun Oct  8 17:37:15 2023

@author: Dominik
"""

def divisible(numbers, divisor):
    '''

    Parameters
    ----------
    numbers : list
       it is a list of numbers (of any type), these numbers will be tested
    divisor : integer or float
        a number that will be a testing parameter for "numbers" list

    Returns
    -------
    divisible_num : list
        list of all the numbers, that are divisible, from "numbers" list

    '''
    #I'm using for loop to simplify the code ,also module operator helps to make it all simple
    divisible_num = []
    for i in numbers:
        if  i % divisor == 0:
            divisible_num.append(i)
    return divisible_num


def divisible_test():
    '''
    It is a simple testing function for "divisible" function. Raises assertion
    error if the output is wrong

    Returns
    -------
    Assertion Error if conditions are not met

    '''
    numbers = [1,3,4,5,6,7,8,9,10]
    divisor = 3

    assert divisible(numbers, divisor) == [3,6,9]
divisible_test()


