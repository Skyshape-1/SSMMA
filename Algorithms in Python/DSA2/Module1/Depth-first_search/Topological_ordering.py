import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Breadth_first_search.visualize_graph import visualize_graph

# Example of a Directed Acyclic Graph (DAG)
graph1 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

if __name__ == "__main__":
    visualize_graph(graph1)