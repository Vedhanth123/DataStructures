// C++ program to implement queue using array
#include <stdio.h>

int ar[5];
int n = 5;
int front = - 1;
int rear = - 1;

void enqueue(int item) {
    if (rear == n - 1){
        printf("\nOverflow\n");
    }
    else {
        if (front == - 1 && rear==-1){
            front = 0;
            rear=0;
        }
        else{
            rear++;
        }
        ar[rear] = item;
    }
}
void dequeue() {

    if (front == - 1 || front > rear) {
        printf("\nUnderflow\n");
    }
    else {
        printf("%d Element deleted: ",ar[front]);
        if(front == rear)  {  
            front = -1;  
            rear = -1;  
        }
        else{
            front++;
        }
   }
}

// Stack using Linked List -------------------------------------------------------
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

//driver code
int main() {
    for(int i = 1; i <= 7; i++)
    {
        enqueue(i*10);
    }
    for(int i = 1; i <= 7; i++)
    {
        dequeue();
    }

}