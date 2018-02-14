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

    
    #instead of moving one pointer twice and other once
    #have it the way that you just move the slow pty
    #every other iteration
    def insert_middle(self, val):
        fast = self.head
        slow = self.head
        tick = False
        
        while fast:
            fast = fast.next
            if tick:
                slow = slow.next
            tick = not tick

        tmp = Node(slow.val)
        tmp.next = slow.next
        slow.next = tmp
        slow.val = val

    def insert_sorted(self, val):
        tmp = self.head

        while tmp.next != None and tmp.next.val < val:
            tmp = tmp.next

        res = Node(val)
        res.next = tmp.next
        tmp.next = res
        return True

    def compare_str(self, s1, s2):
        if not s1 and not s2:
            return True

        if (s1 == None and s2 != None) or (s2 == None and s1 != None):
            return False

        if s1.val == s2.val:
            return self.compare_str(s1.next, s2.next)
        else:
            return False
if __name__ == '__main__':

    l = link_list()
    l.head = Node('g')
    l.head.next = Node('e')
    l.head.next.next = Node('e')
    l.head.next.next.next = Node('k')
    l.head.next.next.next.next = Node('s')
    
    l2 = link_list()
    l2.head = Node('g')
    l2.head.next = Node('e')
    l2.head.next.next = Node('e')
    l2.head.next.next.next = Node('k')
    l2.head.next.next.next.next = Node('s')
    #for i in range(10,0,-1):
    #    l.insert_at_head(i)
    
    print l.compare_str(l.head, l2.head)
    #l.insert_sorted(5)
    #print l
