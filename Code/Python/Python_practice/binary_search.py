
def sorted_array(array, key, start = 0, end=10):

    # base case of recursion
    if(len(array) == 0):
        return "not found"

    # finding the midpoint of the array
    mid = (start + end) // 2

    # if element found returning the place of the 
    if(array[mid] == key):
        return f"found at {mid}"
    
    # checking if the key is less then the element in the mid
    if(array[mid] > key):

        # if the key is less than the element in the mid
        # search for the left part of the array
        return sorted_array(array, key, start=0, end=mid-1)
    
    # checking if the key is greater than the element in the mid
    else:

        # if the key is greater than the element in the mid
        # search for the right part of the array
        return sorted_array(array, key, start=mid+1, end=len(array)-1)
        
array = [1,2,3,4,5,6,7,8,9]
print(sorted_array(array, 9))

for x in range(10):
    print(sorted_array(array, x))
