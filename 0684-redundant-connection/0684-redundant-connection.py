class UnionFind():

    def __init__(self, n):

        self.parent = [x for x in range(n)]
        self.size = [1] * n
        self.rem_sets = n
    
    def find(self, u):

        root = u
        while(root != self.parent[root]):
            root = self.parent[root]
        
        curr_node = u
        while(curr_node != root):
            temp = self.parent[curr_node]
            self.parent[curr_node] = root
            curr_node = temp
        
        return root
    
    def union(self, u, v):

        root1 = self.find(u)
        root2 = self.find(v)

        if(root1 == root2):
            return True
        
        if(self.size[root1] > self.size[root2]):
            self.size[root1] += self.size[root2]
            self.parent[root2] = root1
        else:
            self.size[root2] += self.size[root1]
            self.parent[root1] = root2

        self.rem_sets -= 1
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        obj = UnionFind(len(edges))
        for u,v in edges:

            if(obj.union(u-1,v-1)):
                return [u,v]
        

            
        
