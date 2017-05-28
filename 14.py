#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
Extras:
1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.
2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
a = [1,2,3,4,5,4,3,2,1]

def solution1(a):
    r = []
    for item in a:
        if item not in r:
            r.append(item)
    print r



def solution2(a):
    b = list(set(a))
    print b

#solution1(a)
solution2(a)
