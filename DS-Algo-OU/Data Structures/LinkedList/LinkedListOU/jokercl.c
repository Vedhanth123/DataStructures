
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

void delst()
{
    struct node *t = head, *temp = head;
    if (head == NULL)
        printf("List is empty");
    else
    {
        if (t->link == head)
        {
            head = NULL;
            free(t);
        }
        else
        {
            head = t->link;
            head = temp->link;
            t->link = head;
            free(temp);
        }
        t = head;
        tail->link = head;
    }
}
void dele()
{
    struct node *t = tail, *temp = head;
    if (head == NULL)
        printf("list is empty");
    else
    {
        while (temp->link != t)
        {
            temp = temp->link;
        }
        temp->link = head;
        tail = temp;
        free(t);
        t = tail;
    }
}
void delsp(int z)
{
    struct node *t = head;
    struct node *temp = NULL;
    if (head == NULL)
        printf("List is empty");
    else
    {
        if (t->link == head && t->data != z)
            printf("node not found");
        else
        {
            if (t->link == head && t->data == z)
            {
                free(t);
                head = NULL;
            }
            else
            {
                while (t->link != head)
                {
                    if (t->data == z)
                    {
                        temp = t;
                    }
                }
            }
        }
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
