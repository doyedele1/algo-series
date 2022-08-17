'''
    Explanation: Recursive DFS Backtracking Solution
        - We can't reuse any characters that have been used
        
        backtrack function:
            Base cases:
                - If the index is the same as the length of word, we return True
                - If we are out of bounds we return false
                - If we see a character we are not looking for, we return false
                - If we see the same character twice, we return false
            - Add the current position to the set
            - Recursively call the backtrack function on all four directions
            - Remove the position from the set
            - Return res
        
        main function:
            - Iterate through the board
                - If the backtrack function returns true, that means we've found the word on the board, so return True
            - Return false
        
        - TC: O(rc * backtrack) = O(rc * 4 ^ len(word))
'''


from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # positions = set()
        
        def backtrack(r, c, i):
            if i >= len(word): return True
            
            elif 0 <= r < rows and 0 <= c < cols and board[r][c] == word[i]:
                temp = board[r][c]
                board[r][c] = None
                
                if backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1): return True
                board[r][c] = temp
            
            return False
            
            # If any of the directions return true, we return true as our result
            # We remove the position we just added, since we are no longer visiting that position
            
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0): return True
                
        return False