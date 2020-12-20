# program to print factorial of a number

# fact = int(input("Enter number for which you want to find factorial of it : "))
from time import time
sec = time()


def fact(num):

    if num > 1:
        return num*fact(num-1)
    else:
        return num


print(fact(-1))


""" logic of the program """
""" firstly num*fact(num-1) will be executed as if statement is true 
    fact(num-1) will create its own memory and another virtual function will be executed arugument as num - 1 (in this case as 4)
    then again virtual function will be executed with num - 1 (3 in this case)
    this will go on till number reaches 2 again virtual function will be executed then next time number reaches 1
    so as in else staement num will be return as 1 (num is 1 right) so this num as 1 will be return to recently created virtual function 
    which is [2*fact(2-1)]  the function call will be replaced with 1 as else statement returned 1 so now
    [2*1] will be returned to its predecessor which is [3*fact(3-1)] now fact will be again replaced wil [2*1] which is 2
    now again [3*2] will be returned to its predecessor which is [4*fact(4-1)] this will go on till it reaches the first function call and at last
    all the function execution is cleared then the last answer will be returned. [ in this case this will go to main function to be printed.]
"""
