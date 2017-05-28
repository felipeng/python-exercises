#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Write a program (using functions!) that asks the user for a long string 
containing multiple words. Print back to the user the same string, 
except with the words in backwards order. 
For example, 
say I type the string: "My name is Michele"
Then I would see the string: "Michele is name My" shown back to me.
'''

#string = str(raw_input("String: "))
string = "My name is Michele"


def solution1(string):
    string = string.split(" ")
    i = len(string)-1
    r = []
    while i >= 0:
        r.append(string[i])
        i -= 1
    
    print " ".join(r)


def solution2(string):
    string = string.split(" ")
    string.reverse()
    print " ".join(string)

def solution3(string):
    print " ".join(string.split()[::-1])

#solution1(string)
#solution2(string)
solution3(string)
