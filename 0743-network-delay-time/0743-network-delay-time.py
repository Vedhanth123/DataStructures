from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        distances = [float('inf')] * n
        distances[k-1] = 0

        graph = defaultdict(list)

        for src, dest, weight in times:
            graph[src-1].append((weight, dest-1))
        
        priority_queue = [(0,k-1)]


        visited = set()

        while(priority_queue):

            weight, node = heapq.heappop(priority_queue)
            curr_distance = distances[node]

            if(node in visited):
                continue

            visited.add(node)

            for new_weight, neighbour in graph[node]:
                # visited.add((curr_distance + weight, neighbour))
                    distances[neighbour] = min(distances[neighbour],curr_distance + new_weight)
                    heapq.heappush(priority_queue, (curr_distance + new_weight, neighbour))

        if(len(visited) != n):
            return -1
        else:
            return max(distances)

if __name__ == "__main__":
    obj = Solution()
    obj.networkDelayTime(times = [[1,2,1],[2,3,2],[1,3,2]], n = 3, k = 1)

