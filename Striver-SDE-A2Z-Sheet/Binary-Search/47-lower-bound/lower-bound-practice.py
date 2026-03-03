def lowerBound(arr: list, n: int, x: int) -> int:
    # Write your code here

    left = 0
    right = n-1
    answer = n
    while(left <= right):
        mid = left + (right - left) // 2
        if(arr[mid] > x):
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer

print(lowerBound([1, 2, 2, 3], 4, x=2))
