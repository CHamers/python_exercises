# simple guessing game
# based on the classic carnival game of guessing under which cup is the red ball
# Theree will be 3  positions in the list, one of which iss an 'O'.
# One function will shuffle the list
# another one will take a player's guesss
# anther one will checck to seee if it is correct

from random import shuffle

myList = [' ','O',' ']

def shuffle_list(aList):
    shuffle(aList)
    return aList

mixedupList = shuffle_list(myList)
print(mixedupList)

def player_guess():
    guess = ' '
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 or 2: ")
    return int(guess)

playerGuess = player_guess()
print(playerGuess)

def check_guess(myList, guess):
    if myList[guess] == 'O':
        print("Correct")
    else:
        print("Wrong guess")
        print(myList)
        
check_guess(myList, playerGuess)