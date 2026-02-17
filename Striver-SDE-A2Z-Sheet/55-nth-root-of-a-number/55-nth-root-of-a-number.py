def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here

    left = 0
    right = m
    answer = -1

    while(left <= right):
        mid = left + (right - left) // 2

        if(mid ** n == m):
            answer = mid
            break
        elif(mid ** n < m):
            left = mid + 1
        else:
            right = mid - 1

    return answer

NthRoot(n=3,m=27)