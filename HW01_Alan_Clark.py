"""
   File Name:    HW01_Alan_Clark.py
   Author:       Alan Clark
   Date:         11 Sep 2021
   Description:  Function to classify triangles
"""

# Function to classify a triangle by comparing its sides
def classify_triangle(a: int, b: int, c: int) -> str:
    """ Validate input """
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError('Triangle side lengths must be greater than zero, fool')
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise TypeError('Triangle side lengths must be positive integers')
    result : str
    hypotenuse : int = a
    sum_of : int = b**2 + c**2
    """ Determine the type of triangle """
    if a == b:
        if b == c:
            result = "equilateral"
        else:
            result = "isoceles"
    elif a == c or b == c:
        result = "isoceles"
    else:
        result = "scalene"
    """ Now find the correct hypotenuse """
    if b > hypotenuse:
        hypotenuse = b
        sum_of = a**2 + c**2
    if c > hypotenuse:
        hypotenuse = c
        sum_of = a**2 + b**2
    """ So, is this a right triangle? """
    if hypotenuse**2 == sum_of:
        result += ", right triangle"
    return result
