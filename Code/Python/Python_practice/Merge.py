
# take an array 
# go on splitting it into 2 parts untill size of array is 1
# sort and merge all the arrays

array = [4,3,2,1]

def MergeSort(array,low, high):

    if(low>=high):
        return 0
    
    # creating left array

    mid = (low+high-1)//2

    left = array[:mid]

    right = array[mid+1:]

    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    
    while (j < n2) 
        arr[k] = R[j]
        j+=1
        k+=1
    }

