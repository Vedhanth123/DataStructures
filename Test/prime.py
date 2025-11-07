'''
If there is atleast 1 factor between 1 and the number itself then call it prime else not
'''

# program to check whether a number is prime or not

num = 2


def isPrime(num):
    factors = 0
    for x in range(2,num):
        if(num % x == 0):
            return "Prime"
    
    return "not Prime"

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

