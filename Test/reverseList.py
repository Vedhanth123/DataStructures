'''
1) Put left and right pointers in the far ends of the list
2) Swap the numbers in the left and right position of the number
3) Do it till left < right
4) This will work even if the array's length is odd or even
'''

li = [1,2,3,4,5,6]

left = 0
right = len(li) - 1
while(left < right):
    
    # swap the numbers in left and right indices
    li[left], li[right] = li[right], li[left]
    left += 1
    right -= 1

print(li)

'''
Time Complexity: O(n)
space complexity: O(1)
'''