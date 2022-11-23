#include <stdio.h>

// Let's create an array of size n
int array[5] = {0, 0, 0, 0, 0};

// --------------------------------------------------------- Insert from Rear -------------------------------------------------
// 1) point index at -1 at start
// 2) increment index
// 3) insert data to -1/ required place
// 4) stop at last.

// 1) point index at -1 at start
int insert_from_rear = -1;
void InsertFromRear(int data)
{
    if (insert_from_rear < 5 || (insert_from_rear == insert_from_front-1))
    {
        // 2) increment index
        insert_from_rear += 1;

        // 3) insert data to -1/ required place
        array[insert_from_rear] = data;
    }
    // 4) stop at last.
    else
    {
        printf("Queue is full");
    }
}

// --------------------------------------------------- Delete from Rear -----------------------------------------------
// 1) point index at -1
// 2) increment index
// 3) delete data
// 4) stop at last
int delete_from_rear = -1;

void DeleteFromRear()
{
    if (delete_from_rear < 5 || (delete_from_rear == delete_from_front-1))
    {
        // 2) increment index
        delete_from_rear += 1;

        // 3) insert data to -1/ required place
        array[delete_from_rear] = 0;
    }
    // 4) stop at last.
    else
    {
        printf("Queue is empty");
    }
}
// ---------------------------------------------------- Insert from Front ------------------------------------------------
int insert_from_front = 5;
// 1) point index at -1 at start
// 2) increment index
// 3) insert data to -1/ required place
// 4) stop at last.

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
int delete_from_front = 5;
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
int main()
{
  // ------------------------------ 1) ---------------------------
  // 1) insert half from rear
  // 2) try to check for overflow of insert from front
  
  // ------------------------------ 2) ---------------------------
  // 1) insert half from front
  // 2) try to check for overflow of insert from rear
  
  
}