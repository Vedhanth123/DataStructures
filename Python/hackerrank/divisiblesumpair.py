# python program to solve divisible sum pair

# You are given an array of n integers
# and a positive integer,k.
# Find and print the number of pairs where a[i] + a[j] is divisible by k.


def divisibleSumPairs(n, k, ar):

    # variable to store no of pairs
    counter = temporary_sum = 0

    # looping through array
    for x in range(len(ar)):

        # looping through array once again taking into consideration of array[i] every single time
        for y in range(len(ar)):

            if(x+y >= len(ar)):
                break

            # if y == 0 then some elements will be checked two times resulting in incorrect answer
            if(y == 0):
                continue

            else:
                temporary_sum = ar[x] + ar[x+y]
                if(temporary_sum % k == 0):
                    print(temporary_sum)
                    counter += 1
                
            temporary_sum = 0

    return counter

print(divisibleSumPairs(6,3,[1, 3, 2, 6 ,1 ,2]))                