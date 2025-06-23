#!/usr/bin/env python3
try:
    num = int(input('Enter a number less than 25: '))
except ValueError:
    print("Error")
    exit()

if num > 25:
    print("Error") 
else: 
    i = num
    while i <= 25:
        print(i)
        i += 1 