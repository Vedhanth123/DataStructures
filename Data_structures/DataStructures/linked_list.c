// implementation of linked list

#include <stdio.h>

void main()
{
    // create backbone of linked list
    struct linked_list
    {
        int variable;
        struct linked_list *pointer;
    };

    // declaring linked list
    struct linked_list l1, l2, l3, l4, traversel;

    l1.variable = 10;
    l1.pointer = &l2;

    l2.variable = 20;
    l2.pointer = &l3;

    l3.variable = 30;
    l3.pointer = &l4;

    l4.variable = 40;
    l4.pointer = NULL;

    // traversing linked list

    traversel.pointer = &l1;

    for (int i = 0; i < 4; i++)
    {
        printf("%d\n", traversel.pointer->variable);
        traversel.pointer = traversel.pointer->pointer;
    }
}
