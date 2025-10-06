from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Take the help of heapq so that we can do BFS traversal on the graph and also we make sure that we only visit the nearest ones first
        queue = [(0, k)]

        graph = defaultdict(list)

        for src, dest, dist in times:
            graph[src].append((dist, dest))
        
        distances = {x:float('inf') for x in range(1, n+1)}
        visited = set()

        distances[k] = 0

        while(queue):

            weight, node = heapq.heappop(queue)

            if(node not in visited):

                visited.add(node)
                for n_dist, neigh in graph[node]:
                    distances[neigh] = min(distances[neigh], n_dist + distances[node])
                    heapq.heappush(queue, (n_dist + distances[node], neigh))
        
        return -1 if max(distances.values()) == float('inf') else max(distances.values())
    
if __name__ == "__main__":

    obj = Solution()
    obj.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
