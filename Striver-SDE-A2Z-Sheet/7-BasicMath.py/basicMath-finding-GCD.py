
# In this file we will be dealing with the basic math of the DSA

# 1) We will be solving the GCD of two numbers in the most naive way then we will be building upon that..

# Okay buddy let's solve the problem of the GCD if two given numbers are present

# a = int(input())
# b = int(input())

a = 10
b = 30

# The GCD's basic meaning in itself is that we need to find the most Greatest common factor among the two numers
# so to do that we first need to find the factors of the two numbers right. To find the factors of the two numbers we have our basic understanding already right. 

def findFactors(number: int) -> list:

    answer = []

    for x in range(1, number+1):
        if(not number % x):
            answer.append(x)
    
    return answer

a_factors = findFactors(a)
b_factors = findFactors(b)

print(a_factors)
print(b_factors)

GCD = 1

l1 = 0
r1 = 0

while(l1 < len(a_factors) and r1 < len(b_factors)):

    if(a_factors[l1] == b_factors[r1]):
        GCD = a_factors[l1]
        l1 += 1
        r1 += 1
    
    elif(a_factors[l1] < b_factors[r1]):
        l1 += 1
    else:
        r1 += 1

print(GCD)


