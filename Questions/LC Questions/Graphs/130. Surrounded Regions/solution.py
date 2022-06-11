'''
    Explanation I: 
        - To capture the surrounded regions, can we capture everything except the unsurrounded regions?
            - To know unsurrounded regions, we know the region is connected to the border

'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O':
                return
            
            board[r][c] = 'U'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for row in range(rows):
            for col in range(cols):
                # run a dfs on every unsurrounded region. i.e every region connected to the border
                if board[row][col] == 'O' and (row in [0, rows - 1] or col in [0, cols - 1]):
                    dfs(row, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                    
                if board[row][col] == 'U':
                    board[row][col] = 'O'