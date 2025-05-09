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
        assert key not in self.index
        self.index[key] = len(self.min_heap)
        self.min_heap.append([key, value])
        self.__heapify_up(len(self.min_heap) - 1)

    def popmin(self):
        assert len(self.min_heap) > 0
        r = self.min_heap[0][0]
        if len(self.min_heap) > 1:
            self.__swap(0, len(self.min_heap) - 1)
            self.min_heap.pop()
            self.__heapify_down(0)
        del self.index[r]
        return r

    def peek(self):
        assert len(self.min_heap) > 0
        return self.min_heap[0][0]

    def decrease_key(self, key, new_value):
        assert key in self.index
        i = self.index[key]
        assert new_value < self.min_heap[i][1]
        self.min_heap[i][1] = new_value
        self.__heapify_up(i)
    
    def __heapify_up(self, i):
        p = (i - 1) // 2
        if p >= 0 and i >= 0 and self.min_heap[i][1] < self.min_heap[p][1]:
            self.__swap(i, p)
            self.__heapify_up(p)

    def __heapify_down(self, i):
        if i < 0 or i >= len(self.min_heap):
            return
        l = (2 * i) + 1
        r = (2 * i) + 2
        if l < len(self.min_heap) and self.min_heap[i][1] > self.min_heap[l][1]:
            self.__swap(i, l)
            self.__heapify_down(l)
        if r < len(self.min_heap) and self.min_heap[i][1] > self.min_heap[r][1]:
            self.__swap(i, r)
            self.__heapify_down(r)

    def __swap(self, i, j):
        assert i >= 0 and i < len(self.min_heap)
        assert j >= 0 and j < len(self.min_heap)
        k1, k2 = self.min_heap[i][0], self.min_heap[j][0]
        assert k1 in self.index
        assert k2 in self.index
        self.index[k1], self.index[k2] = self.index[k2], self.index[k1]
        self.min_heap[i], self.min_heap[j] = self.min_heap[j], self.min_heap[i]

    def __len__(self):
        return len(self.min_heap)

'''
Problem 2
Dijkstras minimum path from s to t
You should use the Indexed priority queue from problem 1
'''
def Dijkstras(G, s, t):
    ipq = IndexedPriorityQueue()

    def relax(v, x, e):
        if G.nodes[v]["dist"] + e["weight"] < G.nodes[x]["dist"]:
            G.nodes[x]["parent"] = v
            G.nodes[x]["dist"] = G.nodes[v]["dist"] + e["weight"]
            ipq.decrease_key(x, G.nodes[x]["dist"])

    for x in G.nodes:
        G.nodes[x]["parent"] = None
        G.nodes[x]["dist"] = float('inf')
        ipq.push(x, G.nodes[x]["dist"])
    ipq.decrease_key(s, 0)
    G.nodes[s]["dist"] = 0

    seen = set()
    while len(ipq) > 0:
        v = ipq.popmin()
        if v == t:
            path = []
            n = t
            while n != None:
                path.append(n)
                if n == s:
                    break
                n = G.nodes[n]["parent"]
            path.reverse()
            return path

        for x in G.neighbors(v):
            if x not in seen:
                relax(v, x, G.edges[(v, x)])
        
        seen.add(v)
    return None

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
print(" -> ".join(Dijkstras(G, "a", "e")))
