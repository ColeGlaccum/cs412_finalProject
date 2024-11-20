"""
    This is an approximate solution to the longest path problem.

    Author: Logan Johnson
"""


def approx_longest_path(graph, start):
    visited = set()
    queue = [start]
    path_weight = 0
    path = []

    # greedily visit vertices connected by the largest weight
    while queue:
        u = queue.pop(0)
        if u in visited:
            continue
        visited.add(u)
        path.append(u)

        # find the vertex with the largest weight to visit next, ignoring the other choices
        greedy_node, greedy_weight = None, 0
        for v, weight in graph[u]:
            if v in visited:
                continue
            if weight > greedy_weight:
                greedy_node, greedy_weight = v, weight

        path_weight += greedy_weight

        if greedy_node is not None:
            queue.append(greedy_node)

    return path_weight, path


def find_start_vertex(graph):
    """
        Finds the vertex with the largest edge weight.
        In case of a tie, the vertex with the smallest total weight is chosen in order to
        leave other potentially high weight vertices available.
    """
    max_total_weight = 0
    max_edge_weight = 0
    start_vertex = None

    for vertex in graph:
        current_total_weight = 0
        current_max_edge_weight = 0

        for _, weight in graph[vertex]:
            if weight > current_max_edge_weight:
                current_max_edge_weight = weight
            current_total_weight += weight

        if current_max_edge_weight == max_edge_weight:
            if current_total_weight < max_total_weight:
                max_total_weight = current_total_weight
                start_vertex = vertex
        elif current_max_edge_weight > max_edge_weight:
            max_edge_weight = current_max_edge_weight
            max_total_weight = current_total_weight
            start_vertex = vertex

    return start_vertex


def validate_solution(graph, solution):
    path_weight, path = solution
    current_weight = 0
    previous_vertex = None
    for vertex in path:
        if vertex not in graph:
            return False
        current_weight += graph[vertex][1]
        if previous_vertex is not None:
            if graph[previous_vertex][0] != vertex:
                return False
        previous_vertex = vertex
    return current_weight == path_weight


def main():
    # build input graph from input
    vertices, edges = map(int, input().split())
    graph = dict()
    for i in range(edges):
        u, v, w = input().split()
        w = int(w)

        # add edge to graph, initializing if necessary
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

        if v not in graph:
            graph[v] = []
        graph[v].append((u, w))

    # run algorithm
    start = find_start_vertex(graph)
    if start is None:
        result = (0, [])
    else:
        result = approx_longest_path(graph, start)
    valid = validate_solution(graph, result)
    if valid:
        print(f"{result[0]}")
        print(" ".join(result[1]))
    else:
        print("Invalid solution")


if __name__ == '__main__':
    main()
