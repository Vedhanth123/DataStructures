# problem from hacker rank to solve birthday chocolate problem

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    # function to return no of possible outcomes of chocolate

    counter = summer = x = y = 0
    
    while x < len(s):
        
        
        while y < m:
            if(y+x >= len(s)):
                return counter
            summer += s[y+x]
            y += 1
        
        y = 0
        #print(summer)
        if(summer == d):
            counter += 1
            summer = 0
        else:
            summer = 0
        

        x += 1
    return counter

s = [1, 2, 1, 3, 2]
d = 3
m = 2
print(birthday(s,d,m))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     s = list(map(int, input().rstrip().split()))

#     dm = input().rstrip().split()

#     d = int(dm[0])

#     m = int(dm[1])

#     result = birthday(s, d, m)

#     fptr.write(str(result) + '\n')

#     fptr.close()
