
print("Enter any two numbers which you want to find gcd of")
# num1 = int(input())
# num2 = int(input())

num1 = 12
num2 = 15


# assigning all factors of two numbers into lists
# factors2 = arr.array('i',[])

# assigning common factors of both the numbers into a list


# final answer will be assigned to this
largest_common_factor = 0
# finding all the factors of both

# function to find out GCD of two numbers
def GCD(num1,num2):

    # checking which of the number is greatest
    if(num1 < num2):
        lowest = num1
        highest = num2
    else:
        lowest = num2
        highest = num1

    # looping through the range of highest number to find the GCD
    for x in range(1,highest + 1):
        if lowest % x == 0 and highest % x == 0:
            gcd = x
    return gcd

print(GCD(num1,num2))

