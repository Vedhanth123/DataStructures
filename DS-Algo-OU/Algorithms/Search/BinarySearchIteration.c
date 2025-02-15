#include<stdio.h>
int binarysearch(int key);
void main()
{

    int k, arr[5]={23,27,28,36,43}, l=0, r=4 ,result=-1;
    printf("Enter the element to search: ");
    scanf("%d",&k);


    int binarysearch(int key)
    {
        int mid;
        while(!(l>r))
        {
            mid = (l+r)/2;
            if(key==arr[mid])
            {
                printf("\n%d element is found at %d",k,mid);
                return 1;
            }
            else if (key>arr[mid])
            {
                l=mid+1;
            }
            else
            {
                r=mid-1;
            }
        }
        printf("element not found");
    }

    binarysearch(k);
}