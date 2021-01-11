// program to implement self referential structures

# include <stdio.h>

void main()
{
    struct player
    {
        int age;
        struct player *structure_pointer;
    }p1,p2;

    p1.age = 10;
    p2.age = 20;

    p1.structure_pointer = &p2;
}