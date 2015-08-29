#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quicksort(arr):
    less, equal, greater = [],[],[]
    if (len(arr) <= 1):
        return arr
    pivot = arr[0]
    for x in arr:
        if (x < pivot):
            less.append(x)
        elif (x == pivot):
            equal.append(x)
        else:
            greater.append(x)
    quicksort(less)
    quicksort(greater)
    return quicksort(less) + equal + quicksort(greater)



a = [8,1,6,23,45,2]
print quicksort(a)
print 'done!'

