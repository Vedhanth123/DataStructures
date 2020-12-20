# python program to implement power of a number using recursive approach

# algorithm:

# 1) x^0 = 1
# 2) if n is even then x^n = x^n/2 * x^n/2
# 3) if n is odd then x^n = x. x^n/2 * x*n/2
# 4) if n is negative then x^n = 1/x^-n

def power_using_recursion(number,power):

    if(power == 0):
        return 1

    elif(power % 2):
        return number * power_using_recursion(number,power//2) * power_using_recursion(number,power//2)
    else:
        return power_using_recursion(number,power//2) * power_using_recursion(number,power//2)

print(power_using_recursion(2,3))
