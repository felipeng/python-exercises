#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, 
a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.
'''

n = raw_input("Number: ")
n = int(n)

def prime(n):
    c = []
    for x in range(2,n):
        if (n % x) == 0:
            c.append(x)
    
    if len(c) != 0:
        r = " NOT"
    else:
        r = ""
    print("The number {} is{} prime.".format(n,r))

prime(n)
