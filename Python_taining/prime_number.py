#!/usr/bin/python

# Python program to display all the prime numbers
    
n = 100
p = 1

while p <= n:
    is_prime=True
    for i in range(2, p):
        if p%i == 0:
            is_prime=False
            break;
    if is_prime==True:
        print (p)
    p=p+1
