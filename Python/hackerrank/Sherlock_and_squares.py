# Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints. Sherlock must determine the number of square integers within that range.

# Note: A square integer is an integer which is the square of an integer, e.g. .

# 1) find the square root of the minimum number and round it to nearest value
# 2) square the obtained number and check if the square of the number is greater than the upper boundary
# 3) if the number is between the smaller and larger number increment no_of_squares
# 4) increment the number and repeat the process

from math import sqrt

def squares(a, b):

    number = int(sqrt(a))

    no_of_squares = 0

    while(not (a <= number** 2)):

        number += 1
    

    while(a <= number ** 2 <= b):

        no_of_squares += 1
        number += 1
    
    return no_of_squares    


squares(17,24)