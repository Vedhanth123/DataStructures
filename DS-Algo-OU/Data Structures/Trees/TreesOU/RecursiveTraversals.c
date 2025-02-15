#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *right_child;
    struct node *left_child;
} *root,*t;

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

void pre_order(struct node *root)
{
    if(root)
    {
        printf("\t%d",root->data);
        pre_order(root->left_child);
        pre_order(root->right_child);
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

}