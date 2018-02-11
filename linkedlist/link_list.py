#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 danial <danial@danial-Blade>
#
# Distributed under terms of the MIT license.

"""
    My implementation of link_list data structure
"""

class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None



class link_list:
    
    def __init__(self):
        self.head = None
    
    def get_head(self):
        return self.head

    def is_empty(self):
        return self.head == None

    def insert_at_head(self, val):

        if self.head == None:

            self.head = Node(val)
            return self.head
        else:

            ins = Node(val)
            ins.next = self.head
            self.head =ins
            return ins

    def delete_head(self):
        if self.head == None:
            raise Exception("Empty list")
        else:
            self.head = self.head.next
            return True
    
    def insert_at_tail(self, val):

        if self.head  == None:
            self.head = Node(val)
            return self.head

        else:
            tmp = self.head
            while (tmp.next != None):
                tmp  = tmp.next

            ins = Node(val)
            tmp.next = ins

            return ins

    def delete_tail(self):
        if self.head == None:
            raise Exception("Empty list")

        elif self.head.next == None:
            self.head == None
            return True

        else:
            tmp = self.head

            while tmp.next.next != None:
                tmp = tmp.next
            
            tmp.next = None
            return True

    def insert_after(self, val):
        
        if self.head == None:
            raise Exception("Empty list. Cannot insert after")

        else:
            tmp =  self.head
            while(tmp.val != val and tmp !=  None):
                tmp = tmp.next

            if not tmp:
                raise Exception(val, " does not exist in the list")
            else:
                tmp2 = tmp.next
                ins = Node(val)
                ins.next = tmp2
                tmp.next = ins
                return ins
                
                
    def delete_val(self, val):

        if self.head == None:
            raise Exception("Empty list. Cannot delete value")
        else:
            tmp = self.head
            prev = tmp
            while tmp.val != val and tmp != None:
                prev = tmp
                tmp = tmp.next
            
            if tmp == None:
                raise Exception("Value does not exist in list")
            else:
                prev.next = tmp.next

    def length(self):

        size = 0
        tmp  = self.head
        while tmp != None:
            tmp = tmp.next
            size += 1

        return size

    def __contains__(self, val):
        tmp = self.head
        
        contains = False
        while (tmp != None):
            if tmp.val == val:
                contains = True

            tmp = tmp.next

        return contains
    

    def __str__(self):
        tmp = self.head
        res = []
        while tmp != None:
            res.append(tmp.val)
            tmp = tmp.next
        
        return " ".join([str(r) for r in res]) 

if __name__ == '__main__':
    l = link_list()
    
    for i in range(10,-1,-1):
        l.insert_at_head(i)

    print l

    for i in range(10,-1,-1):
        l.delete_head()

