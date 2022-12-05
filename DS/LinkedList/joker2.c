#include<stdio.h>
#include<stdlib.h>
struct node {
    int data;
    struct node *link;
}*head=NULL;
struct node *getnode(){
    struct node *temp =(struct node*)malloc(sizeof(struct node));
    return temp;
}
void insrt(int x){
    struct node *t=head;
    t = getnode();
    t->data=x;
    if(head==NULL)
    {
        t->link=NULL;
        head=t;
    }
    else
    {
        t->link=head;
        head=t;
    }
}
void ine(int y){
    struct node *t= head;
    t=getnode();
    t->data=y;
    t->link = NULL;
    if (head==NULL)
    {
        t->link=NULL;
        head=t;
    }
    else
    {
        struct node *temp =head;
        while(temp->link)
        {
            temp=temp->link;
        }
        temp->link=t;
    }
}
void inb(int z,int a)
{
    struct node *t= head;
    t=getnode();
    t->data=z;
    if(head==NULL)
    {
        t->link=NULL;
        head=t;
    }
    else{
    struct node *temp=head;
    while(temp->data!=a)
    {
        temp=temp->link;
    }
    t->link=temp->link;
    temp->link=t;
     }
}
void display(){
     if(head==NULL)
     printf("List is empty");
     else{
          struct node *temp=head;
          printf("\nList elements are: ");
          while(temp){
               printf("%d\t",temp->data);
               temp=temp->link;
          }
     }
}
int count(struct node *t){
    if(t)
        return 1 + count(t->link);
}
int cunt(struct node *t){
    int count =0;
    while(t){
          t=t->link;
          count=count+1;
     }
     return count;
}
void swap(int *x,int *y){
    int temp;
        temp=*x;
        *x=*y;
        *y=temp;
}    
int arrenge(struct node *t){
    struct node *u;
    int temp;
     while(t){
        u = head;
           while(u->link){
                  if (u->data>u->link->data){
                printf("Error is over here\n");
                swap(&(u->data), &(u->link->data));
                }
            u = u->link;
            }
        t = t->link;
        }
      return (t->data);
}

int main(){
  ine(600);
  ine(500);
  ine(400);
  ine(300);
  arrenge(head);
  display();
}