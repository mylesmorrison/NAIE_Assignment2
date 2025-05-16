import copy
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

def check_exists(adj_list):
    # The conditions for an euler path to exist in an undirected graph is that the graph is connected
    # it is also that number of odd degrees from a node is 0 or 2.
    number_of_odd_degrees = 0
    for i in range(len(adj_list)):
        if (len(adj_list[i]) % 2) != 0:
            number_of_odd_degrees+=1
    #print(number_of_odd_degrees)
    if is_connected(adj_list) and ((number_of_odd_degrees == 0) or (number_of_odd_degrees == 2)):
        return True
    else:
        return False


def is_connected(adj_list):
    n = len(adj_list)
    visited = [False] * n
    start_node = None
    # find a node with at least 1 edge to it
    for i in range(n):
        if len(adj_list[i]) > 0:
            start_node = i
            break

    #if there are no edges then technically is true
    if start_node is None:
        return True

    # Step 3: Run DFS from start_node
    dfs(start_node, visited, adj_list)

    # Step 4: Check that all nodes with edges were visited
    for i in range(n):
        if len(adj_list[i]) > 0 and not visited[i]:
            return False  # This node is disconnected
    return True


def dfs(node, visited, adj_list):
    visited[node] = True
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, adj_list)


def euler_walk(adj_list):
    if check_exists(adj_list) == False:
        return (False, None)
    #Hierholzer Algorithm


    # making a copy of the list
    adj_list_copy = copy.deepcopy(adj_list)

    # choose starting node
    degrees = [len(neighbor) for neighbor in adj_list]
    odd_degrees = []
    for i in range(len(adj_list)):
        if len(adj_list[i]) % 2 == 1:
            odd_degrees.append(i)
    if len(odd_degrees) > 0:
        start = odd_degrees[0]
    else:
        for i in range(len(adj_list)):
            if len(adj_list[i]) > 0:
                start = i
    #print(start)
    path = []
    stack = [start]

    while stack:
        node = stack[-1]
        if adj_list_copy[node]:
            neighbor = adj_list_copy[node].pop()
            adj_list_copy[neighbor].remove(node)
            stack.append(neighbor)
        else:
            path.append(stack.pop())

    return (True, path[::-1])


print(euler_walk([[1, 2], [0], [0]]))
print(euler_walk([[1, 2, 3], [0], [0], [0]]))

'''
    I think I was thinking of how it would work if graph is directed but instead will try for an undirected graph
    node_out_list = []
    node_in_list = [0] * len(adj_list)
    for i in range(len(adj_list)):
        node_out_list.append(len(adj_list[i]))
        for j in range(len(adj_list[i])):
            going_into = adj_list[i][j]
            node_in_list[going_into] += 1

    print(node_out_list)
    print(node_in_list)
    '''

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

"""
5.2 (1.)
"""

# The algorithm I used to decide whether there is an Euler Walk from the list was to check two conditions. The first
# was that the graph is connected. If nodes are disconnected but have no edges this was fine and technically meant it
# passed the test cases but has no actual path as there are no edges. The second condition is to check that the graph
# has either 0 odd number of degrees or 2.

# I first checked that the algorithm had an odd number of degrees. This is simply done by looping through the adjacency
# list and then for every array I would check if it is odd or not and increment the odd degree counter or pass
# through the loop. The next part of the algorithm requires using depth first search to check if it is connected or not.

# The is_connected() function part of my algorithm works by first finding a start node that has degree of more than 0
# and then traverse through the graph and at each vertex checks that if a node with edges but is not in visited then it
# must be disconnected and vice versa it will return as True. These two test cases give us the necessary information to
# determine whether a graph is an euler walk or not.

"""
5.2 (2.)
"""

# To find the traversal of the euler walk after we have confirmed that one exists in the graph is to first find the
# starting node. This consists of find the odd degrees and starting at either one as the starting node. The other method
# if there are no odd degrees is to start from the first node where the number of edges is greater than 0.

# After this I created a stack that would keep track of the nodes visited and a path array to keep order of nodes
# visited. Look at the current node on top of the stack. Then check if there are any unused neighbours take a neighbour
# add it to the stack and then remove that neighbour from the graph. Because it is undirected you must also remove the
# opposite edge from the graph. Then move to the neighbour by pushing it onto the stack. If there are no unused
# neighbours then backtrack using the stack and pop the last used neighbour. After you put the path in reverse to get
# correct order.