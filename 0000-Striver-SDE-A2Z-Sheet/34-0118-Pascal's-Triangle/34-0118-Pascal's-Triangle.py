from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # This is the dynamic programming solution for this problem
        # here we do as the problem states us to do 
        # creating the current row using the previous row.
        # we tend to iterate every value in the previous row to create a new row
        '''
        Docstring for generate

        prev = [1]

        answer = [prev]

        for x in range(1,numRows):
            curr = [0] * (len(prev) + 1)
            for y in range(len(prev)):
                curr[y] += prev[y]
                curr[y+1] += prev[y]
            
            prev = curr
            answer.append(curr)
        
        return answer
        '''
        # --------------------- Striver's new technique O(n^3) -------------------------
        # Striver's solution for this problem is a bit different
        # he uses nCr formula.
        # his solution is that: to generate a new row we use row-1 C col-1 to generate a single number. 
        # but... if we iterate col from 0 to row (inclusive) then we can generate new row itself.
        
        '''
        def factorial(n: int) -> int:
            if(n <= 1):
                return 1
            else:
                return n * factorial(n-1)

        # THis function here is responsible for printing a single value 
        def nCr(n: int, r: int) -> int:

            answer = 1
            for col in range(1,r):
                answer *= (n - col)
                answer //= (col)
            
            # print(answer)
            return answer

        # I could call another loop to genearte a triangle (meaning I can create multiple rows by looping the rows again and again)
        for row in range(1,numRows+1):

            # I could call a simple for loop to generate a full row out of it
            for x in range(1,row+1):
                print(nCr(row,x),end=" ")
            print("")
        '''

        # another optimization O(n^2)
        def generateRow(row: int) -> List[int]:
            answer = [1]
            ans = 1
            for x in range(1, row):
                ans *= row - x
                ans //= x
                answer.append(ans)
            
            return answer
        
        result = []
        for row in range(1,numRows+1):
            result.append(generateRow(row))

        
        return result



        
Solution().generate(7)
        
                

