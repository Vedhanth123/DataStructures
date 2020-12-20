# implementation of mergesort

import random

def mergesort(array):

    # base condition of function
    if(len(array) == 1):
        return array
    
    else:

        # splitting the array into two parts
        # running the functions to split the array further
        # returns splitted and sorted array
        left = mergesort(array[len(array)//2:])
        right = mergesort(array[:len(array)//2])

        # merging the two arrays
        merged_and_sorted_array = []

        # checking which splitted array is larger 
        if(len(left) < len(right)):

            # sorting and inserting elements of both splitted arrays into a single array
            index_of_left_array = index_of_right_array = 0
            while(index_of_left_array < len(left) and index_of_right_array < len(right)):
                
                if(left[index_of_left_array] < right[index_of_right_array]):
                    merged_and_sorted_array.append(left[index_of_left_array])
                    index_of_left_array += 1

                else:
                    merged_and_sorted_array.append(right[index_of_right_array])
                    index_of_right_array += 1

            while( index_of_right_array < len(right)):
                merged_and_sorted_array.append(right[index_of_right_array])
                index_of_right_array +=1
            
            while(index_of_left_array < len(left)):
                merged_and_sorted_array.append(left[index_of_left_array])
                index_of_left_array += 1

        else:

            # sorting and inserting elements of both splitted arrays into a single array
            index_of_left_array = index_of_right_array = 0
            while (index_of_left_array < len(left) and index_of_right_array < len(right)):

                if(left[index_of_left_array] < right[index_of_right_array]):
                    merged_and_sorted_array.append(left[index_of_left_array])
                    index_of_left_array += 1

                else:
                    merged_and_sorted_array.append(right[index_of_right_array])
                    index_of_right_array += 1
            
            while( index_of_right_array < len(right)):
                merged_and_sorted_array.append(right[index_of_right_array])
                index_of_right_array += 1

            
            while(index_of_left_array < len(left)):
                merged_and_sorted_array.append(left[index_of_left_array])
                index_of_left_array += 1

        return merged_and_sorted_array


