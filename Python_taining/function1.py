#!/usr/bin/python

# Python program to demonstrate function
    
a,b,c,d=10,20,30,40
def funA():
    a,b,c=100,200,300
    print("In funA", a,b,c,d)
    def funB():
        a,b=1000,2000
        print("In funB", a,b,c,d)
        def funC():
            a=10000
            print("In funC", a,b,c,d)
        funC()
    funB()
funA()
print("In_main_",a,b,c,d)
