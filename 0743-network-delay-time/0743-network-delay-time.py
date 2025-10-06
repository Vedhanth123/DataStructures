from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
<<<<<<< HEAD

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
=======
        

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

>>>>>>> 90c7b9b5254aeb00514c716832a6d75954eaf279
