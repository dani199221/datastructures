#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 danial <danial@danial-Blade>
#
# Distributed under terms of the MIT license.

"""

"""
class vertex:
    """
        A vertex class to represent the nodes
        of the graph. Each node has an id and 
        a dictionary of neighbours where the
        key is the vertex and the value is the
        weight between the two vertices
    """
    #The constructor to make a node with id and 
    #empty neighbours lis
    def __init__(self, ids):
        self.id = ids
        self.neighbours = {}

    # return the id of the vertex
    def get_id(self):
        return self.id
    
    #return the neighbours of the vertex
    def get_neighbours(self):
        return self.neighbours.keys()    
    
    #add a neighbour to the vertex with give nweight
    def add_nieghbour(self, neighbour, wt=0):
        self.neighbours[neighbour] = wt
    
    #get weight bewteen two nodes
    def get_weight(self, nbr):
        return self.neighbours[nbr]  if nbr in self.neighbours.keys() else False
    
    #set weight between vertex
    def set_weight(self, nbr, wt):
        if nbr in self.neighbours.keys():
            self.neighbours[nbr] = wt
            return True
        else:
            return False

    #delete a neighbour from adjacency list if it exists
    def delete_neighbour(self,nbr):
        if nbr in self.neighbours.keys():
            del self.neighbours[nbr]
            return True
        else: 
            return False
    
    # if neighbour exists in the ajaccency list
    def __contains__(self, nbr_id):
        return True if nbr_id in self.neighbours.keys() else False
