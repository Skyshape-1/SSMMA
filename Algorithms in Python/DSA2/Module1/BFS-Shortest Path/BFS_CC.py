# # Connected Components in Undirected Graph 

# ## Method
#     The Breadth-first Search algorithm is to be used to find the CC in an undirected graph G

# ## Input and Output
# Input: 
#     An undirected graph G 
# Output: 
#     A dictionary consisting of group indices (as keys) and a list of nodes belonging to that group (as values)
#     * Each group represents a CC

# ## Formatted Printing
#     The outputted dictionary will be printed in the following format:
#     '''Group {group_idx} contains: [a list of nodes in that CC]'''


# Import the Quene class from BFS-Shortest_Path.py
from BFS_Shortest_Path import Quene
from visualize_graph import visualize_graph
# Test Case
graph_test = {
    # CC1
    'A': ['B', 'C', 'D'],
    'B': ['C', 'A'],
    'C': ['A', 'B'],
    'D': ['A'],
    # CC2
    'E': ['F'],
    'F': ['E'],
    # CC3
    'H': ["I", "J"],
    'J': ["H", "I"],
    'I': ["H", "J"]
}


def test():
    res = find_connected_components(graph_test)
    for idx in res:
        print(f"Group {idx} contains: {res[idx]}")

# Return an named dictionary of groupings
def find_connected_components(graph):
    groupings = bfs_cc(graph)
    col_dict, i = {}, 1
    for group in groupings:
        col_dict[str(i)] = group
        i += 1
    return col_dict


# Output: a list of lists, each containing members of a CC
def bfs_cc(graph):
    
    status_dictionary = {key: -1 for key in graph}

    quene = Quene()
    cc_lst = []
    for node in graph:
        if status_dictionary[node] < 0:
            cc = [node]
            status_dictionary[node] = 1
            quene.put_item(node)
            while quene.get_length() > 0:
                consider = quene.pop_item()
                for ele in graph[consider]:
                    if status_dictionary[ele] < 0:
                        status_dictionary[ele] = 1
                        quene.put_item(ele)
                        cc.append(ele)
            cc_lst.append(cc)
    
    return cc_lst

# Running WD
if __name__ == "__main__":
    visualize_graph(graph_test)
    test()
