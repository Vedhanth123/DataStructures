# python program to implement insertion sort


def insertion_sort(array):

    # looping through array from index '1'
    for x in range(1, len(array)):

        # storing a value to be checked if it is sorted
        key = array[x]

        # creating an invariable
        i = x - 1

        # checking if it is sorted if not then keeping it in the correct place
        while ((key < array[i]) and (i >= 0)):

            # swapping till the key gets to its proper place
            array[i+1], array[i] = array[i], array[i+1]
            i -= 1

    return array
