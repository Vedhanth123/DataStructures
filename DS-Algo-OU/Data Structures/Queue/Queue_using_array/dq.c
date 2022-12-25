#include<stdio.h>
#include<stdlib.h>
#define SIZE 5


int Q[SIZE],f=-1,r=-1,x,i,y,a;
void inrq(int x){
	if((f==0 && r==SIZE-1) || (f==r+1))
    	printf("Queue overflow");
    else{
    if (r==SIZE-1 && f!=0)
	        r=-1;    
	    Q[++r]=x;
	    }
	    if(f==-1){
	        f++;
    }
}
void infq(int y){
    if (f<0)
        f = SIZE-1;
    else { 
        f = f-1;
        Q[f++]=a;
    }
} 
	
void delfq(){
    if(f==-1 && r==-1){
        printf("Queue underflow");    }
    else {
        printf("deleted element: %d\n",Q[f++]);
        if(f==SIZE)
            f=0;
        if(f-1==r)
        f=r=-1;
    }
}
void delrq(){
    if(f==-1 && r==-1){
        printf("Queue underflow");    }
    else {
        printf("deleted element: %d\n",Q[r--]);
        if(f==SIZE-1)
            f=0;
        if(f-1==r)
            f=r=-1;
        }
}
void display(){
    if(f==-1)
        printf("Queue underflow");
    else {
        i=f;
        printf("Queue elements are: ");
        if(f<=r){ 
            while(i<=r)
                printf("%d\t",Q[i++]);}
        else{
            while(i<=SIZE-1)
                printf("%d\t",Q[i++]);
                i=0;
            while(i<=r)
                printf("%d\t",Q[i++]);
   		}
 	}
}
int main(){
  infq(20);  
  inrq(30);
  inrq(40);
  infq(50);
  infq(60);
  display();
  delfq();
  display();
  delrq();
  display();
}