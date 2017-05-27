#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, 
tell that to the user. If not, print a different appropriate message.
'''

n = int(input("Number: "))

if (n % 2) == 0:
    r = "even"
    multiple = ""
    if (n % 4) == 0:
        multiple = " is multiple of 4 and"
else:
    r = "odd"

print("The number {}{} is {}".format(n,multiple,r))
