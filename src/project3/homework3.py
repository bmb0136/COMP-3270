'''
COMP 3270 coding section
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
parser.add_argument("--graph", help="file containing graph in pickle format for problem 1")
args = parser.parse_args()

'''
Problem 1
Implement the disjoint-set / union-find data structure with path compression
'''
class DisjointSet:
    # data structure to back the disjoint set here (you can use an array, a dict, or you could use a graph)
    
    def __init__(self):
        # initialize here

    def makeset(self, x):
        # your code here        
    
    def find(self, x):
        # your code here

    def union(self, x, y):
        # your code here


    





'''
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
'''
def kruskal(G):
    print("output")






# load graphs and run functions

graph = pickle.load(open(args.graph,'rb'))
kruskal(graph)


