class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # BFS function to mark safe border-connected 'O's
        def bfs(r, c):
            queue = deque([(r, c)])
            while queue:
                x, y = queue.popleft()
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                    board[x][y] = 'T'  # Temporarily mark safe cells
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        queue.append((x+dx, y+dy))

        for x in (0,len(board)-1):
            for y in range(len(board[0])):
                if(board[x][y] == 'O'):
                    bfs(x,y)
        
        for x in range(len(board)):
            for y in (0,len(board[0])-1):
                if(board[x][y] == 'O'):
                    bfs(x,y,)
        
        print(board)
        for x in range(len(board)):
            for y in range(len(board[0])):
                if(board[x][y]== 'O'):
                    board[x][y] = 'X'
                elif(board[x][y] == 'T'):
                    board[x][y] == 'O'
    



            