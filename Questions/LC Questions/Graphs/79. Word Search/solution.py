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

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, index):
            if index >= len(word): return True
            
            elif 0 <= row < rows and 0 <= col < cols and board[row][col] == word[index]:
                temp = board[row][col]
                board[row][col] = None
                
                # If any of the directions return true, we return true as our result
                if dfs(row + 1, col, index + 1) or dfs(row - 1, col, index + 1) or dfs(row, col + 1, index + 1) or dfs(row, col - 1, index + 1): return True
                board[row][col] = temp
            
            return False
            
        rows, cols = len(board), len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False