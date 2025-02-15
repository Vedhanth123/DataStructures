# take input of the no. of nodes a graph contains
no_of_nodes = int(input("No. of nodes: "))

# array to store all the edges
edges = []

# take input of the edges
while (True):

    # ask for user to continue entering for the edges
    choice = int(input("Do you want to continue: "))

    if (choice != 1):
        break

    # ask user to give input of edge
    edge = input("Enter edge: ")
    edges.append(edge)

# building an adjacency matrix out of the edges given as input


def buildAdjacencyMatrix(edges):

    # build an empty matrix of size n*n
    matrix = []
    for x in range(no_of_nodes):
        matrix.append([0] * no_of_nodes)

    for x in edges:
        temp = x.split('-')
        matrix[int(temp[0]) - 1][int(temp[1]) - 1] = 1

    return matrix


adjacencyMatrix = buildAdjacencyMatrix(edges)

# BFS:
# 1) Start from a node and note down all the non visited vertices into a queue
# 2) mark the choosen node as visited
# 3) now pop out a node from the queue and repeat from the step 1

def BFS_traversal(matrix):

    visited_array = [0] * no_of_nodes

    queue = []

    # 1) Start from the first row of the matrix
    for x in range(len(matrix)):

        # 2) copy all non visited vertices into a queue array
        for y in range(len(matrix[x])):
            

