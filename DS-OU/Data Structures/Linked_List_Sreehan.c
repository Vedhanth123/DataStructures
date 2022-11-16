#include <stdio.h>

// to create a linked list we need to have a struct
struct Gang
{
    int drug;
    struct Gang *pointer;
};

// we use pointers to create new member of the gang will be added with the help of create_Gang
struct Gang *create_Gang;

// we again need a pointer to hold the gang leader
struct Gang *rolex = NULL;

// we again need to create a variable which helps us to connect different gang members
struct Gang *broker = NULL;

// we create a new gang member and add data to the gang member
// we use malloc to achieve this task
void insert(int data) 
{
    // we are appointing new gang member
    create_Gang = (struct Gang *)malloc(sizeof(struct Gang));

    // we then add data to the gang member
    create_Gang->drug = data;

    if (rolex == NULL)
    {
        rolex = create_Gang;
    }
    else
    {
        broker->pointer = create_Gang;
    }
    broker = create_Gang;
}

void main()
{
    insert(10);
    insert(20);
    insert(30);
}
