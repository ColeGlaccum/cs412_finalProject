"""
    name:  Logan Johnson

    Honor Code and Acknowledgments:

    This work complies with the JMU Honor Code.
    - I used an answer from this question to assist with
      running the program for a certain amount of time
      https://stackoverflow.com/q/24374620
  
    Comments here on your code and submission
"""


import time
import random
from collections import defaultdict


def approx_longest_path(graph, start):
    visited = set()
    stack = [start]
    path_weight = 0
    path = []

    # greedily visit vertices connected by the largest weight
    while stack:
        u = stack.pop()
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

        if greedy_node is not None:
            path_weight += greedy_weight
            stack.append(greedy_node)

    return path_weight, path


def validate_solution(graph, solution):
    path_weight, path = solution
    current_weight = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        if u not in graph:
            return False
        for neighbor, weight in graph[u]:
            if neighbor == v:
                current_weight += weight
                break
        else:
            return False

    return current_weight == path_weight


def main():
    # build graph from input
    vertices, edges = map(int, input().split())
    graph = defaultdict(list)
    for i in range(edges):
        u, v, w = input().split()
        w = int(w)
        graph[u].append((v, w))
        graph[v].append((u, w))

    # run approximate algorithm
    time_limit = time.time() + 30 # 30 second limit
    best_solution = (0, [])
    unvisited_starts = set(graph.keys())
    while time.time() < time_limit:
        # stop searching if we've visited all vertices
        if not unvisited_starts:
            break

        # choose a random unvisited vertex to start from
        start = random.choice(list(unvisited_starts))
        unvisited_starts.remove(start)

        result = approx_longest_path(graph, start)
        if validate_solution(graph, result) and result[0] > best_solution[0]:
            best_solution = result

    path_weight, path = best_solution
    if path:
        print(f"{path_weight}")
        print(" ".join(path))
    else:
        print("No valid path found.")


if __name__ == '__main__':
    main()
