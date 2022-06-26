'''
    Explanation I: 
        - To capture the surrounded regions, can we capture everything except the unsurrounded regions?
            - To know unsurrounded regions, we know the region is connected to the border
            - We can run recursive dfs on every unsurrounded region and mark the visited regions to U
            
        - After we are done with the board, we iterate over the board again
            - If we encounter a U which is for unsurrounded regions, we change it to an O
            - If we encounter a O which is for the surrounded regions only, we capture it by flipping it to X
        
        - TC: O(n) where n is the number of cells in the board
        - SC: O(n), we would use space in the recursive call stack

    Explanation II: Simpler Approach, but not More Optimized
        - Use a variable seen to know if any cell is connected to a border of O
        - Iterate over the elements not on the border

        X   X   X   O   X   X
        X   O   X   O   O   X
        X   X   O   X   X   O
        X   O   O   X   X   X
        X   X   X   X   X   X

        seen = False
        - At row 1, col 1,
            - The region isn't connected to a border of O on all four directions, so seen = False
            - Call a marked function to mark the O to X
        - At row 1, col 3,
            - The region is connected to a border of O on all four directions, so seen = True
            - Row 1, col 4 has already been visited and is an O, so we need a visited array to keep track of visited nodes
        - At row 2, col 2, the region calls another O at row 3, col 2 and that also calls another O at row 3 col 1, seen = False
            - Call a marked function to mark the O to X

        - TC: O(m * n)
        - SC: O(m * n)
'''

class Solution1:
    def solve(self, board: List[List[str]]) -> None:
        # Do not return anything, modify board in-place instead.
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c):
            # if we go out of bounds and we are only capturing an O
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
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

class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        
        if rows <= 1 or cols <= 1:
            return
        
        visited = set()

        def dfs(r, c):
            if r < 0 or r > rows -  1 or c < 0 or c > cols - 1 or board[r][c] != 'O' or (r, c) in visited:
                return

            if r <= 0 or r >= rows - 1 or c <= 0 or c >= cols - 1:
                seen = True

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        def markedDfs(r, c):
            if r < 0 or r > rows -  1 or c < 0 or c > cols - 1 or board[r][c] != 'O':
                return
            
            board[r][c] = 'X'
            markedDfs(r + 1, c)
            markedDfs(r - 1, c)
            markedDfs(r, c + 1)
            markedDfs(r, c - 1)

        for row in range(1, rows):
            for col in range(1, cols):
                if board[row][col] == 'O' and (row, col) not in visited:
                    seen = False
                    dfs(row, col)

                    if seen == False:
                        markedDfs(row, col)
                    
                    seen = True