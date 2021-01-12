var=int(input("Enter a number you want to check for the prime factors:"))
x = 1
count = 0
while ( x <= var ):
    if(var%x==0):
        count = count + 1
    x = x + 1
if(count == 2):
    print("The number is prime")
else:
    print("The number is not prime")    