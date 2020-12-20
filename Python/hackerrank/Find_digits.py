# An integer  is a divisor of an integer  if the remainder of .

# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.


# 1) given a number check if its each digit divides with the actual number

# 2) store the actual number
# 3) pick up every digit of the number by dividing the number by 10 and taking its remainder
# 4) divide the stored number with the newly obtained number
# 5) if the number is divisible with the obtained number then increase the counter
# 6) lastly return the counter

def findDigits(n):

    storage_of_number = n
    no_of_numbers_divisible = 0

    while(n != 0):

        remainder = n % 10

        if(remainder == 0):
            n //= 10
            continue    

        if(storage_of_number % remainder == 0):
            no_of_numbers_divisible += 1
        
        n //= 10
        
    return no_of_numbers_divisible

print(findDigits(1011))