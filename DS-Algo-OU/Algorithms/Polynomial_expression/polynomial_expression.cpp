#include <iostream>
using namespace std;


struct Polynomial
{
    int coefficient;
    int powerx;
    struct Polynomial *next;
};

struct Polynomial_terms
{
    string term;
    struct Polynomial_terms *next;
};

struct Polynomial_terms *head = NULL, *tail = NULL;
struct Polynomial *h = NULL, *t = NULL;

// create a struct to store the polynomials in a linked list
// take input of the polymial expression
// divide the polynomial expressions into different terms

// check the polynomial expression if it contains any powers or coefficients
int power_checker(string term)
{
    int i = 0;
    bool var_found = false;

    while(term[i] != '\0')
    {
        if(term[i] == 'x')
        {   
            var_found = true;
            while(term[i] != '\0')
            {
                if(term[i] == '^')
                {
                    return ((int)term[i+1] - 48);
                }
                i ++;
            }
            break;
        }
        i ++;
    }
    if(var_found == true)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int coefficient_checker(string term, struct Polynomial *p)
{
    if(term[0] == 'x')
    {
        p->coefficient = 1;
        p->powerx = power_checker(term);
    }
    else
    {
        p->coefficient = ((int)term[0] - 48);
        p->powerx = power_checker(term);
    }
}


// create a struct to store the polynomials in a linked list

// take input of the polynomial expression
/*
void input_polynomial()
{
    cin >> polynomai_expression;
}
*/

// divide the expression into different terms
void divide_expression(char polynomial_expression[])
{
    int i = 0;
    string temp;
    // traverse the expression till you reach + or minus
    while (polynomial_expression[i] != '\0')
    {
        if (polynomial_expression[i] != '+')
        {
            temp += polynomial_expression[i];
            i += 1;
        }

        if (polynomial_expression[i] == '+')
        {
            struct Polynomial_terms *n1 = new struct Polynomial_terms;
            n1->term = temp;
            if (head == NULL)
            {
                head = n1;
            }
            else
            {
                tail->next = n1;
            }
            tail = n1;
            temp = "";
            i++;
        }
    }
    struct Polynomial_terms *n1 = new struct Polynomial_terms;
    n1->term = temp;
    if (head == NULL)
    {
        head = n1;
    }
    else
    {
        tail->next = n1;
    }
    tail = n1;
    temp = "";
}

void display_linked_list()
{
    struct Polynomial_terms *temp = head;
    
    while(temp)
    {
        struct Polynomial *t1 = (struct Polynomial*) malloc(sizeof(struct Polynomial));
        t1->next = NULL;
        coefficient_checker(temp->term, t1);
        if(h == NULL)
        {
            h = t1;
        }
        else
        {
            t->next = t1;
        }
        t = t1;
        cout << "Expression " << temp->term << ": "; 
        cout << "coefficient = " << t1->coefficient << " ";
        cout << "powerx = " << t1->powerx << endl;
        temp = temp->next;
    }

}
int main()
{
    char polynomial_expression[] = "2x^2+2x+2+3x^9+2+1+6x+9x+x^3+2+x+0" ;
    divide_expression(polynomial_expression);
    display_linked_list();
    return 1;
}