# You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.

# Given the lengths of  sticks, print the number of sticks that are left before each iteration until there are none left.

# 1) append the len of array to another array storing the len of array every iteration  
# 2) find the smallest stick in the array
# 3) subtract length of smallest stick from each element in the array
# 4) find the len of array and store it
# 5) repeat till the size of array is 0


# 2) find the smallest stick in the array
def smallest_element_in_array(array):

    smallest_element = array[0]

    for x in range(len(array)):
        if(smallest_element > array[x]):
            smallest_element = array[x]
    
    return smallest_element

# 3) subtract length of smallest stick from each element in the array
def subtract_len_from_elements(len_smallest_element, array):

    for x in range(len(array)):
        array[x] = array[x] - len_smallest_element

# 4) find the len of array as well as removing 0s from the array
def len_of_array(array):

    no_of_zeros = 0
    for x in range(len(array)):
        
        if(array[x] == 0):
            no_of_zeros += 1
        
    for x in range(no_of_zeros):
        array.remove(0)

    return len(array)


arr = [1,2,0,0,0,5,2,3]
len_of_array(arr)

def cutTheSticks(arr):

    # 1) append the len of array to another array storing the len of array every iteration
    no_of_sticks_every_iteration = [len(arr)]

    while (len(arr) != 0):

        smallest_element = smallest_element_in_array(arr)

        subtract_len_from_elements(smallest_element, arr)

        no_of_sticks_every_iteration.append(len_of_array(arr))

    no_of_sticks_every_iteration.remove(0)
    
    return no_of_sticks_every_iteration

arr = [5, 4, 4, 2, 2, 8]
cutTheSticks(arr)


    


    


