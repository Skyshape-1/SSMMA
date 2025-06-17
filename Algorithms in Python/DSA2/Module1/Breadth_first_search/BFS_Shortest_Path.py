# Goal: Implement an algorithm that can compute the shortest path between two vertices in a graph
# Input: node v1, node v2, graph G
# Output: an integer if v1 and v2 are connected;
#         Otherwise, a line of text "Nodes v1 and v2 are disconnected."

# Test case #
graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

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


# Main Function #
def shortest_path(graph, node1, node2):
    dis_dict = bfs_for_shortest_path(graph, node1)
    if dis_dict[node2][1]:
        return f"Nodes v1 and v2 are {dis_dict[node2][0]} edges apart."
    else:
        return "Nodes v1 and v2 are disconnected."


# BFS algorithm (Customized) #
# Input: a graph G and a starting node s
# Output: a dictionary whose keys are all reachable nodes from s 
#         and whose values are integers marking keys' distances from s
def bfs_for_shortest_path(graph, start_node):
    # HOW to create a dict whose keys are nodes of G with all values initialized as False
    status_dict = {key: ["Inf", False] for key in graph} 
    quene = Quene()
    quene.put_item(start_node)
    status_dict[start_node][0], status_dict[start_node][1] = 0, True
    
    while quene.get_length() > 0:
        source = quene.pop_item()
        for node in graph[source]:
            if not status_dict[node][1]:
                quene.put_item(node)
                status_dict[node][0], status_dict[node][1] = status_dict[source][0] + 1, True
    
    return status_dict

class Quene():
    def __init__(self):
        self.quene = []
    
    def get_length(self):
        return len(self.quene)
    
    def put_item(self, item):
        self.quene.append(item)
    
    def pop_item(self):
        try:
            return self.quene.pop(0) 
        except IndexError:
            print("#####")
            print("Quene is empty. Can not pop item.")
            print("#####")                
    
    def get_item(self):
        try:
            return self.quene[0]
        except IndexError:
            print("#####")
            print("Quene is empty. Can not return item.")
            print("#####")                

def test_case():
    # Graph 1
    print("-------------")
    print(shortest_path(graph1, 'A', 'D'))
    print("The expected answer: 2 edges apart.")
    print("-------------")
    print(shortest_path(graph1, 'A', 'B'))
    print("The expected answer: 1 edges apart.")
    # Graph 2
    print("-------------")
    print(shortest_path(graph2, 'A', 'H'))
    print("The expected answer: 3 edges apart.")
    print("-------------")
    print(shortest_path(graph2, 'D', 'E'))
    print("The expected answer: 3 edges apart.")

if __name__ == "__main__":
    # Only runs when this file is executed directly
    print("Testing BFS-ShortestPath...")
    # test cases here
    test_case()