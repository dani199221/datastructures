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

#------------------find connected components in a graph----------------#
#dfs over an individual node and its neighbouts
def dfs_individual(g, u , visited):
    for n in g.get_neighbours(u):
        if n not in visited:
            visited.append(n)
            dfs_individual(g, n, visited)
    

#dfs over all the nodes to find connected components
def dfs_all_nodes(g):
    
    connected = 0
    visited = []
    for n in g.get_all_vertices():
        if n not in visited:
            dfs_individual(g, n, visited)
            connected += 1

    return connected
#----------------------------------------------------------------------#


if __name__ == '__main__':

    g = graph()
    d = {
            0:[1,2],
            1:[0,3],
            2:[0,3],
            3:[1,2],
            5:[6],
            6:[5,7],
            8:[],
            9:[]

        }
    g.make_graph(d)
    print  dfs_all_nodes(g)
