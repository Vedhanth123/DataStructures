// program to implement self referential structures

# include <stdio.h>

struct player
{
    int age;
    struct player *structure_pointer;
}p1,p2;

void main()
{

    // inserting values into two structures
    p1.age = 10;
    p2.age = 20;

    p1.structure_pointer = &p2;
    
    printf("%d\n",p1.age);
    
    printf("%d\n",p1.structure_pointer->age);
}
