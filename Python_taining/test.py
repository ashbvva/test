#!/usr/bin/python

def average(values):
    """computes mean
    >>> print average([10,20,30])
    20
    >>> print average([10,20,30])
    20.00
    >>> print average([10,20,30])
    30
    >>> print average([10,20,40])
    20
    """
    return sum(values,0.0)/len(values)
