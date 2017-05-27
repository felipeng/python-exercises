#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

1. Keep the game going until the user types: exit
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

from random import randint

number = randint(1,9)
tries = 0
guess = 0

while guess != number and guess != "exit":
    guess = raw_input("Number: ")
    if guess == "exit":
        break
    guess = int(guess)
    tries += 1
    
    if guess > number:
        print "low"
    elif guess < number:
        print "hight"
    elif guess == number:
        print("Congratulations! You needed %s tries. Let's try again... " % tries)
        number = randint(1,9)
        tries = 0
