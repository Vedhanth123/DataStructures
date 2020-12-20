# # You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

# For example, given the arrays  and , there are two numbers between them:  and . , ,  and  for the first value. Similarly, ,  and , .


# 1) find the numbers between two arrays such that elements of first array are the factors
# of the numbers

# 2) the elements of the second array the are the multiples of the second array


# 1) find the multiples for the elements in the first array whose values are less than the first element in the 
# second array

a = [3,4]
b = [24,48]

i = a[-1]
counter = 0
numbers_being_considered = []

while (i <= b[0]):

    counter = 0

    for x in a:

        if(i % x == 0):
            counter += 1
    
    if(counter == len(a)):
        numbers_being_considered.append(i)

    i += 1

print(numbers_being_considered)

final_numbers = []
no_of_factors = 0

iterator = len(b)

# 2) the numbers considered are the factors of the elements in the second array

for x in numbers_being_considered:

    no_of_factors = 0

    for i in range(len(b)):

        if(b[i] % x == 0):
            no_of_factors += 1
        
    if(no_of_factors == len(b)):

        final_numbers.append(x)


print( len(final_numbers))




    