#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and val < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = val
    return arr



if __name__ == '__main__':
    print insertion_sort([2,4,8,4,56,8,54,2,5,8,6,3,6,])
