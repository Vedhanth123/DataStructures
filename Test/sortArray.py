# Bubble sort algorithm
'''
1) Bubble sort algorithm work in the principle by checking if there is a number in the left side of the array
which is greater than the elements which are in the right side of the array
2) If there is a number then swap the numbers
3) This makes sure that the largest number gets to its desired position first followed by other numbers
'''

arr = [5,4,3,2,1]

for x in range(len(arr)):
    for y in range(len(arr)-1):

        # if the the left number is greater than the right side of the number then swap
        if(arr[y] > arr[y+1]):
            arr[y], arr[y+1] = arr[y+1], arr[y]

print(arr)

'''
Time Complexity: O(n^2)
space complexity: O(1)

'''