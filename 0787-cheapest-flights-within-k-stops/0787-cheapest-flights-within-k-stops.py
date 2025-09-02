class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float('inf')] * n
        prices[src] = 0


        while k >= 0:

            # 1. Right at the beginning, make a copy of the prices from the last iteration.
            #    This `temp` array will store the new prices we find in this iteration.
            temp = prices.copy()

            # 2. Now, loop through all the flights to calculate the new prices.
            for u, v, dist in flights:
                
                # 3. CRUCIAL: Read from the original `prices` array (the previous state)
                #    and write the result into your `temp` array (the new state).
                if prices[u] != float('inf'):
                    temp[v] = min(temp[v], prices[u] + dist)

            # 4. After checking all flights, the `temp` array now holds the best prices
            #    for this number of stops. So, update `prices` to be this new state
            #    for the next iteration of the loop.
            prices = temp
            
            # 5. Decrement k
            k -= 1
    
        
        return prices[dst] if prices[dst] != float('inf') else -1