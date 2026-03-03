
def subarraysXor(arr, k):
    # Write your code here
    # Return an integer

    xor_sum = 0
    count = 0
    hashMap = {0:1}

    for i in range(len(arr)):

        xor_sum ^= arr[i]
        target = xor_sum ^ k
        print(xor_sum, target, hashMap)
        if(target in hashMap):
            count += hashMap[target]
        
        hashMap[xor_sum] = hashMap.get(xor_sum, 0) + 1

    return count

print(subarraysXor([5,3,8,3,10],8))