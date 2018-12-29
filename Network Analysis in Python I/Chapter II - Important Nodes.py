"""
Degree Centrality
Betweeness Centrality

The important nodes can be identified by seeing how many nodes it is connected to
Degree Centrality: Number of Neighbours I have  / Number of Neighbours I could possibly have
Example of nodes with high degree centrality:
    Twitter Broadcasters: User followed by many other users
    Airport Transportation Hubs: such as New York or London Airports
    Disease Super-Spreaders: Individuals that can spread disease very fast

Degree Distribution: The number of neighbors that a node has is called its 'degree' and its possible to compute the \
degree distribution across the entire graph

print(G.edges())
=> Prints all the edges in the Graph

print(G.neighbors(1))
=> Prints the neighbors of node 1

nx.degree_centrality(G)
=> Prints a dictionary with each nodes degree centrality
Self loops are not considered
"""
import networkx as nx

# Get all the nodes with m neighbors
def nodes_with_m_nbrs(G, m):
    """
    Returns all nodes in graph G that have m neighbors.
    """
    nodes = set()

    # Iterate over all nodes in G
    for n in G.nodes():

        # Check if the number of neighbors of n matches m
        if len(G.neighbors(n)) == m:
            # Add the node n to the set
            nodes.add(n)

    # Return the nodes with m neighbors
    return nodes

"""
Path Finding
    Optimization: Shortest Transport Paths
    Modeling: Disease Spread, Information Passing
    
Breadth-First-Search (BFS)
    Step I: Look at the adjacent nodes
    Step II: Check if the desired node is achieved
    Step III: If reached, end. Else go back to Step I
Recursion makes sense for this
"""

# To check if node1 and node2 are connected
def path_exists(G, node1, node2):
    """
    This function checks whether a path exists between two nodes (node1, node2) in graph G.
    """
    visited_nodes = set()
    queue = [node1]

    for node in queue:
        neighbors = G.neighbors(node)
        if node2 in neighbors:
            print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
            break

        else:
            visited_nodes.add(node)
            queue.extend([n for n in neighbors if n not in visited_nodes])

        # Check to see if the final element of the queue has been reached
        if node == queue[-1]:
            print('Path does not exist between nodes {0} and {1}'.format(node1, node2))

            # Place the appropriate return statement
            return False
"""
Betweeness Centrality
= Number of shortest paths through node / All possible shortest paths

Find shortest path between every pair of nodes
All shortest paths are:
    Set of path
    Each path is shortest path between a given pair of nodes
    Done for all node pairs
    
Application
    Bridges between liberal and conservative leaning Twitter users
    Critical information transfer links
"""


# Define find_nodes_with_highest_deg_cent()
def find_nodes_with_highest_deg_cent(G):
    # Compute the degree centrality of G: deg_cent
    deg_cent = nx.degree_centrality(G)

    # Compute the maximum degree centrality: max_dc
    max_dc = max(list(deg_cent.values()))

    nodes = set()

    # Iterate over the degree centrality dictionary
    for k, v in deg_cent.items():

        # Check if the current value has the maximum degree centrality
        if v == max_dc:
            # Add the current node to the set of nodes
            nodes.add(k)

    return nodes

# Find the node(s) that has the highest degree centrality in T: top_dc
top_dc = find_nodes_with_highest_deg_cent(T)
print(top_dc)

# Write the assertion statement
for node in top_dc:
    assert nx.degree_centrality(T)[node] == max(nx.degree_centrality(T).values())


# Define find_node_with_highest_bet_cent()
def find_node_with_highest_bet_cent(G):
    # Compute betweenness centrality: bet_cent
    bet_cent = nx.betweenness_centrality(G)

    # Compute maximum betweenness centrality: max_bc
    max_bc = max(list(bet_cent.values()))

    nodes = set()

    # Iterate over the betweenness centrality dictionary
    for k, v in bet_cent.items():

        # Check if the current value has the maximum betweenness centrality
        if v == max_bc:
            # Add the current node to the set of nodes
            nodes.add(k)

    return nodes


# Use that function to find the node(s) that has the highest betweenness centrality in the network: top_bc
top_bc = find_node_with_highest_bet_cent(T)

# Write an assertion statement that checks that the node(s) is/are correctly identified.
for node in top_bc:
    assert nx.betweenness_centrality(T)[node] == max(nx.betweenness_centrality(T).values())