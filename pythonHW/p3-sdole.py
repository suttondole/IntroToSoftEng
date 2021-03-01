"""Sutton Dole's P3
   User defined functions
   Returning the max of three numbers
"""


def maxOfThree():
    try:
        first = float(input('Enter first value: '))
        second = float(input('Enter second value: '))
        third = float(input('Enter third value: '))
        maxi = first
        if maxi < second:
            maxi = second
        if maxi < third:
            maxi = third
        print("The max of " + str(int(first)) + " " + str(int(second)) + " " + str(int(third)) + " is " + str(int(maxi)))
    except:
        print("Please enter a number")
    

def main():
    maxOfThree()

main()
