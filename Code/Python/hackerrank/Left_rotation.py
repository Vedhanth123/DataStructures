# A left rotation operation on an arr of size  shifts each of the arr's elements  unit to the left. Given an integer, , rotate the arr that many steps left and return the result.

# 1) move the first elements of the arr to the last
# 1.1) take first element and store it some where else
# 1.2) take second element and insert second element in first place continue till all the elements are seated

arr = [1,2,3,4,5]
storage = 0

for x in range(len(arr)):

    if(x == len(arr) - 1):
        arr[x] = storage
    
    if(x == 0):
        storage = arr[x]
    
    if(x < len(arr) - 1):
        arr[x] = arr[x+1]
    
print(arr)