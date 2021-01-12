# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

# Example


# There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.


# algorithm
# 1) take a number and compare it with every other number in the array after comparision remove that number
# 2) if the absolute difference is less than 1 or equal to one
# 3) append those two numbers into the array
# 4) lastly return the largest size of array among collection of arrays


def pickingNumbers(a):

    numbers_list = []

    for x in range(len(a)):

        lists = []

        lists.append(a[x])

        for y in range(x, len(a)):

            if(abs(a[x] - a[y]) <= 1):
                lists.append(a[y])

        numbers_list.append(lists)

    print(numbers_list)

    length_of_lists = len(numbers_list[0])

    for x in range(len(numbers_list)):

        if(length_of_lists < len(numbers_list[x])):
            length_of_lists = len(numbers_list[x])
    
    return length_of_lists

print(pickingNumbers([4, 6, 5, 3, 3, 1]))
