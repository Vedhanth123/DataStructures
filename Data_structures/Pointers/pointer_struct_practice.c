# include <stdio.h>

// pointer to structure

struct student
{
    int pin;
    char name[20];
};

void main()
{
    struct student si = {1000, "SBTET"};
    struct student *p;

    p = &si;

    printf("%d",p->pin);
    printf("%s",p->name);
}