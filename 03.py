#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''


def solution1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in a:
        if i < 5:
            print i

def solution2():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for i in a:
        if i < 5:
            b.append(i)
    print b
    
    
def solution3():
    print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < 5 ])

def solution4():
    n = int(input("Number: "))
    print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < n ])
    
## Solutions
#solution1()
#solution2()
#solution3()
solution4()
