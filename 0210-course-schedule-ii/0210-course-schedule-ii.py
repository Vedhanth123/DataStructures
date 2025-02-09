class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}

        for dest,src in prerequisites:

            adj[src].append(dest)
            indegree[dest] += 1
        
        courses_left = numCourses
        order_of_courses = []

        queue = deque([])

        for key,val in indegree.items():
            if(val == 0):
                queue.append(key)
        
        while(queue):

            for x in range(len(queue)):
                curr = queue.popleft()
                order_of_courses.append(curr)
                courses_left -= 1

                for neighbours in adj[curr]:

                    indegree[neighbours] -= 1
                    if(indegree[neighbours] == 0):
                        queue.append(neighbours)
        
        if(courses_left == 0):
            return order_of_courses
        else:
            return []