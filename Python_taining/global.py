#!/usr/bin/python

# Python program to demonstrate scope

x=10
def func():
    #global x
    #x=20
    print(x)
    x+=10
func()
print(x)
