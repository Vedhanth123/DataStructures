#include <stdio.h>
#include <stdlib.h>

char c[] = "laptop";

void function(char *c)
{
    if(*c != '\0')
    {
        function(c+1);
        printf("%c",*c);
    }
}
int main()
{
    function(&c);
    return 0;
}