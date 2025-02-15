#include<stdio.h>

void binarysearch(int arr[], int l, int r, int k);
void binarysearch(int arr[], int l, int r, int k)
{
    int mid=(l+r)/2;
    if(!(l>r))
    {
        if(k==arr[mid])
        {
            printf("\n%d element is found at %d",k,mid);
        }
        else if (k>arr[mid])
        {
            return binarysearch(arr, mid+1, r, k);
        }
        else
        {
            return binarysearch(arr, l, mid-1, k);
        }
        
    }
    else
    {
        printf("\nElement not found");
    }
}
void main()
{
    int n, l, r, key, arr[5]={23,25,28,36,43};
    n=sizeof(arr)/sizeof(arr[0]);
    printf("\nEnter the element to search: ");
    scanf("%d",&key);
    binarysearch(arr, 0, n-1, key);
}