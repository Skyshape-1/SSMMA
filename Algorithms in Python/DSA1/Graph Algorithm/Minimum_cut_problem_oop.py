# Unresolved problems in design are marked by TBC (Use search to locate)
# Currently having removed the inheritance between Vertx and SuperVertex
import random

### Collections ###

# Vertex Collection #
class VerCol():
    def __init__(self):
        self.verlist = []
    
    def add_vert(self, Vert):
        self.verlist.append(Vert)
    
    def remove_vert(self, Vert):
        if Vert in self.verlist:
            self.verlist.remove(Vert)
    
    def merge_vert(self, v1, v2, EdgeCol):
        new_SV = SuperVert(v1, v2)
        new_SV.rewire_call(EdgeCol)
        self.add_vert(new_SV)
        self.remove_vert(v1)
        self.remove_vert(v2)
    
    def get_num_remain(self):
        return len(self.verlist)
    
    def get_first_ele(self):
        if len(self.verlist) > 0:
            res = self.verlist[0]
            self.verlist.remove(res)
            return res
        print("No elements left in VerCol to get.")
    
# Edge Collection #
class EdgeCol():
    def __init__(self):
        self.edgelist = []
    
    def add_edge(self, Edge):
        self.edgelist.append(Edge)
    
    def remove_edge(self, Edge):
        if Edge in self.edgelist:
            self.edgelist.remove(Edge)
            
    def sel_rand_edge(self):
        return random.choice(self.edgelist)

    def edge_contract(self, VerCol):
        sel_edge = self.sel_rand_edge()
        ep1, ep2 = sel_edge.get_eps()[0], sel_edge.get_eps()[1]
        VerCol.merge_vert(ep1, ep2, self)
    
    def get_num_remain(self):
        return len(self.edgelist)
    

### Primitives ###
# Vertices #
class Vert():
    def __init__(self, id):
        self.id = id
        self.contain = [id]
        self.incident_edges = []
    
    def get_id(self):
        return self.id

    def link_edge(self, Edge):
        self.incident_edges.append(Edge)
    
    def get_contain(self):
        return self.contain

    def get_inci_edges(self):
        return self.incident_edges
    
    def get_all_contain_and_num(self): # Duplicated from SuperVert
        return (self.contain, 1)

# Edges #
class Edge():
    def __init__(self, v1, v2):
        self.endpoints = [v1, v2]
        v1.link_edge(self)
        v2.link_edge(self)
        
    def rewire(self, endp1, newp1):
        if endp1 not in self.endpoints:
            # print("Invalid Endpoint Input!")
            return
        self.endpoints.remove(endp1)
        self.endpoints.append(newp1)
        # print(f"Rewired successfully: Edge({self.endpoints[0]}, {self.endpoints[1]})")
    
    def is_self_loop(self):
        return self.endpoints[0] == self.endpoints[1]
    
    def get_eps(self):
        return self.endpoints

# Super Vertices #
class SuperVert(): 
    def __init__(self, v1, v2): 
        if v1 == v2:
            print("Merging the duplicate vertices!")
            return
        self.ep1, self.ep2 = v1, v2
        self.contain = v1.get_contain() + v2.get_contain()
        self.incident_edges = v1.get_inci_edges() + v2.get_inci_edges() # Rewire on SV side completed
    
    def rewire_call(self, EdgeCol):
        to_remove = []
        for edge in self.incident_edges[:]:  # Iterate over a copy
            edge.rewire(self.ep1, self)
            edge.rewire(self.ep2, self)
            if edge.is_self_loop():
                EdgeCol.remove_edge(edge)
                to_remove.append(edge)
        for edge in to_remove:
            while edge in self.incident_edges:
                self.incident_edges.remove(edge)
        
    def get_all_contain_and_num(self):
        return (self.contain, len(self.contain))
    
    def get_contain(self):
        return self.contain

    def get_inci_edges(self):
        return self.incident_edges




