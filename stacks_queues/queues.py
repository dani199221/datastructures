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


class queue:

    def __init__(self):
        self.queue = link_list()


    def enqueue(self, val):
        self.queue.insert_at_tail(val)

    def dequeue(self):
        return self.queue.delete_head()


    def empty(self):
        return self.queue.is_empty()

    def top(self):
        return self.queue.get_head().val


if __name__ == '__main__':
    q = queue()
    print q.empty()
