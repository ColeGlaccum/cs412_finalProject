Hello World

For brute force try everything with itertools then run it through a checker method that checks the possible solution in polynomial time, then ends the program when it verifies that a solution is valid
Also make sure to use adjacency lists

Let's do an undirected graph with finding the longest path from a vertice S, random weights, for testing we should show how changing the number of edges affects the longest path as well as runtime.

For exact solution make a backtracking recursive algorithm that starts at the Vertice S and loops through the adjacency list for all connected vertices by an edge, store the longest path then go through rest of the solutions.