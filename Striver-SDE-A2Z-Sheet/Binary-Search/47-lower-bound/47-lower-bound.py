def lowerBound(arr: list, n: int, x: int) -> int:
    # Write your code here

    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            if mid == 0 or arr[mid - 1] != x:
                return mid + 1
            else:
                right = mid - 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return 0


print(lowerBound([1, 2, 2, 3], 4, x=2))
