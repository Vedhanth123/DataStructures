#include <stdio.h>

// Search in online!!!!!!!!!!!
// Applications of Queues
// 1) OS -> Multi Level Queue Scheduling
// 2) Networking -> Routers 

// Array Implementation of Queue

// we need a person to add elements to queue
int HOD_Vishal = 0;

// we need a person to remove elements from the queue
int Gyaneshwar = 0;

// We need students in college
int Students[3];

// We need function to execute insert
void insert(int pin_number)
{
    if(HOD_Vishal == 3)
    {
        printf("Line is Full\n");
    }
    else
    {
        Students[HOD_Vishal] = pin_number;
        HOD_Vishal ++;
    }
}

void remove_()
{
    if(Gyaneshwar == 3)
    {
        printf("Line is empty");
    }
    else
    {
        Students[Gyaneshwar] = 0;
        Gyaneshwar ++;
    }
}

int main()
{
    int pin[3] = {111, 114, 74};

    for(int i= 0; i < 5; i++)
    {
        insert(pin[i]);
    }
    for(int i = 0; i < 5; i++)
    {
        remove_();
    }
}