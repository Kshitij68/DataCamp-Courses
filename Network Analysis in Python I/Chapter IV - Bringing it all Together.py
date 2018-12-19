""""
We are going to do one-indepth case study to solidify our knowledge
    Github user collaboration network
    Nodes: Users
    Edges: Collaboration on same Github repository
Goals:
    Analyze structure of the graph
    Visualize the graph
    Build simple recommendation system

Data
    Number of nodes
    Number of edges
    Degree centrality distribution
    Betweenness centrality distribution

Connected Component SubGraphs
A set of nodes connected to one another through some paths in a sub-graph and not connected to the other nodes in the graphs

Cliques are:
    Group of nodes
    Fully Connected
Simplest clique: Edge
Simplex Complex clique: Triangle

Maximal Cliques
    A clique that cannot be extended by adding a node

Final Tasks
    Find important users - Degree Centrality
    Find largest communities of collaborators - Maximal Clique Concept
    Build a collaboration recommendation system - Open Triangles
"""
from nxviz import MatrixPlot
import matplotlib.pyplot as plt

# Calculate the largest connected component subgraph: largest_ccs
largest_ccs = sorted(nx.connected_component_subgraphs(G), key=lambda x: len(x))[-1]

# Create the customized MatrixPlot object: h
h = MatrixPlot(largest_ccs,node_grouping = 'grouping')

# Draw the MatrixPlot to the screen
h.draw()
plt.show()


# Recommendar System
# Import necessary modules
from itertools import combinations
from collections import defaultdict

# Initialize the defaultdict: recommended
recommended = defaultdict(int)

# Iterate over all the nodes in G
for n, d in G.nodes(data=True):

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n), 2):

        # Check whether n1 and n2 do not have an edge
        if not G.has_edge(n1, n2):
            # Increment recommended
            recommended[(n1, n2)] += 1

# Identify the top 10 pairs of users
all_counts = sorted(recommended.values())
top10_pairs = [pair for pair, count in recommended.items() if count > all_counts[-10]]
print(top10_pairs)


