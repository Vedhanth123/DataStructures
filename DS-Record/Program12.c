#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *right_child;
    struct node *left_child;
} *root,*t;

struct node *Stack[100]; 
int top = -1; 

void push(struct node *t)
{
    if (top == 100 - 1)
    {
        printf("\nOverflow!!");
    }
    else
    {
        top = top + 1;
        Stack[top] = t;
    }
}

struct node *pop()
{
    if (top == -1)
    {
        return NULL;
    }
    else
    {
        top = top - 1;
        return Stack[top+1];
    }
}

struct node *getnode(int data)
{
    t=(struct node *)malloc(sizeof(struct node));
    t->data=data;
    t->right_child=NULL;
    t->left_child=NULL;
    return t;
}


void in_order(struct node *root)
{
    if(root)
    {
        in_order(root->left_child);
        printf("\t%d",root->data);
        in_order(root->right_child);
    }
}

void inOrderTraversal(struct node *root)
{
	struct node *currentNode = root;

	while (currentNode != NULL || pop() == NULL)
	{
        //condition to check if the node is leftmost node 
		while (currentNode != NULL)
		{
			// step 3 of our algorithm
			push(currentNode);
			currentNode = currentNode->left_child;
		}
		
		currentNode = pop();
        // cout statement to print the node data
		printf("\t%d",currentNode->data);
        
        // statement to process right subtree 
		currentNode = currentNode->right_child;
	} 
}

void pre_order(struct node *root)
{
    if(root)
    {
        printf("\t%d",root->data);
        pre_order(root->left_child);
        pre_order(root->right_child);
    }
}
void preOrderTraversal(struct node *root)
{
	struct node *currentNode = root;
	while (currentNode != NULL || pop() == NULL)
	{
		printf("\t%d",currentNode->data);
		while (currentNode != NULL)
		{
			push(currentNode);
			currentNode = currentNode->left_child;
		}
		currentNode = pop();
		currentNode = currentNode->right_child;
	} 
}


void post_order(struct node *root)
{
    if(root)
    {
        post_order(root->left_child);
        post_order(root->right_child);
        printf("\t%d",root->data);
    }
}
void postOrderTraversal(struct node *root)
{
	struct node *currentNode = root;
	while (currentNode != NULL || pop() == NULL)
	{
		while (currentNode != NULL)
		{
			push(currentNode);
			currentNode = currentNode->left_child;
		}
		currentNode = pop();
		currentNode = currentNode->right_child;
		printf("\t%d",currentNode->data);
	} 
}


void main()
{
    root=getnode(100);
    root->right_child=getnode(200);
    root->right_child->left_child=getnode(400);
    root->left_child=getnode(300);
    root->left_child->right_child=getnode(500);

    printf("\nIn order\n");
    in_order(root);
    printf("\nPre order\n");
    pre_order(root);
    printf("\nPost order\n");
    post_order(root);
    printf("\nIn order\n");
    in_order(root);
    printf("\nPre order\n");
    pre_order(root);
    printf("\nPost order\n");
    post_order(root);

}