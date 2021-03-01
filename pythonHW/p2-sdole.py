"""Sutton Dole's P2
   Convert numeric scores to grades
"""

try:
    score = float(input('Please enter your score '))
    if score > 100 or score < 0:
        print("That is not a valid score")
    elif score > 92:
        print("A")
    elif score > 90:
        print("A-")
    elif score > 87:
        print("B+")
    elif score > 83:
        print("B")
    elif score > 80:
        print("B-")
    elif score > 70:
        print("C")
    else:
        print("F")


except:
    print("Please enter a number")
