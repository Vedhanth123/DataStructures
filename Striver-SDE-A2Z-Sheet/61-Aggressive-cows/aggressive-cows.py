def aggressiveCows(stalls, k):
    # Write your code here.

    stalls.sort()
    min_value = min(stalls)
    max_value = max(stalls)

    left = 1
    right = (max_value - min_value)

    answer = float('-inf')

    while(left <= right):
        mid = left + (right - left) // 2

        remCows = k-1
        localAnswer = float('inf')

        # place the first cow in the first stall
        prev_cow = stalls[0]
        for i in range(1, len(stalls)):
            if(stalls[i] - prev_cow >= mid):
                remCows -= 1
                localAnswer = min(localAnswer, stalls[i] - prev_cow)
                prev_cow = stalls[i]
            
            if(remCows == 0):
                break
        
        if(remCows == 0):
            left = mid + 1
            answer = max(answer, localAnswer)
        else:
            right = mid - 1
        
    
    return answer

print(aggressiveCows([0 ,3 ,4 ,7 ,10,9], 4))
