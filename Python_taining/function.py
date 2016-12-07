#!/usr/bin/python

# Python program to demonstrate function
    
"""def sum(a, b, c=0, d=0):
    initiate with default values for operation
    for ex 0 for sum and 1 for multiplication
    pass list if you want to use more variables in future
    print (a+b+c+d)
    print("a",a, "b",b, "c",c, "d",d)
    
sum (10,20); sum (10,20,30); sum (10,20,30,40); sum(b=100, a=200, d=300, c=400)"""


"""x,y=10,20
def incr(a, b):
    a+=1;b+=1
    return(a, b)

(a,b)=incr(x,y)
print (x,y)
print (a, b)"""


x=input("Type number:")
def factorial(n):
    
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        
        return res	


print(factorial(x))
