from collections import deque
"""
Question 5. 1 (70/100)
An Euler walk is a traversal of a graph, where each edge is traversed exactly once. Nodes may be visited
multiple times. Given a non-directed, unweighted graph (G), your task is to output:
i. Whether a Euler Walk exists for the given graph.
ii. If a Euler Walk exists, print the nodes in the visited order.
The graph G will be presented to you in the form of an adjacency list.
i.e.
[[1, 2],
[0],
[0]]
Would describe a Graph with 3 nodes and 2 edges. Where nodes are 0, 1, and 2. Edges are 0-1 and 0-2.
Two Euler walks exist for this graph: 1-0-2, and 2-0-1.
Your output should be returned from a function as a tuple. Where the first element of the tuple
indicates if a Euler walk exists or not as True or False and the second element gives the nodes in visited
order as a list or None (if no Euler walk exist).
(True, [1, 0, 2]) or (True, [2, 0, 1]) would be valid outputs for the above test case.
Your program should have a callable function with the name “euler_walk()”. That takes an
adjacency list (a 2D python list) as the sole input parameter, and a tuple as described above, as the
return value.
Example 1
Calling the function: euler_walk([[1, 2], [0], [0]])
Function output: (True, [1, 0, 2])
Example 2
Calling the function: euler_walk([[1, 2, 3], [0], [0], [0]])
Function output: (False, None)
"""

def euler_walk
    return

"""
Question 5. 2 (30/100)
Answer the following questions based on your solution for Question 5.1.
1. Explain the algorithm you used to decide whether there is a Euler walk or not for the given
graph? Include a graphical explanation. (150- 200 words)
(10 points)
2. Explain the algorithm you used to find the Euler walk, in the case where a valid Euler Walk
existed. Include a graphical explanation. (150-200 words)
(20 points)

"""