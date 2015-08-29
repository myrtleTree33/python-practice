#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quicksort(arr):
    left, equal, right = [],[],[]
    if (len(arr) <= 1):
        return arr
    pivot = arr[0]
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            right.append(x)
    return quicksort(left) + equal + quicksort(right)

print quicksort([5,2,8,2,1,89,3,6])
