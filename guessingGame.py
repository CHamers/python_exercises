# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# 
# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it too

import random
num = random.randint(0,100)
print(num)

# print("WELCOME TO GUESS ME!")
# print("I'm thinking of a number between 1 and 100")
# print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
# print("If your guess is within 10 of my number, I'll tell you you're WARM")
# print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
# print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]

while True:
    guess = int(input("I am thinking of a number between 1 and 100. \n What is your guess? "))
    print(guess)
    if guess < 1 or guess > 100:
        print('Out of bounds! Please try again:')
        continue
    #Here we compare the player's guess to our number
    if guess == num:
        print(f'Congratulations, you guessed it in only {len(guesses)} guesses!')
        break
    #If guess is incorrect, add guess to the list
    guesses.append(guess)
    print(guesses)

    #If you append all new guesses to the list, then the previous guess is given as guesses[-2] 
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("Warmer")
        else:
            print("Colder")
    else:
        if abs(num-guess) <= 10:
            print("Warmm")
        else:
            print("Cold")
