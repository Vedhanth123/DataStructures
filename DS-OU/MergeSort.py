# create an array
array = [9,8,7,6,5,4,3,2,1,0]

def MergeSort(array):
    
    if(len(array) == 1):
        return array
    # divide the array into 2 parts every time till the size of array is 1
    left = MergeSort(array[:len(array)//2])
    right = MergeSort(array[len(array)//2:])


    left_index = 0
    right_index = 0

    # creating another array to store merged and sorted array
    merged_sorted_array = []

    while(left_index < len(left) and right_index < len(right)):
        if(left[left_index] < right[right_index]):
            merged_sorted_array.append(left[left_index])
            left_index += 1
        else:
            merged_sorted_array.append(right[right_index])
            right_index += 1
    
    if(left_index == len(left)):
        while(right_index < len(right)):
            merged_sorted_array.append(right[right_index])
            right_index += 1
    else:
        while(left_index < len(left)):
            merged_sorted_array.append(left[left_index])
            left_index += 1
            
    return merged_sorted_array


print(MergeSort(array))