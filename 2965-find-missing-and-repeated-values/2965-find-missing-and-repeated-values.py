class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        answer = [0,0]

        dictionary = {x:0 for x in range(1,(len(grid)**2) + 1)}



            
        for x in range(len(grid)):
            for y in range(len(grid[0])):

                dictionary[grid[x][y]] += 1
        
        for key,val in dictionary.items():
            if(val > 1):
                answer[0] = key
            if(key > 0 and val == 0):
                answer[1] = key
        
        return answer
            