
"""
Augment to show why the Bellman-Ford algorithm fails to solve the Longest Path problem
by negating edge weights.
Author: Cole Glaccum
"""

def bellman_ford(vertices, edges, src):
    # Init
    dist = [float('inf')] * vertices
    dist[src] = 0

    # Relax all edges V - 1 times
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
    n, m = map(int, input().split())
    vertices = {}
    edge_list = []

    # Read edges
    for i in range(m):
        u, v, w = input().split()
        w = int(w)
        
        # Map vertex labels to indices
        if u not in vertices:
            vertices[u] = len(vertices)
        if v not in vertices:
            vertices[v] = len(vertices)

        u_idx = vertices[u]
        v_idx = vertices[v]

        # Add both directions bc its undirected
        edge_list.append((u_idx, v_idx, w))
        edge_list.append((v_idx, u_idx, w))

    # Negate edge weights
    negated_edges = [(u, v, -weight) for u, v, weight in edge_list]

    # Run on the negated graph
    result = bellman_ford(len(vertices), negated_edges, 0) # Start at 0, ig

    if result is not None:
        print("Distances in the negated graph:", result)

if __name__ == "__main__":
    main()