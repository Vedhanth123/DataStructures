# program to print factorial of a number iteratively


print("Enter the limit of the factorial :")


limit = 5
a = 1
factorial = 1

while a <= limit:
    factorial = factorial*a
    a += 1

print("The factorial is :", factorial)

