# create an array
array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def MergeSort(array):

    # stop recursion of the array if the size of the array is 1
    if (len(array) == 1):
        return array

    # divide the array into 2 parts every time till the size of array is 1
    left = MergeSort(array[:len(array)//2])
    right = MergeSort(array[len(array)//2:])

    # creating indexes for the left and right arrays
    left_index = 0
    right_index = 0

    # creating another array to store merged and sorted array
    merged_sorted_array = []

    # traversing though left array and making sure that we don't over traverse the left and right array
    while (left_index < len(left) and right_index < len(right)):

        # if element of the left array is less that right array
        if (left[left_index] < right[right_index]):

            # insert the element of the left array into merged and sorted array
            merged_sorted_array.append(left[left_index])
            left_index += 1
        else:

            # insert the element of the right array into merged and sorted array
            merged_sorted_array.append(right[right_index])
            right_index += 1

    # checking if left array is fully traversed
    if (left_index == len(left)):

        # traversing till the right array is completely traversed
        while (right_index < len(right)):

            # inserting the elements of the right array into merged and sorted array
            merged_sorted_array.append(right[right_index])
            right_index += 1

    # if the left array is not fully traversed then traverse the array properly
    else:

        # traversing till the left array is completely traversed
        while (left_index < len(left)):

            # inserting the elements of the left array into merged and sorted array
            merged_sorted_array.append(left[left_index])
            left_index += 1

    return merged_sorted_array


print(MergeSort(array))
