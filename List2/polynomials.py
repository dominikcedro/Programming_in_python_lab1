"""
@author: Dominik Cedro
"""

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def degree(self):
        return (len(self.coefficients)-1)

    def __str__(self):
        result = ""
        string = ""
        for i, coefficient in enumerate(self.coefficients):
            if coefficient != 0:
                if i < self.degree():
                    string += f"{coefficient}x^{self.degree()-i}"
                else:
                    str(coefficient)
                result += (string + " + ")




