#include <iostream>
using namespace std;

int main()
{

    int row = 5;
    int column = 5;

    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            if ((j == 1 || j == 5) || (i == 1 || i == 5))
            {
                cout << "*";
            }
            else
            {
                cout << " ";
            }
        }
        cout << "\n";
    }
    return 1;
}