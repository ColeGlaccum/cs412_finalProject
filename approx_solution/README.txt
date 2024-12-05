The Longest Path Approximation Solution
=======================================

To run the approximation solution, run the following command:

    python cs412_longsetpath_approx.py

This will prompt you to enter a graph in the following format:

    <number of vertices> <number of edges>
    <vertex 1> <vertex 2> <weight>
    ...
    <vertex n> <vertex n+1> <weight>

For example, the following graph has 4 vertices and 3 edges:

    4 3
    a b 1
    a c 2
    b c 2
    b d 4
    c d 3

Alternatively, you can provide the graph as a file. The file should
contain the graph in the same format as above.

The approximation solution will output the length of the longest path
and the sequence of vertices in the path.

Example output:

    5
    a b c d
