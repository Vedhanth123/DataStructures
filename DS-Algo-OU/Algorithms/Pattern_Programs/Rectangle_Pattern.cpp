#include <iostream>
using namespace std;

int main()
{
    // iterate a for loop for columns
    int rows;
    cout << "Enter no. of rows:\n";
    cin >> rows;

    int columns;
    cout << "Enter no. of columns:\n";
    cin >> columns;

    int iterator;
    // iterate a for loop for rows
    while(rows > 0)
    {
        iterator = columns;
        // iterate a for loop for columns
        while(iterator > 0)
        {
            cout << "*";
            iterator -= 1;
        }
        cout << "\n";
        rows -= 1;

    }

    return 0;

}