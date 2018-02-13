#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 danial <danial@danial-Blade>
#
# Distributed under terms of the MIT license.

"""

"""
import  sys 
sys.path.append('../graphs')
from  graphs import *


class union:

    def __init__(self, head):

        self.parent = head
        self.members = set()
        self.members.add(head)
    
    def add(self, new):
        self.children.add(new)

    def union(self, set2):
        self.members.union(set2)






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
