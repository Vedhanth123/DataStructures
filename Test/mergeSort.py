
array = [5,4,3,2,1]

def mergeSort(array, left, right):

    if(right - left > 1):

        mid = left + (right - left) // 2

        mergeSort(array, left, mid)
        mergeSort(array, mid, right)
    

        i = left
        j = mid
        merged = []

        while(i < mid and j < right):
            if(array[i] < array[j]):
                merged.append(array[i])
                i += 1
            else:
                merged.append(array[j])
                j += 1
        
        while(i < mid):
            merged.append(array[i])

            i += 1
        while(j < right):
            merged.append(array[j])
            j += 1


        for k in range(len(merged)):
            array[left + k] = merged[k]
        
print(mergeSort(array, 0, len(array)))
print(array)