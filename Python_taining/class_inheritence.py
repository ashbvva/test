#!/usr/bin/python

# Python program to demonstrate class

class mgm(): 
    def talk(self):
        print("speak softly")

class mgf():
    def teach(self):
        print("teach values")

class pgm():    
    def talkPGM(self):
        print("tell stories")
        
class pgf():    
    def talkPGF(self):
        print("encourage")
    def talk(self):
        print("pgf speaking")

class mom(mgm, mgf):
    """class Mom"""
    x=10; y=20
    def walk(self):
        print ("walk elegently")
        # print(id(self))
    def sum(self, a, b):
        return (a+b+self.x+self.y)
    def __init__(self):
        print("object of class MOM created")

        
# myMother = mom()
# print(id(myMother))
# myMother.walk()

class dad(pgm, pgf):
    def talk(self):
        print("speak politely")
    def __del__(self):
        print("object of class DAD destroyed")

class infant(mom, dad):
    pass

baby = infant()
print (dir(baby))
baby.walk()
baby.talk()
print(baby.sum(10,20))
