#include <iostream>
using namespace std;

// program to add two trivariate expressions

// 1) Create a struct to store trivariate terms
struct trivariate
{
    int data;
    int powerx;
    int powery;
    int powerz;
    struct trivariate *right;
};

// 2) Create two trivariate terms
struct trivariate *t1 = (struct trivariate*) malloc(sizeof(struct trivariate));
struct trivariate *t2 = (struct trivariate*) malloc(sizeof(struct trivariate));

t1->data = 100;
t1->powerx = 2;
t1->powery = 4;
t1->powerz = 7;

t1->data = 100;
t1->powerx = 3;
t1->powery = 5;
t1->powerz = 8;


int main()
{

}