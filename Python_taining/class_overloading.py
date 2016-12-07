#!/usr/bin/python

# Python program to demonstrate overloading


class newDate():
    def __add__(self, num):
	month = 12
	date = 7
	if ((date+30)% 31) < date:
		month = (month+1)% 12
		date = (date+30)% 31
	if instanceOf == 'str':
		result = ''
	for i in args:
		result = result + i
	return result

    def __init__(self):
        print("object of class MOM created")
 
print add('int', 3,4,5)
print add('str', 'I',' am',' in', ' Python')
 
