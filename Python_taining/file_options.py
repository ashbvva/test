#!/usr/bin/python

"""
import sys
fobj = open ("notes.txt", "r")
fsize=sys.argv.__sizeof__()

ctr=0
line=fobj.readline()
while line:
    ctr += 1
    print (ctr, line,end="")
    line=fobj.readline()
else:
    print ("size of file is", fsize, "bytes")
fobj.close()
"""



import sys

fobj = open ("notes.txt", "r")
fobj1 = open ("newFile.txt", "w")

fobj1.write(fobj.read())

fobj.close()
fobj1.close()
