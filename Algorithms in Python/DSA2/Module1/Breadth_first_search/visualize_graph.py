import matplotlib.pyplot as plt
import networkx as nx

if "__name__" == "__main__":
    # Define graph2 (copy from your main.py)
    graph2 = {
        'A': ['B', 'C', 'E'],
        'B': ['A', 'D', 'F'],
        'C': ['A', 'D', 'G'],
        'D': ['B', 'C', 'H'],
        'E': ['A', 'F'],
        'F': ['B', 'E', 'H'],
        'G': ['C', 'H'],
        'H': ['D', 'F', 'G']
    }

    G = nx.Graph()
    for node, neighbors in graph2.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1200, font_size=14, edge_color='gray')
    plt.title("Visualization of graph2")
    plt.show()

def visualize_graph(graph):
    if type(graph) != dict:
        print("Invalid input! Graph must be represented by a dictionary!")
        raise TypeError
    
    # Visualization
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1200, font_size=14, edge_color='gray')
    plt.title("Visualization of Your Graph")
    plt.show()