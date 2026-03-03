def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here

    left = 1
    right = 2 ** 16
    answer = [0]
    while(left <= right):

        mid = left + (right - left) // 2
        if(mid ** n <= m):
            left = mid + 1
            answer[0] = max(answer[0], mid)
        else:
            right = mid - 1
    
    return answer[0]

print(NthRoot(3, 27))