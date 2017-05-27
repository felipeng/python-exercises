#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

from datetime import date

name = raw_input("Name: ")
age = int(input("Age: "))

print("{} you will turn 100 years old in {}".format(name, (100-age)+date.today().year))
