#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quicksort(arr):
    (left,eq,right) = ([],[],[])
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    for x in arr:
        if (x < pivot):
            left.append(x)
        elif (x == pivot):
            eq.append(x)
        else:
            right.append(x)
    return quicksort(left) + eq + quicksort(right)


if __name__ == '__main__':
    print quicksort([3,2,2,8,9,5,4,7,5,3,2,6,8])
