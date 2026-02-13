class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        min_heap = [(grid[0][0], 0,0)]
        min_path = [[float('inf') for x in range(len(grid))] for x in range(len(grid))]

        min_path[0][0] = grid[0][0]

        while(min_heap):

            curr_cost, r,c = heapq.heappop(min_heap)

            if r == N - 1 and c == N - 1:
                return curr_cost

            for n_r,n_c in [(0,1), (0,-1),(1,0),(-1,0)]:
                n_x = n_r + r
                n_y = n_c + c

                if(0 <= n_x < len(grid) and 0 <= n_y < len(grid[0])):

                    new_time = max(curr_cost, grid[n_x][n_y])

                    if(new_time < min_path[n_x][n_y]):
                        min_path[n_x][n_y] = new_time
                        heapq.heappush(min_heap, (new_time, n_x,n_y))

        return -1



