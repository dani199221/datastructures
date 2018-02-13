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
            1:[2,3,7],
            2:[1,3,7],
            3:[1,2,4,5,6],
            4:[3,5,6],
            5:[3,4,6],
            6:[3,4,5,7],
            7:[1,2,6]

            }
    g.make_graph(d)
    g.print_vertices()
