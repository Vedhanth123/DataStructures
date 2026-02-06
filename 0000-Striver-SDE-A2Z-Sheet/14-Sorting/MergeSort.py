
array = [5,4,3,2,1]

# MergeSort

# Divide the array into 2 parts
# Go on dividing the array into two parts till the size of the array you are dividing is not 1
# After dividing the array merget the sorted arrays by creating a new array
# This is a divide and conquer algorithm so... it needs recursion to solve this problem

# This file will return a new array
'''
def MergeSort(left: int, right: int) -> list[int]:

    # If here are 
    if(left + 1 >= right):
        return array[left:right]

    mid = (left + right) // 2
    left_array = MergeSort(left, mid)
    right_array = MergeSort(mid,right)

    mergedArray = []
    l = 0
    r = 0
    
    while(l < len(left_array) and r < len(right_array)):
        if(left_array[l] <= right_array[r]):
            mergedArray.append(left_array[l])
            l += 1
        else:
            mergedArray.append(right_array[r])
            r += 1
    
    while(l < len(left_array)):
        mergedArray.append(left_array[l])
        l += 1
    while(r < len(right_array)):
        mergedArray.append(right_array[r])
        r += 1
    
    return mergedArray

print(array)
array = MergeSort(0, len(array))
print(array)

'''


# If you want to create another array will will take the array and will not return anything but.. will sort it self.
array = [5,4,3,2,1,6]
def MergeSort(left, right):

    if(left + 1 >= right):
        return 

    mid = (left + right) // 2
    MergeSort(left, mid)
    MergeSort(mid, right)

    sortedArray = []
    l = left
    r = mid

    while(l < mid and r < right):
        if(array[l] <= array[r]):
            sortedArray.append(array[l])
            l += 1
        else:
            sortedArray.append(array[r])
            r += 1
        
    while(l < mid):
        sortedArray.append(array[l])
        l += 1

    while(r < right):
        sortedArray.append(array[r])
        r += 1
    
    # copy that to the original array
    for k in range(len(sortedArray)):
        array[k+left] = sortedArray[k]
    
print(array)
MergeSort(0,len(array))
print(array)



