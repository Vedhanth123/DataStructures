#include <stdio.h>

#define max 10

// increasing order
void printi(n)
{
    if(n > max)
        return;
    else
    {
        printf("%d ,",n);
        printi(n+1);
    }
}

// decreasing order
void printd(n)
{
    if(n > max)
        return ;
    else
    {
        printd(n+1);
        printf("%d ,",n);
    }
}
int main()
{
    printi(0);
    printf("\n");
    printd(0);
    return 0;
}