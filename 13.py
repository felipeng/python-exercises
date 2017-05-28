#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci sequence is a sequence of numbers where the next number in the sequence is the sum 
of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, ...)
'''
qtd = int(input("How many Fibonnaci numbers? "))

def fib():
    f = [1, 1]
    n = 2
    while n < qtd:
        t = f[n-2] + f[n-1]
        f.append(t)
        n += 1 
    print f

fib()
