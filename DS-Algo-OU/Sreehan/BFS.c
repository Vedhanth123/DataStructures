#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 1) Take input of the no. of nodes a graph has
// 2) Take input of all the edges the graph has
// 3) represent the graph in adjacency matrix
// 4) Create a stack to push all the non visited nodes to the stack and then push and pop accordingly

int *AdjacencyMatrix(int no_of_nodes)
{
    int *matrix = (int *)calloc((no_of_nodes * no_of_nodes), sizeof(int));
    return matrix;
}
void main()
{
    // 1) Take input of the no. of nodes a graph has
    int no_of_nodes;
    printf("Enter the no. of nodes a graph has:\n");
    scanf("%d", &no_of_nodes);
    int *matrix = AdjacencyMatrix(no_of_nodes);

    // 2) Take input of all the edges the graph has
    char edges[10];
    int stopper = 0;
    while (1)
    {
        printf("Enter edges for the graph: ");
        gets(edges);

        char *token = strtok(edges, ' ');
        puts(token);

        printf("Press 1 to stop, Press 0 to contine: ");
        scanf("%d", &stopper);
        if (stopper == 1)
            break;
    }
}