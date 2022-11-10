#include <stdio.h>

void main()
{
    // declaring a structure
    struct sports_player
    {
        int age;
        char name[10];
    }s1;

    // initializing address of struct into a pointer
    struct sports_player *pointer = &s1;

    // reading elements into a structure using pointer
    scanf("%i",&pointer->age);
    scanf("%s",&(*pointer).name);

    // accessing elements from a structure using pointer
    printf("%i,%s\n",pointer->age,(*pointer).name);

    // 19124-CM-111 Vedhanth
}
