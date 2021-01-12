
# 1) take the last element of the array as pivot element
# 2) take two variables i and -1 and j as 0
# 3) if a[pivot] >= a[j] then increment i and swap a[i] and a[j]

def QuickSort(array, first, last):

    if(first >= last):
        return 0
        
    def pivot_adjuster(array, first, last):

        i = (first - 1)

        pivot = array[last]
        # adjusting values so that elements before pivot are less than pivot
        for j in range(first, last):

            if(array[j] <= pivot):

                i = i + 1

                # swapping i and j
                array[i],array[j] = array[j],array[i]

        # adjusting pivot element
        array[i+1],array[last] = array[last],array[i+1]

        return (i + 1)
    
    pivot = pivot_adjuster(array, first, last)

    # sorting left array not considering pivot element
    QuickSort(array, first, pivot-1)

    # sorting right array not considering pivot element
    QuickSort(array, pivot+1, last)


array = [10, 7, 8, 9, 1, 5] 

QuickSort(array, 0, len(array)-1)

print(array)
