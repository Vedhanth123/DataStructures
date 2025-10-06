class UnionFind():
    
    def __init__(self, n):
        
        self.parent = [x for x in range(n)]
        self.size = [1] * n
    
    def find(self, u):
        
        if(self.parent[u] != self.parent[u]):
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return
        
        if(self.size[root_u] < self.size[root_v]):
            self.size[root_v] += self.size[root_u]
            self.parent[root_u] = root_v
        else:
            self.size[root_u] += self.size[root_v]
            self.parent[root_v] = root_u


