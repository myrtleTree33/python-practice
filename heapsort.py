#!/usr/bin/env python
# -*- coding: utf-8 -*-

def swap(a,b):
    pass

def sift_down(a,idx,end):
    pass

def heapify(a):
    start = len(a) - 2 / 2 ## parent
    while start > 0:
        siftDown(a,start,len(a)-1)
        start  = start - 1

def heap_sort(a):
    heapify(a)
    end = len(a) - 1
    while end > 0:
        swap(a[end], a[0])
        end -= 1
        sift_down(a, 0, end)

