'''
Sutton Dole
P4: Guess a Number using loops and a function

'''


import random

def check(number, numberGuess):
    try:
        numberGuess = float(input('Take a guess: '))
        ifVal = 0
        if numberGuess < 1 or numberGuess > 20:
            ifVal = 2
        elif numberGuess == number:
            ifVal = 0
        elif numberGuess < number: 
            ifVal = -1
        else:
            ifVal = 1
        return ifVal
    except:
        ifVal = -2
        return ifVal

def main():
    number = random.randint(1, 20)
    counter = 1
    flag = 0
    name = input('What is your name? \n')
    print("Hi " + name + ", I'm thinking of a number between 1 and 20")
    while counter != 7:
        checker = check(number, numberGuess)
        if checker == -2:
            print("Please enter a number in integer form")
            counter = counter - 1
        elif checker == 2:
            print("The number should be in between 1 and 20")
            counter = counter - 1
        elif checker == -1:
            print("Your guess was too low")
        elif checker == 1:
            print("Your guess was too high")
        else:
            print("Good job " + name + ". You guessed my number in " + str(counter) + " guesses!")
            flag = 1
            break
        counter = counter + 1
    if flag == 0:
        print("The number I was thinking of was " + str(number))



main()
