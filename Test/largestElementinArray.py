'''
1) To find largest element in an array
2) Create a variable and initialize it to atmost minimum value
3) at every index check if the current number is less than the number in the array
4) If it is then update the number
5) Return the number
'''

array = [5,3,-9,10, 1]

def findMaxNumber(array):
    
    maxNumber = float("-inf") # atmost minimum value in python
    maxNumberIndex = 0

    for x in range(len(array)):

        if(maxNumber < array[x]):
            maxNumber = array[x]
            maxNumberIndex = x
        
        return [maxNumberIndex, maxNumber]
    
print(findMaxNumber(array))

'''
Time Complexity: O(n)
Space Complextiy: O(1)
'''