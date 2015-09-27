#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue

graph = {
    "a": ["b","c"],
    "b": ["d","e"],
    "e": ["f","h"]
}

def bfs(head):
    visited = []
    q = Queue.Queue()
    q.put(head)
    while not q.empty():
        curr = q.get()
        if curr not in visited:
            visited.append(curr)
            if (curr in graph):
                map(q.put,graph[curr])
    print visited


def dfs(head):
    visited = []
    stack = [head]
    while stack:
        curr = stack.pop()
        if (curr not in visited):
            visited.append(curr)
            if (curr in graph):
                stack.extend(graph[curr])
    print visited

dfs("a")
bfs("a")

