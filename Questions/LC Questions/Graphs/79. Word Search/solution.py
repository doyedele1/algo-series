'''
    Explanation: Recursive DFS Backtracking Solution
        - We can't reuse any characters that have been used
        
        dfs function:
            - If the index is the same as the length of word, we return True
            - Else if, if we are in of bounds and we see a character we are looking for,
                - We set our cell in the board to None
                - We run a recursive dfs function on all four directions
                    - And return True if the recursive dfs function is true
                - We set our cell back to the letter it was
            - Else. we return False
        
        main function:
            - Iterate through the board
                - If the dfs function returns true, that means we've found the word on the board, so return True
            - Return false
        
        - TC: O(rc * dfs) = O(rc * 4 ^ len(word))
        - SC: O(len(word))
'''

from typing import List

# Modifying visited character to a value of None
class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, index):
            if index >= len(word): return True
            
            elif 0 <= row < rows and 0 <= col < cols and board[row][col] == word[index]:
                temp = board[row][col]
                board[row][col] = None
                
                # If any of the directions return true, we return true as our result
                if dfs(row + 1, col, index + 1) or dfs(row - 1, col, index + 1) or dfs(row, col + 1, index + 1) or dfs(row, col - 1, index + 1):
                    return True
                board[row][col] = temp
            
            return False
            
        rows, cols = len(board), len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False

# Using hash set to keep track of visited characters - Doesn't submit sometimes on LC
class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(row, col, index):
            if index == len(word): return True
            
            if (row < 0 or row >= rows or col < 0 or col >= cols or word[index] != board[row][col] or (row, col) in visited): return False
            
            visited.add((row, col))
            res = dfs(row - 1, col, index + 1) or dfs(row + 1, col, index + 1) or dfs(row, col - 1, index + 1) or dfs(row, col + 1, index + 1)
            visited.remove((row, col))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False