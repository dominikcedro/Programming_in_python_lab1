'''
@author: Dominik Cedro
@date: 17.11.2023
This is corrected version of my code.
'''

from list1 import weekday
from list1 import segment_lenght
from list1 import dec2bin
from list1 import random_walk
from list1 import dna_complement
import random


#testweekday
def test_weekday():
    ''' This is a test function for "weekday" function.
                '''
    assert weekday(4, 8, 2009) == "Tuesday"
    assert weekday(19, 11, 2023) == "Sunday"




def test_segment_lenght():
    ''' This is a test function for "segment_lenght" function.
            '''
    assert segment_lenght(1, 2, 3, 4) == None
    # test for normal intersection
    assert segment_lenght(1, 2, 1, 4) == (1, 2)
    # test for inverted Ap Ak
    assert segment_lenght(2, 1, 4, 2) == (2, 2)
    # test for inverted segments A and B
    assert segment_lenght(3, 8, 1, 4) == (3, 4)
    # test for
    assert segment_lenght(2, 1, 4, 2) == (2, 2)


def test_random_walk():
    ''' This is a test function for "random_walk" function.

        Raises: Assertion error if function works incorrectly
    '''
    # test if returns list
    assert isinstance(random_walk(10), list), "Function did not return a list"
    # check specific random event, if lenght of coordinates list is correct
    random.seed(42)
    assert len(random_walk(100)) == 3684

def test_dec2bin():
    ''' This is a test function for "dec2bin" function.

        Raises: Assertion error if function works incorrectly
        '''
    # test for normal argument
    assert dec2bin(10) == "1010"
    # test for negative argument
    assert dec2bin(-10) == "01010"
    # test for 0
    assert dec2bin(0) == "0"


#test_dna_complement
def test_dna_complement():
    ''' This is a test function for "dna_complement" function.

        Raises: Assertion error if function works incorrectly
        '''
    result = dna_complement("ATC")
    assert result=="TAG"


#start testing functions
