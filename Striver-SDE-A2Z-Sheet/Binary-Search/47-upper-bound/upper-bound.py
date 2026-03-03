def upperBound(arr: list, x: int, n: int) -> int:
    # Write your code here.
    
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

print(upperBound(arr = [2,4,6,7], x = 5, n= 4))
