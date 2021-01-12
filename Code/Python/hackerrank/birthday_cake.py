# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# Example


# The maximum height candles are  units high. There are  of them, so return .

# Function Description

# Complete the function birthdayCakeCandles in the editor below.

# birthdayCakeCandles has the following parameter(s):

# int candles[n]: the candle heights


# program to find number of biggest values in ar


# importing mergesort algorithm

# function to find num of biggest values in ar

ar = [3,2,1,3]

biggest_value = ar[0]

for x in range(len(ar)):

    if(x >= biggest_value):
        biggest_value = x

# assigning the biggest value in a variable 
# counter
no_of_biggest_values = 0

# looping through the ar to find out number of biggest values in ar
for x in range(len(ar)):

    if(ar[x] == biggest_value):
        no_of_biggest_values += 1

print(no_of_biggest_values)

