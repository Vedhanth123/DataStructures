#include <stdio.h>

struct Dnode
{
    int data;
    struct Dnode *left;
    struct Dnode *right;
};

struct Dnode *head = NULL, *tail = NULL;

// function to insert nodes into the list
void insert_at_end(int data)
{
    // create memory
    struct Dnode *newnode = (struct Dnode*) malloc(sizeof(struct Dnode));

    // inserting data into the node;
    newnode->left = tail;
    newnode->right = NULL;
    newnode->data = data;

    if(head == NULL)
    {
        head = newnode;
    }
    else
    {
        tail->right = newnode;
    }

    // updating the tail to the newnode
    tail = newnode;
}

// function to insert at start
void insert_at_start(int data)
{
    // create a newnode
    struct Dnode *newnode = (struct Dnode*) malloc(sizeof(struct Dnode));

    // inserting data into the newnode
    newnode->data = data;

    if(head == NULL)
    {
        head = newnode;
    }
    else
    {
        newnode->right = head;
        head->left = newnode;

    }
    newnode->left = NULL;
}

// function to insert nodes in between / randomly
void insert_random(int data, int index)
{
    int c = 0;
    struct Dnode *t = head;
    struct Dnode *newnode = (struct Dnode*) malloc(sizeof(struct Dnode));

    // inserting data into the node
    newnode->data = data;
    while(t != NULL && c != index)
    {
        t = t->right;
        c ++;
    }
    t->right->left = newnode;
    newnode->right = t->right;
    newnode->left = t;
    t->right = newnode;
}

// function to delete the node from end
void delete_from_end()
{
    tail = tail->left;
    struct Dnode *temp = tail;
    free(temp->right);
}

void delete_from_start()
{
    struct Dnode *temp = head;
    head = head->right;
    head->left = NULL;
    free(temp);
}

void randome_delete(int index)
{
    struct Dnode *t = head;
    int c= 0;
    struct Dnode *l = t->right->right;
    while(t != NULL && c != index && l != NULL)
    {
        t = t->right;
        l = l->right;
        c ++;
    }
    l->left->left = t;
    free(t->right);
    t->right = l;
}

// search
void search(int key)
{
    struct Dnode *temp = head;
    while(temp != NULL)
    {
        if(temp->data == key)
        {
            printf("Found ");
            break;
        }
        temp = temp->right;
    }
}

void traverse()
{
    struct Dnode *temp = head;
    while(temp != NULL)
    {
        printf("%d",temp->data);
        temp = temp->right;
        
    }
}
int main()
{
    return 0;
}