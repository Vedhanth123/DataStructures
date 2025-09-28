from typing import List
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        distances = [0] + [float('inf')] * (n-1)

        while(k != -1):

            temp = distances.copy()
            for source, destination, price in flights:

                temp[destination] = min(distances[destination], temp[source] + price)
            
            distances = temp
            k -= 1

        return distances[dst]

        
obj = Solution()
obj.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1)
