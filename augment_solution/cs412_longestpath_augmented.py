"""
This implementation demonstrates why the Bellman-Ford algorithm fails to solve the Longest Path problem
by negating edge weights. Specifically, it fails in graphs with cycles.

Author: Cole Glaccum
"""

def bellman_ford(vertices, edges, src):
    # Init
    dist = [float('inf')] * vertices
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
    # Init graph
    vertices = 4
    edges = [
        (0, 1, 1),
        (1, 2, 2),
        (2, 3, 3),
        (1, 3, 4),
        (3, 1, -6)   # Showing cycle
    ]

    # Negate edge weight
    negated_edges = [(u, v, -weight) for u, v, weight in edges]

    # Run Bellman-Ford on the graph
    result = bellman_ford(vertices, negated_edges, 0)

    if result is not None:
        print("Distances in the negated graph:", result)
    else:
        print("The algorithm failed due to negative-weight cycles.")

if __name__ == "__main__":
    main()