'''
def rec(count):

    if(count == 5):
        return
    print(f"{count + 1} -> Vedhanth")
    rec(count + 1)

rec(0)

'''
# ------------ print from 1 to N

'''
def pri(count, n):

    if(count == n):
        return
    print(count + 1)
    pri(count + 1,n)

pri(0,5)
'''

# -------- print from n to 1
'''

def pri(n):
    if(n == 0):
        return
    print(n)
    pri(n-1)

pri(5)

'''

# ------- print linearly from 1 to N backtracking
'''
def pri(n):

    if(n == 0):
        return
    pri(n-1)
    print(n)

pri(5)
'''

# ------- print linearly from n to 1 backtracking
'''
def pri(count, n):

    if(count == n):
        return
    
    pri(count + 1, n)
    print(count + 1)

pri(0,5)
'''

# ------------ Sum of n numbers using return statement
'''
def s(n):


    if(n == 0):
        return 0
    return n + s(n-1)

print(s(3))
'''
# ----------- Reverse an array using recursion (two pointers )

'''
def rev(array, left, right):

    if(left + 1 >= right):
        return
    
    array[left], array[right] = array[right], array[left]
    rev(array,left+1, right-1)

array = [1,2,3,4,5,6]
print(array)
rev(array,0,len(array)-1)
print(array)

'''
# ------- Reverse an array using recursion (single pointer) 
'''
array = [1,2,3,4,5,6]
def rev(i):

    if(i == len(array)//2):
        return
    
    array[i], array[-(i+1)] = array[-(i+1)], array[i]
    rev(i+1)
    

print(array)
rev(0)
print(array)
'''

# -------- Check if a function is a palindrome or not

string = "madams"

def pal(i:int =0) -> bool:

    if(i == len(string)//2):
        return True

    if(string[i] != string[-(i+1)]):
        return False

    return pal(i+1)

print(pal())