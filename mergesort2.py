#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mergesort(m):
    (left,right,result) = ([],[],[])
    if (len(m) <= 1):
        return m
    else:
        middle = len(m) / 2
        left = mergesort(m[:middle])
        right = mergesort(m[middle:])
        result = merge(left,right)
        return result

def merge(left, right):
    result = []
    while(len(left) > 0 and len(right) > 0):
        if (left[0] < right[0]):
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if (len(left) > 0):
        result += left
    else:
        result += right
    return result

print mergesort([2,4,7,9,3,6,12,7,4,2,8,2,0,3])
