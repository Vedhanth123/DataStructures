
array = [1,2,3,4,5]

def binarySearch(arr, target):

    left = 0
    right = len(arr)

    while(left < right):
        mid = left + (right - left) // 2

        if(arr[mid] == target):
            return mid
        elif(arr[mid] < target):
            left = mid + 1
        else:
            right = mid
    
    return -1

for x in range(len(array)):
    print(binarySearch(array, array[x]))

