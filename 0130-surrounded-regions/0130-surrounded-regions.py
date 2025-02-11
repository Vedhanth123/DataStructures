class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = '#'  # Mark as safe
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # Explore 4 directions
                dfs(r + dr, c + dc)
        
        # Step 1: Mark border-connected 'O's
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)


        for x in range(rows):
            for y in range(cols):

                if(board[x][y] == 'O'):
                    board[x][y] = 'X'
                if(board[x][y] == '#'):
                    board[x][y] = 'O'
        
        
            