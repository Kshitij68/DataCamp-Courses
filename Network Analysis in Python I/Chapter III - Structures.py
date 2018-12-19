import networkx as nx
import matplotlib.pyplot as plt
"""
Structures and Sub-Graphs using networkx
Cliques
    Social cliques: tightly-knit groups
    Network cliques: Completely connected graphs

Triangle Application
    Friend Recommendations

Maximal Cliques
    A clique that, when extended by one node is no longer a clique
"""

# To check if a node is in triangle
from itertools import combinations
# Define is_in_triangle()

def is_in_triangle(G, n):
    """
    Checks whether a node `n` in graph `G` is in a triangle relationship or not.

    Returns a boolean.
    """
    in_triangle = False

    # Iterate over all possible triangle relationship combinations
    for n1, n2 in combinations(G.neighbors(n), 2):

        # Check if an edge exists between n1 and n2
        if G.has_edge(n1, n2):
            in_triangle = True
            break
    return in_triangle

"""
SubGraphs
    Visualize portions of large graphs 
        Paths
        Communities / cliques
        Degrees of separation from a node
"""
nodes_of_interest = [29, 38, 42]
def get_nodes_and_nbrs(G, nodes_of_interest):
    """
    Returns a subgraph of the graph `G` with only the `nodes_of_interest` and their neighbors.
    """
    nodes_to_draw = []

    # Iterate over the nodes of interest
    for n in nodes_of_interest:

        # Append the nodes of interest to nodes_to_draw
        nodes_to_draw.append(n)

        # Iterate over all the neighbors of node n
        for nbr in G.neighbors(n):
            # Append the neighbors of n to nodes_to_draw
            nodes_to_draw.append(nbr)

    return G.subgraph(nodes_to_draw)


# Extract the subgraph with the nodes of interest: T_draw
T_draw = get_nodes_and_nbrs(T, nodes_of_interest)

# Draw the subgraph to the screen
nx.draw(T_draw)
plt.show()