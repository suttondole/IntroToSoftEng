'''Sutton Dole's P5
   String manipulation
'''

def plural(oldString):
    newString = ""
    listOfExceptions = ["o", "ch", "s", "sh", "x", "z"]
    listOfVowels = ["a", "e", "i", "o", "u"]
    indexOfSpaces = []
    listOfOldStrings = []
    currentIndex = 0


    for x in oldString:
        if x == ' ':
            indexOfSpaces.append(currentIndex)
        currentIndex += 1
    currentIndexOfBeggining = 0
    for x in indexOfSpaces:
        listOfOldStrings.append(oldString[currentIndexOfBeggining:x])
        currentIndexOfBeggining = x + 1
    listOfOldStrings.append(oldString[currentIndexOfBeggining: ])
    for x in listOfOldStrings:
        if x[len(x) -2: ] in listOfExceptions or x[len(x)-1] in listOfExceptions:
            newString = newString + x + "es "
        elif x[-1:] == "y":
            if x[len(x) - 2] in listOfVowels:
                newString = newString + x + "s "
            else:
                newString = newString + x[:-1] + "ies "
        else:
            newString = newString + x + "s "
    return newString
        
def main():
    oldString = input('Please enter a string: ')
    print(plural(oldString))

main()
