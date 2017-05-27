#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don't know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

n = int(input("Number: "))
r = []

def solution1():
    for i in range(1,n+1):
        if (n % i) == 0:
            r.append(i)
        
    print r

def solution2():
    r.append([i for i in range(1,n+1) if (n%i) == 0])
    print r[0]

#solution1()
solution2()
  