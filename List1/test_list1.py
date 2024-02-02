'''
@author: Dominik Cedro
@date: 17.11.2023
This is corrected version of my code.
'''
from list1 import weekday
from list1 import segment_lenght
from list1 import dec2bin
from list1 import dna_complement
import pytest

#testweekday
def test_weekday_case1():
    ''' This is a test function for "weekday" function.
        '''
    assert weekday(4,8,2009) == "Tuesday"

def test_weekday_case2():
    ''' This is a test function for "weekday" function.
        '''
    assert weekday(4,8,2009) == "Tuesday"


def test_segment_lenght():
    ''' This is a test function for "segment_lenght" function.

            Raises: Assertion error if function works incorrectly
            '''
    result = segment_lenght(1,10,1,8)
    assert result == [1,8]

#no test for function 3, because it has random output

def test_dec2bin():
    ''' This is a test function for "dec2bin" function.

        Raises: Assertion error if function works incorrectly
        '''
    result = dec2bin(-10)
    assert result == "01010"

#test_dna_complement
def test_dna_complement():
    ''' This is a test function for "dna_complement" function.

        Raises: Assertion error if function works incorrectly
        '''
    result = dna_complement("ATC")
    assert result=="TAG"


#start testing functions
test_weekday_case1
test_segment_lenght()
test_dec2bin()
test_dna_complement()
