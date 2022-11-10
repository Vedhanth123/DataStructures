#include <stdio.h>
#include <stdlib.h>

struct node
{
    int val;
    struct node *ptr;
} node;

int pos;
struct node *head = NULL;
struct node *old = NULL;

void append(int x)
{
    struct node *new = (struct node *)malloc(sizeof(struct node));

    new->val = x;
    new->ptr = NULL;
    if (head == NULL)
    {
        head = new;
        old = head;
    }
    else
    {
        old->ptr = new;
    }
    old = new;
}

void random_delete()
{
    struct node *joker, *del;
    int c = 0;
    joker = head;
    del = head->ptr;
    printf("Enter position for deleteion\n");
    scanf("%d", &pos);
    while (del != NULL)
    {
        c = c + 1;
        if (c == pos)
        {
            joker->ptr = del->ptr;
            free(del);
        }
        del = del->ptr;
    }
}
void random_insert(int x, int pos)
{
    if (pos == 1)
    {
        struct node *new = (struct node *)malloc(sizeof(struct node));
        new->val = x;
        head = new;
    }
    else
    {
        struct node *ved = head;
        int c = 1;
        while (ved != NULL)
        {
            if (c == pos - 1)
            {
                struct node *ins = (struct node *)malloc(sizeof(struct node));
                ins->val = x;
                ins->ptr = ved->ptr;
                ved->ptr = ins;
            }
            c = c + 1;
            ved = ved->ptr;
        }
    }
}
void display()
{
    struct node *trav;
    trav = head;
    while (trav != NULL)
    {
        printf("%d", trav->val);
        trav = trav->ptr;
    }
}

void main()
{
    int i;
    printf("Starting append:\n");
    for (i = 1; i <= 5; i++)
    {
        printf("%d\n", i);
        append(i);
    }
    printf("append completed");
    display();
    random_insert(10, 3);
    display();
}