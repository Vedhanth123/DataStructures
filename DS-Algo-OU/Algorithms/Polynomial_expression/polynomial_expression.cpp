#include <iostream>
using namespace std;

// create a struct to store the polynomials in a linked list
// take input of the polymial expression
// divide the polynomial expressions into different terms

struct Polynomial_terms
{
    string term;
    struct Polynnomial_term *next;
};

struct Polynomial_terms *head = NULL;

void append(string term)
{
    Polynnomial_term *n1;
    n1 = (struct Polynomial_term*) malloc(sizeof(struct Polynomial_term));
    n1->term = term;
}

// create a struct to store the polynomials in a linked list
struct Polynomial
{
    int coefficient;
    int powerx;
    struct Polynomial *next;
};

// take input of the polynomial expression
string polynomai_expression;
void input_polynomial()
{
    cin >> polynomai_expression;
}


// divide the expression into different terms
void divide_expression()
{

}
int main()
{   

    return 1;
}