def quicksort(left: int, right: int, array: list):

    if left < right:
        # let's take the first index as the pivot
        pivot = array[left]
        i = left
        j = right

        while i < j:
            while i <= right and array[i] <= pivot:
                i += 1

            while j >= left and array[j] > pivot:
                j -= 1

            if j >= i:
                array[i], array[j] = array[j], array[i]

        array[left], array[j] = array[j], array[left]

        quicksort(left, j - 1, array)
        quicksort(j + 1, right, array)


if __name__ == "__main__":
    array = [4, 3, 7, 2, 5, 1]

    # sorted_array = [1,2,3,4,5,7] for reference
    quicksort(0, len(array) - 1, array)
    print(array)
