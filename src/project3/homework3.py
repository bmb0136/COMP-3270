"""
COMP 3270 coding section
requires networkx, argparse
requires python 3.6+ (can get with anaconda or elsewhere, note standard python with mac is python 2)
pip install networkx
pip install argparse
"""

import argparse
from typing import override
import networkx as nx
import pickle
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument(
    "--graph", help="file containing graph in pickle format for problem 1"
)
args = parser.parse_args()

"""
Problem 1
Implement the disjoint-set / union-find data structure with path compression
"""


class DisjointSet:
    def __init__(self):
        self.mapping = {}
        self.mapping_rev = {}
        self.next_id = 0
        self.parents = []

    def makeset(self, x):
        assert x not in self.mapping
        self.mapping[x] = self.next_id
        self.mapping_rev[self.next_id] = x
        self.parents.append(self.next_id)
        self.next_id += 1

    def find(self, x):
        return self.mapping_rev[self._find(self.mapping[x])]

    def _find(self, id):
        next = self.parents[id]
        if next == id:
            return id 
        r = self._find(next)
        self.parents[id] = r 
        return r

    def union(self, x, y):
        x = self._find(self.mapping[x])
        y = self._find(self.mapping[y])
        if x != y:
            self.parents[y] = x

    def components(self):
        return sum((1 if i == x else 0) for i, x in enumerate(self.parents))

    @override
    def __str__(self) -> str:
        return f"DisjointSet [{", ".join(f"{x}->{self.find(x)}" for x in self.mapping.keys())}] ({self.components()} CC)"

"""
Problem 2
find the minimum spanning tree of G using your disjoint set data structure above
then draw the graph with the edges in the MST twice as thick as the other edges and save that to mst.png

some code I used to draw the graph
edge_labels = nx.get_edge_attributes(G, "weight") # get edge labels
pos = nx.spring_layout(G) # get position of nodes with a spring model layout
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.axis("off")
plt.savefig('graph.png')
"""


def kruskal(G):
    get_weight = lambda e: G[e[0]][e[1]]["weight"]
    E = sorted(G.edges, key=get_weight)
    ds = DisjointSet()
    for n in G.nodes:
        ds.makeset(n)
    mst = nx.Graph()
    for x, y in E:
        e = (x, y)
        x = ds.find(x)
        y = ds.find(y)
        if x != y:
            ds.union(x, y)
            mst.add_edge(x, y, weight=get_weight(e))
    return mst

# load graphs and run functions

graph = pickle.load(open(args.graph, "rb"))
mst = kruskal(graph)

edge_labels = nx.get_edge_attributes(mst, "weight")
pos = nx.spring_layout(mst)
nx.draw_networkx_edges(mst, pos)
nx.draw_networkx_nodes(mst, pos)
nx.draw_networkx_labels(mst, pos)
nx.draw_networkx_edge_labels(mst, pos, edge_labels)
plt.axis("off")
plt.savefig("mst.png")
