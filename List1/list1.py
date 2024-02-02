'''
@author: Dominik Cedro
@date: 17.11.2023
This is corrected version of my code.
'''
from math import floor as fl
import matplotlib.pyplot as plt

def weekday(day, month, year):
    '''Task 1.It returns day of the week on given day, month and year.
    
    User will provide day, month and year of interest. This function will
        return which day of the week was.
    
    Args:
        day : integer, day of the week: 0 for Sunday, 1 for Monday, 2 for Tuesday, and so forth..
        month : integer, describes a month, use 1 for January, 2 for February, and so o.
        year : integer , year as an integer.

    Returns:
        d_zero : string, that's the day the user was searching for.

    Raises:

    '''
    d = day
    m = month
    y = year

    # y_zero
    y_zero = y - fl((14 - m) / 12)

    # x
    x = y_zero + fl(y_zero / 4) - fl(y_zero / 100) + fl(y_zero / 400)

    # m
    m_zero = m + 12 * fl((14 - m) / 12) - 2

    # d_zero
    d_zero = (d + x + fl((31 * m_zero) / 12)) % 7

    # list with all the days of the week so i can tell the user which one he got
    week = ["Sunday", "Monday", 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday',
            ]
    return week[d_zero]

def segment_lenght(ap, ak, bp, bk):
    '''Task 2.Returns common segment of two sections.

    User will provide two sections, which are placed on one axis,
    then the function will calculate what is the common part.

    Parameters:
    Ap : Float, beginning of A section
    Ak : Float, end of A section
    Bp : Float, beginning of B section
    Bk : Float, end of B section
    Returns:
    common: float, common part of two sections

    '''
    if ap > ak:
        ap, ak = ak, ap
    if bp > bk:
        bp, bk = bk, bp

    else:
        a = [ap, ak]
        b = [bp, bk]
        common = []

    if ap < ak and bp < bk and ak < bp:
        return None
    elif bp < bk and ap < ak and bk < ap:
        return None
    elif ap < bk and ak == bk:
        return ak
    elif bp < ak and bk == ap:
        return ap
    elif ap == bp and bp < bk and bk < ak:
        common = [ap, bk]
        return common
    elif ap == bp and bp < bk and ak < bk:
        common = [ap, ak]
        return common
    elif ap < bp and ak == bk:
        common = [bp, ak]
        return common
    elif bp < ap and ak == bk:
        common = [ap, bk]
        return common
    elif ap < bp and bk < ak:
        common = [bp, bk]
        return common
    elif bp < ap and ak < bk:
        common = [ap, ak]
        return common
    elif ap == bp and ak == bk:
        common = a
        return common



    
def random_walk(distance):
    '''Task 3.This function shows a random walk via plot

    This function represents a walk of a person in two dimensional area.
    Person starts from point (0,0) and walks randomly in one of 4 ways until
    he reaches n moves.

    Arguments:
    n : integer, this marks the distance from the

    Returns:
    plot: plot, plot that shows the trajectory of the person
    coords: list of tuples, list of coordinates that the walker reached until he stopped
    '''

    current_position = (0,0)
    list_of_positions = []
    while (abs(0-current_position[0]) + abs(0-current_position[1])) < distance:
        current_position = list(current_position)
        current_position[random.choice([1,0])] += random.choice([-1, 1])
        list_of_positions.append(tuple(current_position))

    return list_of_positions


# coordinates = random_walk(100)
# x, y = zip(*coordinates)
# plt.plot(x, y, marker='o', linestyle='-', markersize=2)
# plt.xlabel('X Coordinate')
# plt.ylabel('Y Coordinate')
# plt.title('Walker\'s Trajectory')
# plt.grid(True)
# plt.show()
# print(coordinates)

def dec2bin(x):
    '''Task 4. Turns decimal to binary

    This function will translate number written in decimal form to number
    written in binary form. If the input number is negative it will write one
    extra zero at the beggining

    Parameters
    ----------
    x : int
        It is a number in decimal form, can be negative, can't be a flota

    Returns
    -------
    binary: string, It is a number in binary form, it's in form of a string.
    '''
    binary = ""
    negbinary = "0"
    negative = False
    if x == 0:
        binary = "0"
        return binary
    if x < 0:
        negative = True
        x = x * (-1)
    while x > 0:
        if x % 2 == 0:
            binary = binary + "0"
            x = x / 2
        else:
            binary = binary + "1"
            x = (x - (x % 2)) / 2
    if negative is True:
        negbinary = negbinary + binary[::-1]
        return negbinary
    else:
        return binary[::-1]

def dna_complement(orig_strand):
    '''Task 5. Complements DNA strand given by user.

    This function will complement DNA that is given to it in form of string
    Complemented DNA strand will be sent back to user.

    Parameters:
    orig_strand: string, strand of dna that will be complemented by function

    Returns:
    new_strand: string, complemented original strand
    '''
    new_strand = ""
    letters = ["A", "T", "C", "G"]
    for k in range(len(orig_strand)):
        if orig_strand[k] == letters[0]:
            new_strand = new_strand + letters[1]
        elif orig_strand[k] == letters[1]:
            new_strand = new_strand + letters[0]
        elif orig_strand[k] == letters[2]:
            new_strand = new_strand + letters[3]
        elif orig_strand[k] == letters[3]:
            new_strand = new_strand + letters[2]
        else:
            print("Wrong input, strand consists of incorrect letters.")
            return None
    return new_strand

