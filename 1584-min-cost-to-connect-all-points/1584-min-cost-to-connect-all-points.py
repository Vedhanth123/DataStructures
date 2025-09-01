class UnionFind():

    def __init__(self, n):
        
        self.parent = [x for x in range(n)]
        self.size = [1] * n
        self.rem_sets = n
    
    def find(self, u):

        root = self.parent[u]

        while(root != self.parent[root]):
            root = self.parent[root]
        
        curr = u
        while(curr != self.parent[curr]):
            temp = self.parent[curr]
            self.parent[curr] = root
            curr = temp

        return root
    
    def union(self, u, v):

        root1 = self.find(u)
        root2 = self.find(v)

        if(root1 == root2):
            return True

        if(self.size[root1] >= self.size[root2]):
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

        else:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        
        self.rem_sets -= 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = []

        for i in range(len(points)):

            x1 = points[i][0]
            y1 = points[i][1]

            for j in range(i+1,len(points)):

                x2 = points[j][0]
                y2 = points[j][1]

                dist = abs(x2-x1) + abs(y2-y1)
                heapq.heappush(edges, (dist, i,j))
        

        uf = UnionFind(len(points))
        answer = 0

        while(uf.rem_sets != 1):

            curr = heapq.heappop(edges)
            if(uf.find(curr[1]) != uf.find(curr[2])):
                uf.union(curr[1], curr[2])
                answer += curr[0]
        
        return answer
