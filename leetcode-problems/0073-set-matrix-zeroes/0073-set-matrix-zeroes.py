class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zero_indices = []

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if(matrix[x][y] == 0):
                    zero_indices.append((x,y))
        
        for r,c in zero_indices:
            for x in range(r,len(matrix)):
                matrix[x][c] = 0
            for x in range(r,-1,-1):
                matrix[x][c] = 0
            for y in range(c, len(matrix[0])):
                matrix[r][y] = 0
            for y in range(c, -1,-1):
                matrix[r][y] = 0

         
