# include <stdio.h>

void main()
{
    char *p[3] = {"cricket","football","basketball"};

    int i;

    for (i = 0; i < 5; i++)
    {
        printf("%s,  %s\n",*(p+i));
    }   
}
