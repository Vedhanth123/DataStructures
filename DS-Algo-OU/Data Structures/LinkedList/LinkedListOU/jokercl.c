
#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *link;
} *head = NULL, *tail = NULL;

struct node *getnode()
{
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    return temp;
}

void insrt(int x)
{
    struct node *t = getnode(),
                *temp = getnode();
    t->data = x;
    t->link = head;
    if (head == NULL)
    {
        head = temp = t;
        tail = head;
    }
    else
    {
        t->link = head;
        head = t;
    }
    temp->link = head;
}
void ine(int y)
{
    struct node *t = getnode();
    t->data = y;
    t->link = head;
    tail = t;

    if (head == NULL)
    {
        head = t;
    }
    else
    {
        struct node *temp = head;
        while (temp->link != head)
        {
            temp = temp->link;
        }
        temp->link = t;
        t->link = head;
    }
    t->link = head;
}

void inb(int z, int a)
{
    struct node *t = getnode();
    t->data = z;

    if (head == NULL)
    {
        t->link = NULL;
        head = t;
    }
    else
    {
        struct node *temp = head;
        while (temp->data != a)
        {
            temp = temp->link;
        }
        t->link = temp->link;
        temp->link = t;
    }
}


void display()
{
    if (head == NULL)
    {
        printf("List is empty\n");
    }
    else
    {
        struct node *temp = head;
        printf("\nList elements are: ");
        while (temp->link != tail)
        {
            printf("%d\t", temp->data);
            temp = temp->link;
        }
        printf("%d\t", temp->data);
    }
    printf("%d\t", tail->data);
}

int main()
{
    insrt(10);
    ine(20);
    ine(30);
    ine(40);
    display();
    dele();
    display();
    insrt(50);
    delsp(50);
    display();
}
