# include <stdio.h>

struct practoce
{
    int jock;
    char switcher;

};

void main()
{
    struct practoce si;
    struct practoce *p;

    p = &si;

    // reading values to a structure using special structure pointer method
    scanf("%d",&p->jock);

    // accessing values of a structure using special structure pointer method
    printf("%d",p->jock);

    // reading values to a structure using pointer method
    scanf("%c",&(*p).switcher);

    // accessing values of a structure using pointer method
    printf("%c",(*p).switcher);
}