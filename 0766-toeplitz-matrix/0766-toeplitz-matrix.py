class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        r = len(matrix)
        c = len(matrix[0])

        # lt
        for lt in range(r):
            ltr = r
            ltc = 0
            diag = matrix[ltr][0]

            while(ltr < r and ltc < c):
                if(matrix[ltr][ltc] != diag):
                    return False
            
                ltr += 1
                ltc += 1
        
        # ut
        for ut in range(1, c):
            utc = ut
            utr = 0
            diag = matrix[utr][utc]
            
            while(utr < r and utc < c):
                if(matrix[utr][utc]!= diag):
                    return False
                
                utr += 1
                utc += 1
        
        return True