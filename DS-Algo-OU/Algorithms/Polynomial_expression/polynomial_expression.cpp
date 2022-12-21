#include <iostream>
using namespace std;

// structure to create linked list of polynomials to store coefficient and power in it
struct Polynomial
{
    int coefficient;
    int powerx;
    struct Polynomial *next;
};

// structure to create linked list of polynomial terms
struct Polynomial_terms
{
    string term;
    struct Polynomial_terms *next;
};

// head and tail of polynomial term array
struct Polynomial_terms *head = NULL, *tail = NULL;

// head and tail of polynomial which stores coefficient and power in it
struct Polynomial *h = NULL, *t = NULL;


// take input of the polymial expression

// check the polynomial expression if it contains any powers or coefficients
int power_checker(string term)
{
    int i = 0;
    bool var_found = false;

    // iterating the whole term
    while(term[i] != '\0')
    {
        // checking if the term has variable
        if('a' <= term[i] <= 'z')
        {   
            // if we have a variable then we need check if there is a power to the variable
            var_found = true;

            // traversing the term 
            while(term[i] != '\0')
            {
                // checking if there is a power in the term
                if(term[i] == '^')
                {
                    // we have to check if there is double digit power to the term
                    int digit = 0;

                    // check the index next to the carot
                    i += 1;

                    while(term[i] != '\0')
                    {
                        digit = (digit * 10) + ((int)term[i] - 48);
                        i += 1;
                    }
                    // if we have then we return the power of the term
                    return digit;
                }
                i ++;
            }

            // after checking if there is no power to the term then break the loop 
            break;
        }
        i ++;
    }

    // if there is a variable to the term then return its power as 1
    if(var_found == true)
    {
        return 1;
    }
    // if there is no variable then the power would be 0
    else
    {
        return 0;
    }
}
int coefficient_checker(string term, struct Polynomial *p)
{
    p->coefficient = 0;
    // if there are no coefficients in the term
    if(term[0] == 'x')
    {
        p->coefficient = 1;
        p->powerx = power_checker(term);
    }
    // if there exists a coefficients in the term
    else
    {
        // p->coefficient = ((int)term[0] - 48);
        int i = 0;
        while(term[i] != 'x' && term[i] != '\0')
        {
            p->coefficient = (p->coefficient * 10) + ((int)term[i] - 48);
            i += 1;
        }
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

// divide the polynomial expressions into different terms
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
            // creating linked list to store the substring
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
    // stores the last term in the linked list
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

// function to display all the polynomials converted to linked list format
void display_linked_list()
{
    // traversing throught the substrings of polynomials
    struct Polynomial_terms *temp = head;
    
    while(temp)
    {
        // creating a linked list of the converted polynomials
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
    char polynomial_expression[] = "20x^200+2x+2+3x^9+2+1+6x+9x+x^3+2+x+0" ;
    divide_expression(polynomial_expression);
    display_linked_list();
    return 1;
}