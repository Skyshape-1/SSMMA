from Minimum_cut_problem_oop import *
# main() runs the Random Cut Algorithm n^2 times
def main():
    number_of_vertices = 8 # n

    min_cut = float('inf')
    best_A = best_B = None
    num_runs = number_of_vertices*2  # N = n^2

    for _ in range(num_runs):
        ### Re-initialize graph for each run

        # Initiating Collections
        vertices = VerCol()
        edges = EdgeCol()
        # Initiating vertices
        id_list_ver = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8']
        ver_dict = {}
        for id in id_list_ver:
            ver_dict[id] = Vert(id)
            vertices.add_vert(ver_dict[id])
        # Initiating edges 
        edge_lst = [
            Edge(ver_dict["v1"], ver_dict["v2"]),
            Edge(ver_dict["v2"], ver_dict["v3"]),
            Edge(ver_dict["v3"], ver_dict["v4"]),
            Edge(ver_dict["v1"], ver_dict["v5"]),
            Edge(ver_dict["v1"], ver_dict["v6"]),
            Edge(ver_dict["v2"], ver_dict["v5"]),
            Edge(ver_dict["v2"], ver_dict["v6"]),
            Edge(ver_dict["v3"], ver_dict["v7"]),
            Edge(ver_dict["v3"], ver_dict["v8"]),
            Edge(ver_dict["v4"], ver_dict["v7"]),
            Edge(ver_dict["v4"], ver_dict["v8"]),
            Edge(ver_dict["v5"], ver_dict["v6"]),
            Edge(ver_dict["v6"], ver_dict["v7"]),
            Edge(ver_dict["v7"], ver_dict["v8"])
        ]
        for edge in edge_lst:
            edges.add_edge(edge)

        # Algorithm in Action #
        while vertices.get_num_remain() > 2:
            edges.edge_contract(vertices)
        A = vertices.get_first_ele().get_all_contain_and_num()
        B = vertices.get_first_ele().get_all_contain_and_num()
        # A, B are tuples: 
        # (list of contained ids of Verts, len(that list))
        cut_size = edges.get_num_remain()

        
        if cut_size < min_cut:
            min_cut = cut_size
            best_A, best_B = A, B

    print("Minimum cut found:", min_cut)
    print("Primitive vertices in group A:")
    for ele in best_A[0]:
        print(ele)
    print(f'Total: {best_A[1]} vertices.')

    print("Primitive vertices in group B:")
    for ele in best_B[0]:
        print(ele)
    print(f'Total: {best_B[1]} vertices.')

main()