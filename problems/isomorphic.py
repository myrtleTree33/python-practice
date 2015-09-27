#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = "foo"
b = "bar"

def is_isomorphic(s,t):
    if len(s) != len(t): return False
    mapping = {}
    for i, ch in enumerate(s):
        if not mapping.has_key(ch):
            mapping[ch] = t[i]
        elif mapping[ch] != t[i]:
            return False
    return True


print is_isomorphic(a,b)
