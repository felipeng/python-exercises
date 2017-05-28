'''
Create a program that will play the cows and bulls game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that 
the user guessed correctly in the correct place, they have a cow For every digit the user guessed 
correctly in the wrong place is a bull. Every time the user makes a guess, tell them how many cows and bulls they have. 
Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
'''
from random import randint
number = str(randint(1000,9999))

def bulls_check(number,guess):
    number = list(number)
    guess = set(guess)
    bulls = 0
    for i in guess:
        bulls += number.count(i)
        
    return bulls

def cows_check(number,guess):
    cows = 0
    for i in range(4):
        if number[i] == guess[i]:
            cows += 1
    
    return cows
    
guess = 0000
tries = []
while guess != number:
    guess = str(raw_input("Enter a number: "))
    # validate the input
    if (int(guess) < 1000 or int(guess) > 9999):
        print("Only numbers between 1000 and 9999 are accepted")
        continue

    bulls = bulls_check(number,guess)
    cows = cows_check(number,guess)
    
    tries.append(guess)
    print("%s - %s cows, %s bulls" % (len(tries), cows, bulls))

print("Congratulations the number is %s and you tried %s" % (number, len(tries)))
