#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 danial <danial@danial-Blade>
#
# Distributed under terms of the MIT license.

from vertex import *

class graph:
    """
        The main graph class whic has one vertices
        dictonary in which the key is the id of the
        vertex/node and the id is the node itself
    """
    
    #The constructor of the graph wiht one dict
    def __init__(self):
        self.vertices = {}
   
    #-------------------Edge Functions-------------------#
    #add an edge to the graph. Check if both vertices are
    #present. If not make them and add the edge.
    def add_edge(self, fromm, too, wt=0, bidirectional=True):
        if fromm not in self.vertices.keys():
            self.add_vertex(fromm)
        if too not in self.vertices.keys():
            self.add_vertex(too)
        self.vertices[fromm].add_nieghbour(too, wt)
        if bidirectional:
            self.vertices[too].add_nieghbour(fromm, wt)
    
    def remove_edge(self, fromm, too, bidirectional=True):
        if fromm not in self.vertices.keys() or too not in self.vertices.keys():
            return False
        else:
            self.vertices[fromm].delete_neighbour(too)
            if bidirectional:
                self.vertices[too].delete_neighbour(fromm)
            
            return True
    
    def get_edge_value(self, fromm, to):
        if to in self.vertices[fromm]:
            if self.vertices[fromm].get_weight(to):
                return self.vertices[fromm].get_weight(to)
            else:
                return False

    def set_edge_value(self, fromm, too, wt, bidirectional=True):
        if fromm not in self.vertices.keys() or too not in self.vertices.keys():
            return False
        else:
            self.vertices[fromm].set_weight(too,wt)
            if bidirectional:
                self.vertices[too].set_weight(fromm,wt)

    #---------------Vertex Functions-----------------------#
    #adding a vertex. First check if it does not exist
    #if not then make a new vertex and add it to dict
    def add_vertex(self,ids):
        if ids not in self.vertices.keys():
            new_vertex = vertex(ids)
            self.vertices[ids] = new_vertex
            return True
        else:
            return False
    #returns the vertex if it exists in the graph else none
    def get_vertex(self, ids):
        return None if ids not in self.vertices.keys() else  self.vertices[ids]
    
    #returns all nodes in the graph
    def get_all_vertices(self):
        return self.vertices
    
    #delete a vertex from the graph
    def delete_vertex(self, ids):
        if ids not in self.vertices.keys():
            return False

        else:
            node =  self.vertices[ids]
            neighbours = self.vertices[ids].get_neighbours()

            for n in neighbours:
                n.delete_neighbour[node]

            del self.vertices[ids]
    
    #test to see if two vertices are have an edge, directed or undirected
    def is_adjacent_vertex(self, fromm, too):
        if fromm not in self.vertices.keys() or too not in self.vertices.keys():
            return False
        else:
            if too in  self.vertices[fromm].get_neighbours() or fromm in  self.vertices[to].get_neighbours():
                return True
            else:
                return False


    #given a vertex/node find all the neighbours of that vertex/node
    def get_neighbours(self, ids):
        return self.vertices[ids].get_neighbours() if ids in self.vertices.keys() else None

    #print all the vertices in the graph 
    def print_vertices(self):
        for v in self.vertices.keys():
            print v, self.vertices[v]

   #---------------------------------------------# 
def make_graph(g):
    for i in range(0,7):
        g.add_vertex(i)
 

    g.add_edge(0,1,5)
    g.add_edge(0,2,5)
    g.add_edge(1,3,4)
    g.add_edge(3,4,1)
    g.add_edge(4,2,2)
    g.add_edge(5,6,3)
    g.add_edge(6,6,2)


    print g.get_edge_value(4,2)
    g.set_edge_value(4,2,22)
    print g.get_edge_value(4,2)
if __name__ == '__main__':

    g = graph()
    make_graph(g)