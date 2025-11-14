from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        maxleft = 0
        maxright = 0

        total = 0

        for x in range(len(height)):
            maxleft = max(maxleft, height[x])
            maxLeft[x] = maxleft

        for x in range(len(height)-1, -1, -1):
            maxright = max(maxright, height[x])
            maxRight[x] = maxright
        
        
        for x in range(1, len(height)-1):

            borders = min(maxRight[x+1], maxLeft[x-1])
            depth = height[x]
            
            total += max(0, borders-depth)
        
 
obj = Solution()
obj.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])