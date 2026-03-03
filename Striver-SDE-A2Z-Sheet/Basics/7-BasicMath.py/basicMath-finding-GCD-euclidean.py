# we all know the euclidean way of find the GCD of two numbers

# a = bq + r
# then a = b
# b = r

# a = int(input())
# b = int(input())

b = 10
a = 15

while(a % b):

    r = a%b
    q = a//b
    a = b
    b = r

print(b)

