class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        
        for x in range(len(matrix)):

            y = x
            z = 0
            diag_elem = matrix[x][z]
            while(y < len(matrix) and z < len(matrix[0])):

                if(diag_elem != matrix[y][z]):
                    return False
                y += 1
                z += 1
        
        for x in range(1,len(matrix[0])):

            y = x
            z = 0
            diag_elem = matrix[z][y]
            while(z < len(matrix) and y < len(matrix[0])):

                if(diag_elem != matrix[z][y]):
                    return False
                
                y += 1
                z += 1

            
        return True
            
                    