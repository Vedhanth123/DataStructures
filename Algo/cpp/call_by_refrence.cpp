#include <iostream>
using namespace std;
// program to swap the values using pointers
void function(int *a, int *b)
{
    *a = *a * *b; // a = 30 = (10 + 20)
    *b = *a / *b; // b = 10 = (30 - 20)
    *a = *a / *b; // a = 20 = (30 - 10)
    cout << *a << endl
         << *b;
}

int main()
{
    int c, d;
    cout << "enter the c value";
    cin >> c;
    cout << "enter the d value";
    cin >> d;
    function(&c, &d);
}
