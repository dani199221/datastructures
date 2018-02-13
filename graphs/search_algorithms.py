#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 danial <danial@danial-Blade>
#
# Distributed under terms of the MIT license.

"""

"""

from graphs import *

def bfs(g, node):
    queue = [] 
    visited = []
    queue.append(node)

    while len(queue) != 0:
        res = queue.pop(0)
        visited.append(res)
        print res
        neighbours =  g.get_neighbours(res)
        for n in neighbours:
            if n  in visited:
                continue

            if n not in queue: 
                queue.append(n)

def dfs(g, node):
    queue = [] 
    visited = []
    queue.append(node)

    while len(queue) != 0:
        res = queue.pop()
        print res
        visited.append(res)
        neighbours =  g.get_neighbours(res)
        for n in neighbours:
            if n  in visited:
                continue

            if n not in queue: 
                queue.append(n)

def make_graph(g, d):
    #add vertecies
    for k in d.keys():
        g.add_vertex(k)
    
    #add edges
    for k in d.keys():
        for v in d[k]:
            g.add_edge(k, v)
    
    #g.print_vertices()
    return g

if __name__ == '__main__':

    g = graph()
    d = {
            1:[2,3,7],
            2:[1,3,7],
            3:[1,2,4,5,6],
            4:[3,5,6],
            5:[3,4,6],
            6:[3,4,5,7],
            7:[1,2,6]

            }
    g.make_graph(d)
    dfs(g, 2)
