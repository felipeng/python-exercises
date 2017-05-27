#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

word = str(raw_input("Word: "))

def solution1():
    r = ""
    if word != word[::-1]:
        r = " NOT"    
    print("The word '{}' is{} palindrome".format(word, r))

def solution2():
    r = [word != word[::-1]]
    print r[0]
    

def solution3():
    drow = ""
    r = ""
    l = len(word)-1
    while l >= 0:
        drow += word[l]
        l -= 1
        
    if word != drow:
        r = " NOT"
    print("The word '{}' is{} palindrome".format(word, r))

    
    
#solution1()
#solution2()
solution3()
