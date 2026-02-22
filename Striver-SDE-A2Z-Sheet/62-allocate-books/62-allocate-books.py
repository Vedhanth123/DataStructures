def findPages(arr: [int], n: int, m: int) -> int:

    left = max(arr)
    right = sum(arr)

    answer = float('inf')
    while(left <= right):

        mid = left + (right - left) // 2

        studentCount = 0
        localAnswer = float('-inf')
        studentPage = 0
        for pages in arr:
            if(studentPage + pages > mid):
                localAnswer = max(localAnswer, studentPage)
                studentPage = pages
                studentCount += 1
            else:
                studentPage += pages
        
        studentCount += 1
        localAnswer = max(localAnswer, studentPage)
        if(studentCount >= m):
            left = mid + 1
            if(studentCount == m):
                answer = min(answer, localAnswer)
        else:
            right = mid - 1
    
    return answer
print(findPages([25, 46, 28, 49, 24], 5, 4))
