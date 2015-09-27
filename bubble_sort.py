#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


if __name__ == '__main__':
    print bubble_sort([3,6,8,5,3,2,1,8,2])
