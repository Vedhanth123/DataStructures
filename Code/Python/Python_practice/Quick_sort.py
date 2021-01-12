arr = [4,3,2,1,-1,-2,-3,4,5,10]

def pivoting_point(arr, first, last):

    i = first - 1
    pivot = arr[last]

    for x in range(first, last):

        if(pivot >= arr[x]):

            i += 1
            arr[x],arr[i] = arr[i],arr[x]

    arr[i+1],arr[last] = arr[last],arr[i+1]
    
    return i+1

def Quick_sort(arr, first, last):

    if(first >= last):

        return 0
    
    pivot_point = pivoting_point(arr, first, last)

    Quick_sort(arr, first, pivot_point-1)
    Quick_sort(arr, pivot_point+1, last)



Quick_sort(arr, 0, len(arr) -1)
print(arr)