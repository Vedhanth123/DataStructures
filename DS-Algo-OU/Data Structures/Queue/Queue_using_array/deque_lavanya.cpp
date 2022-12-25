#include <iostream>
using namespace std;


int array[5] = {0, 0, 0, 0, 0};

int insert_from_rear = -1;
int delete_from_front = 5;
int delete_from_rear = -1;
int insert_from_front = 5;

void InsertFromRear(int data)
{
    if (insert_from_rear < 5 || (insert_from_rear == insert_from_front - 1))
    {
        insert_from_rear += 1;
        array[insert_from_rear] = data;
    }
    else
    {
        printf("Queue is full");
    }
}

void DeleteFromRear()
{
    if (delete_from_rear < 5 || (delete_from_rear == delete_from_front - 1))
    {
        delete_from_rear += 1;
        array[delete_from_rear] = 0;
    }
    else
    {
        printf("Queue is empty");
    }
}
// ---------------------------------------------------- Insert from Front ------------------------------------------------

void InsertFromFront(int data)
{
    if (insert_from_front == -1 || (insert_from_front == insert_from_rear + 1))
    {
        printf("Queue is full");
    }
    else
    {
        insert_from_front -= 1;
        array[insert_from_front] = data;
    }
}

// -------------------------------------------------- Delete from Front --------------------------------------------------
void DeleteFromFront()
{
    if (delete_from_front == -1 || (delete_from_front == delete_from_rear + 1))
    {
        printf("Queue is full");
    }
    else
    {
        delete_from_front -= 1;
        array[delete_from_front] = 0;
    }
}
void display()
{
    int i;
    printf("The Queue elements are: \n");
    for (i = 0; i < 5; i++)
    {
        printf("%d, ", array[i]);
    }
    printf("\n");
}

int main()
{
    int choice;
    int value;
    while(1)
    {
        printf("1 for insert from front\n");
        printf("2 for insert from rear\n");
        printf("3 for delete from front\n");
        printf("4 for delete from rear\n");
        cin >> choice;

        if(choice == 1)
        {
            printf("Enter value you want to insert into Queue:\n");
            cin >> value;
            InsertFromFront(value);
            display();
        }
        else if(choice == 2)
        {
            printf("Enter value you want to insert into Queue:\n");
            cin >> value;
            InsertFromRear(value);
            display();
        }
        else if(choice == 3)
        {
            DeleteFromFront();
            display();
        }
        else if(choice == 4)
        {
            DeleteFromRear();
            display();
        }
        else
        {
            break;
        }
    }
}