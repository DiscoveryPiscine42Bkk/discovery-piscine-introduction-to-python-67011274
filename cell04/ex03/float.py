#!/usr/bin/env python

number = input("Give me a number: ")
num = float(number)
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")