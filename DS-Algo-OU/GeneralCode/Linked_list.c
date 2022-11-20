#include <stdio.h>
#include <stdlib.h>

// we shall create a sofa for MGIT
struct Sofa
{
    // person sits on sofa
    int person;

    // We also need to have contact of another sofa
    // in order to link to another sofa we use pointers in C
    struct Sofa *contact;
};

// We created CR so that we can get in touch with all other students in class
struct Sofa *CR = NULL;
struct Sofa *Admin = NULL;


// We need to make a person sit on sofa which is a task. We write that in a function
void Sit(int p)
{
    // In order to create sofa we need to have builder/carpenter. In C we have malloc
    // In malloc we actually allocate memory
    Admin = (struct Sofa*) malloc(sizeof(struct Sofa));
    Admin->person = p;
    Admin->contact = NULL;

    if(CR == NULL)
    {
        CR = Admin;
    }

}