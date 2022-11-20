#include <stdio.h>

int GCD(int a, int b)
{
    // if remainder of the numbers becomes zero stop recursion
    if(b == 0)
    {
        return a;
    }
    else // divide the two numbers and substitue a with b and b with remainder of a and b
    // Note: we need not find the division we just need to substitue the values as we have final answer in the termination condition itself
    {
        GCD(b, a%b);
    }
}

// GCD of two numbers
int main()
{
    int a = 55, b = 20;

    // 1) GCD of two numbers can be solved using Euclidean algorithm
    // a = bq + r 
    // a = larger number
    // b = smaller number
    // q = quotient
    // r = remainder

    // 2) till the r reaches 0
    // we substitue a with b and b with r for every successive iteration

    printf("%d", GCD(a, b));
}