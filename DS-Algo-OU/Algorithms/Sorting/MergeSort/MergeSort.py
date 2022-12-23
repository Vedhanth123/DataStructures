# Write a python program to implement MergeSort

# 1) take an array
array = [5,4,3,2,1]

# Merge the divided arrays
def Merge(array, left, mid, right):

    

# 2) Write a function to divide the array
def MergeSort(array, left, right):

    if(left < right):
        # find out mid
        mid = (left + right) // 2

        # split the array into two parts
        MergeSort(array, left, mid)
        MergeSort(array, mid+1, right)
    

    