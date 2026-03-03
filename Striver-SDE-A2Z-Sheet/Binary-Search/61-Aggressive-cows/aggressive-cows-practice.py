stalls = [0,3,4,7,9,10]
k =  4

def can_put_cows(min_distance, stalls, k):

    prev_cow = stalls[0]
    cowCount = 1
    minDistance = float('inf')
    for x in range(1, len(stalls)):
        # print(f"prev_cow = {prev_cow}, cowCount = {cowCount}, current stall = {stalls[x]}",end="  | ")
        if(stalls[x] - prev_cow >= min_distance):
            minDistance = min(minDistance, stalls[x] - prev_cow)
            prev_cow = stalls[x]
            cowCount += 1
    
        # print(f"prev_cow = {prev_cow}, cowCount = {cowCount}, current stall = {stalls[x]}")
        if(cowCount == k):
            break
    
    # print(minDistance)
    if(cowCount == k):
        return minDistance
    else:
        return float('inf')


def aggressiveCows(stalls, k):

    # --------------------------------------- Brute Force -----------------------------------------
    max_stalls = max(stalls)
    min_stalls = min(stalls)
    answer = float('-inf')
    for x in range(1, (max_stalls - min_stalls) + 1):

        # let's check what will our answer be...
        # print(f"---------------------------- min distance {x} ---------------------------------")
        answer = max(answer, can_put_cows(x, stalls, k))


    return answer
print(aggressiveCows([1,2,3], 2))
