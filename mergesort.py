#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mergesort(m):
    (left,right,result) = ([],[],[])
    if (len(m) <= 1):
        return m
    else:
        middle = len(m) / 2
        for x in m[:middle]:
            left.append(x)
        for x in m[middle:]:
            right.append(x)
        #print 'left:' + ','.join(str(e) for e in left)
        #print 'right:' + ','.join(str(e) for e in right)
        left = mergesort(left)
        right = mergesort(right)
        """
        if (left[-1] <= right[0]):
            left += right
            return left
        """
        result = merge(left, right)
        return result

def merge(left, right):
    result = []
    while(len(left) > 0 and len(right) > 0):
        if (left[0] <= right[0]):
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result +=right
    return result

print mergesort([4,8,2,1,6,7,2,3,4,3,2,1,8,4,2,1,1,0])

