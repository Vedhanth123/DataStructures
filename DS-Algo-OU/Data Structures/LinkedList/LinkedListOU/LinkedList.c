#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *link;
};

typedef struct node node;
struct node *first = NULL, *last, *n1;
void insertend(int data)
{

    n1 = (struct node *)malloc(sizeof(struct node));

    n1->data = data;

    n1->link = NULL;

    if (first == NULL)
    {
        first = n1;
    }
    else
    {
        last->link = n1;
    }
    last = n1;
}
void randominsert(int data, int index)
{
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = data;

    int i = 0;
    struct node *traverser = first;

    while (i < index - 1 && traverser != NULL)
    {
        traverser = traverser->link;
        i++;
    }

    temp->link = traverser->link;
    traverser->link = temp;
}

void insertfront(int data)
{

    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = data;
    if (first == NULL)
    {
        first = temp;
        temp->link = NULL;
    }
    else
    {

        temp->link = first;
        first = temp;
    }
}

void randomdelete(int index)
{
    struct node *traverser = first, *temp;
    int i = 0;

    while (i < index - 1 && traverser != NULL)
    {
        traverser = traverser->link;
        i++;
    }

    temp = traverser->link;
    traverser->link = temp->link;
    free(temp);
}

void traverse()
{
    struct node *temp;

    temp = first;
    printf("------------------------------------------------- \n");
    while (temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->link;
    }
    printf("\n");
}

void deletestart()
{
    struct node *t = first, *temp = first;
    if (first == NULL)
    {
        printf("List is empty:");
    }
    else
    {
        first = first->link;
        free(temp);
    }
}
void deleteend()
{
    struct node *t = last, *temp = first;
    if (first == NULL)
        printf("list is empty");
    else
    {
        while (temp->link != NULL)
        {
            temp = temp->link;
        }
        last = temp;
        if (temp == first)
        {
            first = NULL;
            free(temp);
        }
    }
}

void main()
{

    int i;

    insertend(10);
    traverse();
    insertfront(200);
    traverse();
    randominsert(150, 1);
    traverse();
    randomdelete(1);
    traverse();
    deletestart();
    traverse();
    deleteend();
    traverse();
}