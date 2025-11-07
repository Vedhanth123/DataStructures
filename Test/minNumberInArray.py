'''
1) To find largest element in an array
2) Create a variable and initialize it to atmost minimum value
3) at every index check if the current number is greater than the number in the array
4) If it is then update the number
5) Return the number
'''

array = [5,3,-9,10, 1]

def findminNumber(array):

    minNumber = float("inf") # atmost maximum value in python
    minNumberIndex = 0

    for x in range(len(array)):

        if(minNumber > array[x]):
            minNumber = array[x]
            minNumberIndex = x
        
    return [minNumberIndex, minNumber]
    
print(findminNumber(array))

'''
Time Complexity: O(n)
Space Complextiy: O(1)
'''