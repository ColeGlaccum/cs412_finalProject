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

import time
import os
import cs412_longestpath_exact

def main():
    #print_graph_input(10)
    
    # count = 0

    # while count < 1000:
    #     count += 1
    #     try:
    #         directory_name = "test_cases/test" + str(count)
    #         os.mkdir(directory_name)
    #         print(f"Directory '{directory_name}' created successfully.")
    #     except FileExistsError:
    #         print(f"Directory '{directory_name}' already exists.")
    
    # count = 0
    
    # n = 3
    # while count < 999:
    #     count += 1
    #     path = "test_cases/test" + str(count)
    #     if count % 58 == 0:
    #         n += 1
    #     print_graph_input(n, path)
        
    # count += 1
    count = 1000
    path = "test_cases/test" + str(count)
    
    start = time.time()
    print(start)
    print_graph_input(30, path, 33)
    end = time.time()
    
    millis = (end-start) * 10**3
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24

    print ("%d hours %d minutes %d seconds %f milliseconds" % (hours, minutes, seconds, millis))
       
def print_graph_input(n, path, additional = None):
    #Random prime numbers to mod by when deciding how many additional edges to have
    prime_numbers = [17, 19, 23, 29, 31, 37, 41]
    prime = random.randint(0, len(prime_numbers) - 1)
    prime = prime_numbers[prime]
    
    graph, edges = create_graph(n, prime, additional) # 11 is just a fun prime number so there can be a lot of edges
    
    visited = set()
    
    input_path = path + "/testInput.txt"
    
    f = open(path + "/testOutput.txt",  "w")
    f.write("")
    f.close()
    
    f = open(input_path, "w")
    f.write(str(len(graph.keys())) + " " + str(edges) + "\n")
    
    print(len(graph.keys()), edges)
    for node in graph.items():
        for v, w in node[1]:
            if (node[0], v) not in visited and (v, node[0]) not in visited:
                f.write(f"{node[0]} {v} {w}\n")
                print(node[0], v, w)
            
            visited.add((node[0], v))
            visited.add((v, node[0]))

    print("---------")
    f.close()
    longest_path_length, longest_path = cs412_longestpath_exact.find_longest_path(graph)
    
    expected_path = path + "/testExpected.txt"
    f = open(expected_path, "w")
    f.write(f"{longest_path_length}\n")
    f.write(f"{" ".join(str(x) for x in longest_path)}")
    
    print(longest_path_length)
    print(" ".join(str(x) for x in longest_path))       
    f.close()
 
# Return an adjacency list of nodes length with e edges between them
def create_graph(n, prime_num, additional = None):
    edge_count = 0
    
    if n <= 1:
        return {0: []} if n == 1 else {}

    adjacency_list = {i: [] for i in range(n)}
    vertices = list(range(n))
    
    random.shuffle(vertices)

    # This makes a spanning tree so every node is connected by at least one edge
    # I think thats called a connected graph
    for i in range(n - 1):
        v1 = vertices[i]
        v2 = vertices[i + 1]
        weight = random.randint(n, n*n)
        adjacency_list[v1].append((v2, weight))
        adjacency_list[v2].append((v1, weight))
        edge_count += 1

    if additional is None:
        additional_edges = random.randint(0, (n * (n - 1)) % prime_num) #prime_num is just an weird number to mod so it allows for more edges without a shit ton
    else:
        additional_edges = additional
    
    for _ in range(additional_edges):
        v1, v2 = random.sample(range(n), 2)
        if v2 not in [v for v, _ in adjacency_list[v1]]:
            weight = random.randint(n, n*n)
            adjacency_list[v1].append((v2, weight))
            adjacency_list[v2].append((v1, weight))
            edge_count += 1

    return adjacency_list, edge_count

if __name__ == "__main__":
    main()