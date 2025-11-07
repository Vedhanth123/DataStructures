'''
1) To check if a number is missing in the array use sets to check
2) The question could be framed in such a way that 
que: An array contains all the numbers from 1 to n where n is the size of the array but... 
array contains a number which is repeated and a another number is missing
ex: [1,2,3,3,5]
ans: 4 number is missing and 3 is repeated
'''


def findTwoElement(arr):
    n = len(arr)

    # frequency array to count occurrences
    freq = [0] * (n + 1)
    repeating = -1
    missing = -1

    # count frequency of each element
    for num in arr:
        freq[num] += 1

    # identify missing and repeating numbers
    for i in range(1, n + 1):
        if freq[i] == 0:
            missing = i
        elif freq[i] == 2:
            repeating = i

    return [repeating, missing]

print(findTwoElement([1,2,3,3,5]))

'''
Time Complexity: O(n)
Space Complextiy: O(n)
'''