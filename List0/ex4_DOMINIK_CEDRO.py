# -*- coding: utf-8 -*-
"""
Exercise 4

Created on Sun Oct  8 21:04:04 2023

@author: Dominik
"""

def my_program(text):
    '''

    Parameters
    ----------
    text: string,
        text written by the user, my_program will perform operations on this text

    Returns
    -------
    None, this function prints its results instantly

    '''
    #some space so it looks good
    print("")

    #just text
    print("Original string: ", text)

    #lenght
    print("Length of the string: ", len(text))

    #counting vowels
    count = 0
    for j in range(len(text)):
        if text[j] == "a" or text[j] == "e" or text[j] == "i" or text[j] == "o" or text[j] == "u" or text[j] == "y":
            count = count +1
        
    #reverse order
    reverse = ""
    for k in range(len(text)):
        reverse = reverse + text[len(text)-1]
        text = text[:-1]
    print("Reversed string: ", reverse)
 
    #printing count
    print("Number of vowels: ", count)

my_program(input("Write something: "))