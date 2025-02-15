#include<stdio.h>
#include<stdlib.h>

void linear_search(int key);

void main()
{

int k,pointer=0,array[5]={1,3,6,83,2};


int linear_search(int key)
{
	if(pointer==5)	
	{
		printf("element not found");
		//eturn 0;
	}
	else
	{
		if(key==array[pointer])
		{
			printf("%d element found at %d",key,pointer);
		}
		else
		{	
			pointer++;
			linear_search(key);

		}
	}
	
}
printf("enter element to search: ");
scanf("%d",&k);
linear_search(k);
}