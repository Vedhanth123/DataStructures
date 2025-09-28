class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        # dijkstra is of 3 steps

        # 1) initialize all the nodex = infintiy distance except the source node which is 0
        # 2) Also take set for checked whether this node is visited or not
        # 3) user priority queue to pick the minimum weight node

        # 1) convert the graph to adjacency list 
        g = defaultdict(list)
        for u,v,w in times:
            g[u].append((v,w))
        
        distances = {x:float('inf') for x in range(1, n+1)}

        distances[k] = 0

        visited = set()

        queue = [(0,k)]
        while(queue):
            w,u = heapq.heappop(queue)

            if(u in visited):
                continue

            visited.add(u)

            for v,w in g[u]:
                distances[v] = min(distances[v], distances[u] + w)
                heapq.heappush(queue,(distances[v],v))

        result = max(list(distances.values()))
        return result if result != float('inf') else -1


