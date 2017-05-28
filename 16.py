#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Write a password generator in Python. Be creative with how you generate passwords, 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:
1. Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''
import random

if __name__ == '__main__':
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()_+-=[]{}\|/?,<.>"
    password = ""
    pass_size = int(raw_input("Password size: "))

    for i in range(pass_size):
        password += random.choice(chars)

    print password
