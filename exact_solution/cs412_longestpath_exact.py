"""
    name:  Brady Walsh

            Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
              https://stackoverflow.com/q/19798480
  
           Comments here on your code and submission
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
import random


def main():
    graph = create_graph(25, 1, 100)
    for node in graph:
        print(node, graph[node])
    longest_path_length, longest_path = find_longest_path(graph, 0, None, 0)
    
    print(f"Longest Path Length (by weight): {longest_path_length}")
    print(f"Longest Path: {longest_path}")
    
    # vertices, edges = map(int, input().split())
    # graph = dict()
    # for i in range(edges):
    #     u, v, w = input().split()
    #     w = int(w)

    #     # add edge to graph, initializing if necessary
    #     if u not in graph:
    #         graph[u] = []
    #     graph[u].append((v, w))

    #     if v not in graph:
    #         graph[v] = []
    #     graph[v].append((u, w))
        
def find_longest_path(graph, start, visited, path_length):
    if visited is None:
        visited = set()
        
    visited.add(start)
    longest_path = path_length
    longest_path_sequence = [start]
    
    for neighbor, weight in graph[start]:
        if neighbor not in visited:
            new_length, new_path = find_longest_path(graph, neighbor, visited.copy(), path_length + weight)
            if new_length > longest_path:
                longest_path = new_length
                longest_path_sequence = [start] + new_path
        print(longest_path, longest_path_sequence)        
    return longest_path, longest_path_sequence

# Return an adjacency list of nodes length with e edges between them
def create_graph(n, min_w, max_w):

    if n <= 1:
        return {0: []} if n == 1 else {}

    adjacency_list = {i: [] for i in range(n)}
    vertices = list(range(n))
    
    random.shuffle(vertices)

    # This makes a spanning tree so every node is connected by at least one edge
    # I think thats called a connected graph
    # I didn't want to deal with the case in which theres a graph where theres like 2 separate sections of nodes that are connected
    for i in range(n - 1):
        v1 = vertices[i]
        v2 = vertices[i + 1]
        weight = random.randint(min_w, max_w)
        adjacency_list[v1].append((v2, weight))
        adjacency_list[v2].append((v1, weight))


    additional_edges = random.randint(0, (n * (n - 1)) // 13) #7 is just an weird number to mod so it allows for more edges without a shit ton

    for _ in range(additional_edges):
        v1, v2 = random.sample(range(n), 2)
        if v2 not in adjacency_list[v1]:
            weight = random.randint(min_w, max_w)
            adjacency_list[v1].append((v2, weight))
            adjacency_list[v2].append((v1, weight))

    return adjacency_list

if __name__ == "__main__":
    main()