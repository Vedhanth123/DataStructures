from math import *
from collections import *
from sys import *
from os import *
from functools import reduce

def missingAndRepeating(arr, n):
    # Write your code here

    '''
    # sum of n natural numbers
    # sum of original array
    # find the difference

    # let x = missing, y = repeating
    # then mathematically x-y = diff of(sum of original) and (sum of n)

    # sum of sq of orignal
    # sum of sq of n natural
    # then mathematically x^2 - y^2 = diff2

    # then (x-y)(x+y) = diff2
    # sub x-y in eq2

    # diff * (x+y) = diff2
    # simplify x+y = diff2
    # solve for eq1 and eq2

    s = sum(arr)
    sn = n*(n+1) // 2
    diff = s - sn

    s2 = sum(list(map(lambda x:x*x, arr)))
    s2n = (n*(n+1)*(2*n+1)) // 6

    # s2n = sum(list(map(lambda x:x*x, [y for y in range(1, n+1)])))
    diff2 = s2 - s2n

    xplusy = diff2//diff 
    xminsy = diff

    repeating = ((xplusy) - xminsy)//2
    missing = xplusy - repeating

    if(diff < 0 and diff2 < 0):
        missing = abs(missing)
        repeating = abs(repeating)
    
    return [repeating, missing]

    print("Wait")

    '''

    # XOR method

    xor = 0
    # finding the xor of all numbers
    for x in range(n):

        # This will xor the given numbers
        xor ^= arr[x]

        # This will xor the numbers from 1 to n
        xor ^= x+1
    
    # to check for the set bit from the right side. we and it from left hand side. 
    # as and will return true if both the bits are one in this way we will find the 
    # set bit from the right hand side


    bitNo = 0
    while(True):

        # to find the bitNo we use left shift. basically we are finding where does our number change its polarity by anding (anding!) all the numbers from right to left
        if(xor & (1 << bitNo) != 0):
            break
        bitNo += 1

    
    zeroGroup = oneGroup = 0
    for x in range(n):

        # checking for numbers in the array
        # part of oneGroup
        if(arr[x] & (1 << bitNo)):
            oneGroup ^= arr[x]
        # part of zeroGroup
        else:
            zeroGroup ^= arr[x]

        # checking for all the numbers
        if(x+1 & (1 << bitNo)):
            oneGroup ^= x+1
        else:
            zeroGroup ^= x+1

    onecnt = 0
    for x in range(n):
        if(arr[x] == oneGroup):
            onecnt += 1

    if(onecnt == 2):
        return [oneGroup, zeroGroup]
    else:
        return [zeroGroup, oneGroup]

missingAndRepeating([4,3,6,2,1,1],6)
