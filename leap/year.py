#!/usr/bin/python3

year = input("Type an year: ")
year = int(year)
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('year', year, 'is a leap year !')
else:
    print('year', year, 'is not a leap year !')
