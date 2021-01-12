# You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.

# image

# Note that  is indexed from  to , where  is the number of attributes.

# Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
n = 5
m = 3
k = 1

athlete_sorted = []

# firstly insert kth row into an array and sort that array

kth_sorting_array = []

for i in range(n):

    kth_sorting_array.append(arr[i][k])

kth_sorting_array.sort()
# print(kth_sorting_array)

# now using the element of the kth_sorting_array find out the whole inner list and insert 
# it into a frest list

for j in range(len(array)):

    
    for i in range(len(array)):