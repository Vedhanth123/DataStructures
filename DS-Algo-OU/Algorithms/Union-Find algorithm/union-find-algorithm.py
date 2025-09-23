class UnionFind():

    def __init__(self, n): # -> takes the no. of elements

        # we need parent array and size array
    
        # parent array will basically answer questions like -> this is my parent
        self.parent = list(range(n)) # initially there are no new parents

        # size says how many are below me (will become irrelevant as the captains will change)
        self.size = [1] * n

        self.num_components = n

        print(self.parent)
        print(self.size)

    def find(self, u):

        # we will use a temporaray variable to store the parent of the u
        root = u

        # we will check if the u is the parent (meaning if the u is the root of the Union Find. If it is then we will return it else we will find it)
        while(root != self.parent[root]):
            root = self.parent[root]

        curr_node = u
        while(curr_node != root):
            temp = self.parent[curr_node]
            self.parent[curr_node] = root
            curr_node = temp

        return root

    def union(self, p, q):

        # fetching the parents of p and q
        root1 = self.find(p)
        root2 = self.find(q)

        # checking if both the parents are same
        if(root1 == root2):
            return

        # now checking the sizes of the parents
        if(self.size[root1] > self.size[root2]):
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        
        self.num_components -= 1


obj = UnionFind(5)
