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
sys.path.append('../linkedlist')
from  link_list import *

class Stack:

    def __init__(self):
        self.stack = link_list() 
    

    def push(self, val):
        self.stack.insert_at_head(val)

    def pop(self):
        return self.stack.delete_head()

    def top(self):
        return self.stack.get_head().val

    def empty(self):
        return self.stack.is_empty()
