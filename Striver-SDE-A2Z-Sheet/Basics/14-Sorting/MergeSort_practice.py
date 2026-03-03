array = [5,4,3,2,1,0]

def mergeSort(left, right):

    if(left < right):

        mid = left + (right - left) // 2

        mergeSort(left, mid)
        mergeSort(mid+1, right)

        left_array = array[left:mid+1]
        right_array = array[mid+1: right+1]

        k = left
        while(left_array and right_array):
            if(left_array[0] < right_array[0]):
                array[k] = left_array.pop(0)
                k += 1
            else:
                array[k] = right_array.pop(0)
                k += 1
        
        while(left_array):
            array[k] = left_array.pop(0)
            k += 1
        while(right_array):
            array[k] = right_array.pop(0)
            k += 1
        
mergeSort(0, len(array)-1)

print(array)
