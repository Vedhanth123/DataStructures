class UnionFind():

    def __init__(self, n):

        self.parent = [x for x in range(n)]
        self.rank = [0] * n
    
    def find(self, u):

        if(self.parent[u] != self.parent[u]):
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if(self.rank[root_u] < self.rank[root_v]):
            self.parent[root_u] = root_v
        elif(self.rank[root_u] > self.rank[root_v]):
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1 
    