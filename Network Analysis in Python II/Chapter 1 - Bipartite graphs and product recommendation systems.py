"""
Network = Graph = (nodes, edges)

networkx: API for analysis of graphs
nxvix: Visualize a large dataset to create beautiful Visualizations like
    Matrix plot
    Arc Plot
    Circos Plot
    Hive Plot

import neworkx as nx

G.nodes() : Prints all the nodes in a list
len(G.nodes()) : Total number of nodes in a graph
len(G.edges()) : Total number of edges in a graph

import nxviz as nv
import matplotlib.pyplot as plt
c = nv.CircosPlot(G)
c.draw()
plt.show()
"""