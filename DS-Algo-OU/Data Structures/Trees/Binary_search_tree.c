// #include <stdio.h>

// // 1) Start at the node

// // 2) Go to the total last left node

// // 3) check the value is less than the parent node then proceed else return

// // 4) Check for the right last node to it's parent node if the value is greater

// // than the node then proceed else return 


// struct node
// {
//     int data;  
//     struct node* left_node;
//     struct node* right_node;
// };

// int data = 1;

// struct node *tree, *root = NULL;

// // creating a binary tree
// void insert()
// {

//     // allocating memory for the node
//     tree = (struct node*) malloc(sizeof(struct node));

//     // inserting data into the node
//     tree->data = data;

//     data += 1;

//     // inserting null values into the child nodes of that tree
//     tree->left_node = NULL;
//     tree->right_node = NULL;

//     // checking if memory contains a node
//     if(root == NULL)
//     {
//         root = tree;
//     }

//     // asking user if this node contains any left node
//     char left_choice;
//     printf("Enter 'l' for creating left node:\n");
//     scanf("%c",&left_choice);

//     if(left_choice == 'l')
//     {
//         insert(data);
//     }

//     // asking user if this node contains any right node
//     char right_choice;
//     printf("Enter 'r' for creating right node:\n");
//     scanf("%c",&right_choice);

//     if(right_choice == 'r')
//     {
//         insert(data);
//     }
// }

// void main()
// {
//     insert();
// }


#include <stdio.h>
#include <stdlib.h>

// 1) Start at the node

// 2) Go to the total last left node

// 3) check the value is less than the parent node then proceed else return

// 4) Check for the right last node to it's parent node if the value is greater

// than the node then proceed else return 


struct node
{
    int data;  
    struct node* left_node;
    struct node* right_node;
};

int data = 1;

struct node *tree, *root = NULL, *current_node;


struct node* left_node_creation(int data)
{
  
          
    // allocating memory for the node
    tree = (struct node*) malloc(sizeof(struct node));

    // inserting data into the node
    tree->data = data;

    data ++;
    // inserting null values into the child nodes of that tree
    tree->left_node = NULL;
    tree->right_node = NULL;
    
    return tree;
  
}

struct node* right_node_creation(int data)
{
    // allocating memory for the node
    tree = (struct node*) malloc(sizeof(struct node));

    // inserting data into the node
    tree->data = data;

    data ++;
    // inserting null values into the child nodes of that tree
    tree->left_node = NULL;
    tree->right_node = NULL;
    
    return tree;

}

// creating a binary tree
void insert(int branches)
{

    if(branches == 0)
        return;
      
    // allocating memory for the node
    tree = (struct node*) malloc(sizeof(struct node));

    current_node = tree;

    // inserting data into the node
    tree->data = data;

    data += 1;

    // inserting null values into the child nodes of that tree
    tree->left_node = NULL;
    tree->right_node = NULL;

    // checking if memory contains a node
    if(root == NULL)
    {
        root = tree;
    }
  
    branches -= 1;
    
    current_node->left_node = left_node_creation(data);
    
    current_node->right_node = right_node_creation(data);
    // asking user if this node contains any left node
    
    /*
    char left_choice;
    printf("Enter 'l' for creating left node:\n");
    scanf("%c",&left_choice);
    
    if(left_choice == 'l')
    {
        insert(data);
    }

    // asking user if this node contains any right node
    char right_choice;
    printf("Enter 'r' for creating right node:\n");
    scanf("%c",&right_choice);

    if(right_choice == 'r')
    {
        insert(data);
    }
    
    */

}

void main()
{
    insert(3);
}








