#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python (don't worry if you can't figure this out at this point - we'll get to it soon)
'''
import random

def solution1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for item_a in a:
        if item_a in b and item_a not in c:
            c.append(item_a)
    print c

def solution2():
    def createList():
        s = random.randint(0,20)
        i = 0
        r = []
        while i < s:
            r.append(random.randint(0,10))
            i += 1
        return r
        
    a = createList()
    b = createList()
    c = []
    for item_a in a:
        if item_a in b and item_a not in c:
            c.append(item_a)
    print c

def solution3():
    print(list(set(a) & set(b)))

#solution1()
solution2()
#solution3()
