'''
COMP 3270 Intro to Algorithms Homework 5 coding section
requires networkx, argparse
requires python 3.6+ (can get with anaconda or elsewhere, note standard python with mac is python 2)
pip install networkx
pip install argparse
'''

import argparse
import networkx as nx
import pickle
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
args = parser.parse_args() # no arguments but im leaving this here

'''
Problem 1
Implement the indexed priority queue data structure backed by a list based min-heap 
and a dict based index.
Hint: if you store a binary tree in a vector with each new element being the final
element in the vector representing the last leaf node at the deepest level, you can
compute the index of the children of the node at position i as 2i+1 and 2i+2
You cannot import Queue or any other package for this problem.
'''
class IndexedPriorityQueue:
    def __init__(self):
        self.min_heap = []
        self.index = {}

    def push(self, key, value):
        self.min_heap.append((key, value))
        self.__heapify_up(len(self.min_heap) - 1)
        pass

    def popmin(self):
        assert len(self.min_heap) > 0
        if len(self.min_heap) == 1:
            r = self.min_heap[0]
            self.min_heap.pop()
            return r[1]
        self.__swap(self.min_heap[0][0], self.min_heap[-1][0])
        r = self.min_heap[-1][1]
        self.min_heap.pop()
        self.__heapify_down(0)
        return r
        

    def peek(self):
        assert len(self.min_heap) > 0
        return self.min_heap[0][1]

    def decrease_key(self, key, new_value):
        pass
    
    def __heapify_up(self, i):
        p = (i - 1) // 2
        if i >= 0 and p >= 0 and self.min_heap[i][0] < self.min_heap[p][0]:
            self.__swap(i, p)
            self.__heapify_up(p)

    def __heapify_down(self, i):
        while i < len(self.min_heap):
            l = (2 * i) + 1
            r = (2 * i) + 2
            if l < len(self.min_heap) and self.min_heap[i][0] > self.min_heap[l][0]:
                self.__swap(i, l)
                self.__heapify_down(l)
            if r < len(self.min_heap) and self.min_heap[i][0] > self.min_heap[r][0]:
                self.__swap(i, r)
                self.__heapify_down(r)

    def __swap(self, i, j):
        assert i >= 0 and i < len(self.min_heap)
        assert j >= 0 and j < len(self.min_heap)
        k1 = self.min_heap[i][0]
        k2 = self.min_heap[j][0]
        self.index[k1], self.index[k2] = j, i
        self.min_heap[i], self.min_heap[j] = self.min_heap[j], self.min_heap[i]

'''
Problem 2
Dijkstras minimum path from s to t
You should use the Indexed priority queue from problem 1
'''
def Dijkstras(G, s, t):
    # your code here
    pass

# make graph and run functions

G = nx.Graph()
G.add_nodes_from([x for x in "abcdef"])
G.add_edge("a","b", weight=14)
G.add_edge("a","c", weight=9)
G.add_edge("a","d", weight=7)
G.add_edge("b","c", weight=2)
G.add_edge("b","e", weight=9)
G.add_edge("c","d", weight=10)
G.add_edge("c","f", weight=11)
G.add_edge("d","f", weight=15)
G.add_edge("e","f", weight=6)
Dijkstras(G, "a", "e")
