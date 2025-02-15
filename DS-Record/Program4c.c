#include <stdio.h>
#include <stdlib.h>

// Structure to create a node with data and the next pointer
struct Node {
    int data;
    struct Node *next;
};
struct Node* top = NULL;

// Push() operation on a  stack
void push(int value) {
    struct Node *newNode;
    newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->data = value; // assign value to the node
    if (top == NULL) {
        newNode->next = NULL;
    } else {
        newNode->next = top; // Make the node as top
    }
    top = newNode; // top always points to the newly created node
    printf("Node is Inserted\n\n");
}

int pop() {
    if (top == NULL) {
        printf("\nStack Underflow\n");
    } else {
        struct Node *temp = top;
        int temp_data = top->data;
        top = top->next;
        free(temp);
        return temp_data;
    }
}




int main() {

    for(int i = 1; i<= 5; i++)
    {
        push(i*10);
    }
    for(int i = 1; i<= 7; i++)
    {
        printf("%d Element deleted\n",pop());;
    }
}
