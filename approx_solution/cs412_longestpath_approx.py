"""
    This is an approximate solution to the longest path problem.

    Author: Logan Johnson
"""


import time
import random


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


def validate_solution(graph, solution):
    path_weight, path = solution
    current_weight = 0
    for count, vertex in enumerate(path):
        if count == len(path) - 1:
            break
        if vertex not in graph:
            return False
        for edge in graph[vertex]:
            if count + 1 >= len(path):
                return False
            if edge[0] == path[count + 1]:
                current_weight += edge[1]
                break
        else:
            return False
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
    t_end = time.time() + 60 * 1
    solution = (0, [])
    while time.time() < t_end:
        start = random.choice(list(graph.keys()))
        if start is None:
            result = (0, [])
        else:
            result = approx_longest_path(graph, start)
            valid = validate_solution(graph, result)
            if not valid:
                continue
        if result[0] > solution[0]:
            solution = result

    print(f"{solution[0]}")
    print(" ".join(solution[1]))


if __name__ == '__main__':
    main()
