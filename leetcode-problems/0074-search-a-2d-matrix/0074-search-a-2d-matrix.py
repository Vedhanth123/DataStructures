from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix)

        while(top < bottom):

            midRow = (top + bottom) // 2

            if(matrix[midRow][0] <= target <= matrix[midRow][-1]):
                break 
            elif(target < matrix[midRow][0]):
                bottom = midRow
            else:
                top = midRow + 1
        
        left = 0
        right = len(matrix[0])

        while(left < right):

            mid = (left + right) // 2

            if(matrix[midRow][mid] == target):
                return True
            elif(target < matrix[midRow][mid]):
                right = mid
            else:
                left = mid + 1
        
        return False
    
print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
        
