#include <iostream>
using namespace std;

int main()
{
    // inverted Half pyramid
    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 6 - i; j++)
        {
            cout << "*";
        }
        cout << "\n";
    }
    return 1;
}