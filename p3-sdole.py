"""Sutton Dole's P3
   User defined functions
"""

def maxOfThree():
    first = input('Enter first value: ')
    second = input('Enter second value: ')
    third = input('Enter third value: ')
    maxi = first
    if maxi < second:
        maxi = second
    if maxi < third:
        maxi = third
    print("The max of " + first + " " + second + " " + third + " is " + maxi)
