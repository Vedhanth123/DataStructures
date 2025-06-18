class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # 1) first search for the middle row's first value
        # 2) if middle row's first value is smaller then again search for it's last value
        # 3) if the last value is smaller then ignore this middle and the rows above it
        # 4) if the middle rows' fist value is greater than the value then ignore middle row and also ignore the rows below it

        top_row = 0
        bottom_row = len(matrix)
        to_search = 0

        while(top_row < bottom_row):

            mid_row = (top_row + bottom_row) // 2

            if(matrix[mid_row][0] <= target and target <= matrix[mid_row][-1]):
                to_search = mid_row
                break
            elif(matrix[mid_row][0] < target):
                top_row = mid_row + 1
            else:
                bottom_row = mid_row
        
        left = 0
        right = len(matrix[0])
    
        while(left < right):

            mid = (left + right)//2

            if(matrix[to_search][mid] == target):
                return True
            elif(matrix[to_search][mid] < target):
                left = mid+1
            else:
                right = mid
        
        return False
                
                

        