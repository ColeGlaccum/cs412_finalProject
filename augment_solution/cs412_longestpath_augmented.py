"""
This implementation demonstrates why the Bellman-Ford algorithm fails to solve the Longest Path problem
by negating edge weights. Specifically, it fails in graphs with cycles.

Author: Cole Glaccum
"""

def bellman_ford(graph, src):
    # Init
    vertices = list(graph.keys())
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((u, v, w))
    dist = {v: float('inf') for v in range(vertices)}
    dist[src] = 0

    # Relax all edges |V| - 1 times
    for _ in range(vertices - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Check for negative-weight cycles
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            print("FAILED: Graph contains a negative-weight cycle")
            return None

    return dist

def main():
    # Take graph input from the user
    vertices, edges = map(int, input().split())
    
    graph = dict()
    edge_list = []

    for _ in range(edges):
        u, v, w = input().split()
        w = int(w)

        # add edge to graph, initializing if necessary
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

        if v not in graph:
            graph[v] = []
        graph[v].append((u, w))

    # Negate edge weights
    negated_edges = [(u, v, -weight) for u, v, weight in edge_list]

    # Run Bellman-Ford on the negated graph
    result = bellman_ford(graph, 0)

    if result is not None:
        print("Longest path distances in the original graph:", result)
    else:
        print("The algorithm failed due to negative-weight cycles.")

if __name__ == "__main__":
    main()
