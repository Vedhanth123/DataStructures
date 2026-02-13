class UnionFind():

    def __init__(self, n):
        self.parent = [x for x in range(n+1)]
        self.size = [1] * (n+1)
    
    def find(self, u):
        if(self.parent[u] != u):
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if(root_u == root_v):
            return 

        if(self.size[root_u] < self.size[root_v]):
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
        

class Solution:
    def longestConsecutive(self, nums):

        numSet = set(nums)
        if(not len(numSet)):
            return 0

        obj = UnionFind(len(numSet))
        hashmap = {v:i for i,v in enumerate(numSet)}

        for num in numSet:

            if(num+1 in numSet):
                obj.union(hashmap[num], hashmap[num+1])
            
        
        if(obj.size):
            return max(obj.size)
        else:
            return 0


if __name__ == "__main__":

    obj = Solution()
    obj.longestConsecutive(nums = [100,4,200,1,3,2])
