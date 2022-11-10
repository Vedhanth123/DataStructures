# include <stdio.h>

void main()
{
    // creating array of pointers
    
    // array of pointers helps us to create any size string without defining the size of string
    char *p[3] = {"cricket","football","basketball"};

    // iterator to traverse array of pointers
    int i;

    // traverse array of pointers
    for (i = 0; i < 5; i++)
    {
        printf("%s,\n",*(p+i));
    }   
}
