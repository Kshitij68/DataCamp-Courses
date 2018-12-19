"""
Networks
Social Network: Modeling relationship between people
Transportation Network: Modeling relationship between routes

By modeling the data in networks, you can end up gaining insights on what entities or nodes are important

Networks are described by two set of items:
-> Nodes
-> Edges
Together these form a network, also called a graph.
Nodes and Edges can have meta-deta
"""

import networkx as nx
from nxviz.plots import ArcPlot
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
print(G.nodes())
# [1,2,3]
G.add_edge(1,2)
print(G.edges())
# [(1,2)]
G.node[1]['label'] = 'blue'
G.nodes(data = True) # Passing data = True argument returns the nodes along with the metadeta

nx.draw(G)
import matplotlib.pyplot as plt
plt.show()

"""
Types of graphs
Undirected graphs: Facebook Social Graph (Edges with no sense of directionality
Directed Graphs: Twitter Social Graph (Edges with sense of directionality)
Multi(Di) Graphs: Multiple nodes between edges
Self Loops: Nodes that are connected to themselves
"""

G = nx.Graph()
print(type(G))
# networkx.classes.graph.Graph

D = nx.DiGraph()
print(type(D))
# networkx.classes.digraph.DiGraph

M = nx.MultiGraph()
print(type(M))
# networkx.classes.multigtaph.MultiGraph

MD = nx.MultiDiGraph()
print(type(MD))
# networkx.classes.multidigraph.MultiDiGraph

# Twitter data
T = nx.DiGraph()
print(T.nodes)


"""
Network Visualization
-> Matrix Plot: 
Nodes are the rows and columns of the matrix. 
Cells are filled in according to whether an edge exists between the pair of nodes
Undirected graph will always result in symmetrical matrix
-> Arc Plot:
All the nodes are put in a single axis and edges are drawn using circular arcs
-> Circos Plots
Transformation of the arc plot such that the nodes are in a circle 
"""
import nxviz as nv
ap = nv.ArcPlot(G)
ap.draw()
plt.show()


# Convert T to a matrix format: A
A = nx.to_numpy_array(T)
# Convert A back to 'category' metadeta field is lost from each node
T_conv = nx.from_numpy_matrix(A,create_using=nx.DiGraph)

for n,d in T_conv.nodes(data = True):
    assert 'category' not in d.keys()


# nv.MatrixPlot(G): To draw a matrix plot
# nv.CircosPlot(G): To draw a line plot

# To specify the ordering and coloring of nodes
a2 = nv.ArcPlot(T, node_order = 'category', node_color='category')