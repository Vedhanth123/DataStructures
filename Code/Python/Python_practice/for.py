# program to find number of biggest values in array

# importing mergesort algorithm
from Mergesort import mergesort

# function to find num of biggest values in array

def biggest_valuees(ar):

    # sorting the array
    ar.sort()

    # assigning the biggest value in a variable
    biggest_value = ar[-1]

    # counter
    no_of_biggest_values = 0

    # looping through the array to find out number of biggest values in array
    for x in range(len(ar)):

        if(ar[(len(ar)-1)-x] == biggest_value):
            no_of_biggest_values += 1

        else:
            break

    print(no_of_biggest_values)

biggest_valuees([1,2,4,4,2])