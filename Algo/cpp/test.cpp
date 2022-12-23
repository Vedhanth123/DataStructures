#include <iostream>
using namespace std;
// to avoid std::cout and cin
// 1.program to call_by_value

void function(int a, int b)
{
    int temp;
    temp = a;
    cout << "temp var is storing the a value" << endl;
    a = b;
    cout << "a is storing the b value"<<endl;
    b = temp;
    cout << "b is storing the temp value"<<endl;
    cout << "after swapping" << a << endl;
    cout << "after swapping" << b;
}
int main()
{
    int c, d;
    cout << "enter the c value" << endl;
    cin >> c;
    cout << c << "this vallue will store in a"<<endl;
    cout << "enter the d value" << endl;
    cin >> d;
    cout << d << "this value will store in b"<<endl;
    function(c, d);
    return 0;
}
