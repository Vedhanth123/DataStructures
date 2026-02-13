class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}
        
        # convert the prerequisites array to adjacent matrix
        for dest, src in prerequisites:

            adj[src].append(dest)
            indegree[dest] += 1
        

        courses_left = n

        queue = deque([])

        for key,val in indegree.items():
            if(val == 0):
                queue.append(key)
        
        while(queue):

            for x in range(len(queue)):
                curr = queue.popleft()
                courses_left -= 1

                for neighbours in adj[curr]:
                    indegree[neighbours] -= 1
                    if(indegree[neighbours] == 0):
                        queue.append(neighbours)

        return courses_left == 0            
