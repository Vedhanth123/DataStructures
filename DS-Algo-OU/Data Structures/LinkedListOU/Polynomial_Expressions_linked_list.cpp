#include <iostream>
using namespace std;

// create a node to store univariate expressions
struct univariate
{
    char data;
    char power;
    struct univariate *right;
};

// given an expression convert polynomial expression from string to linked list format

string number_string = "1234567890";
string characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
string operators = "+-";

// 1) Take input of a string
string input()
{
    string expression;

    cin >> expression;

    return expression;
}

// 2) split the strings from + and - points in the string
void splitter(string str)
{
    int i = 0;
    int ni = 0;

    string number;
    string power;

    while (str[i] != NULL || str[i] != '\0')
    {
        // checking if str[i] belongs to numbers
        while (ni < number_string.length())
        {
            if(str[i] == number_string[ni])
            {
                // store that data into another variable
                number.push_back(str[i]);
                break;
            }

            ni += 1;
            break;
        }


        // checking if str[i] belongs to characters
        while( ni < number_string.length())
        {
            if(str[i] == characters[ni])
            {   
                
            }
    
        }

        // checking if power exists

    }
}

int main()
{
    return 0;
}
