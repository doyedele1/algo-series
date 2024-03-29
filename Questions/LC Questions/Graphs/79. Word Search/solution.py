'''
    Explanation: Recursive DFS (Backtracking) Solution
        * We can't reuse a character that we've visited before
        So, let's do the backtracking brute-force as a human would do

        word = "ABCCED"
        We check if we have an A in the board since that's the first letter in the word
            Yes, we do. Then we check all possible neighbors of A and check if we have a B

        TC: O(rc * dfs) = O(rc * 4 ^ len(word))
        SC: O(len(word))
'''

from typing import List

# Modifying visited character to a value of # - This is very fast on LC
class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col, index):
            # If the index is at the length of word, it means we've found a word
            if index == len(word): 
                return True
            
            # If we go out of bounds, or if we found the wrong character
            if (row < 0 or row >= rows or col < 0 or col >= cols or word[index] != board[row][col]):
                return False
            
            temp = board[row][col] 
            board[row][col] = '#'
                
            up = dfs(row - 1, col, index + 1)
            down = dfs(row + 1, col, index + 1)
            left = dfs(row, col - 1, index + 1)
            right = dfs(row, col + 1, index + 1)
                
            board[row][col] = temp
            
            return up or down or left or right
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False

# Using hash set to keep track of visited characters
class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(row, col, index):
            # If the index is at the length of word, it means we've found a word
            if index == len(word):
                return True
            
            # If we go out of bounds, or if we found the wrong character, or if the (row, col) position we are at is in the hash set- which means we are visiting the position twice
            if (row < 0 or row >= rows or col < 0 or col >= cols or word[index] != board[row][col] or (row, col) in visited):
                return False
            
            visited.add((row, col))
            # run the recursive function in all 4 adjacent positions
            up = dfs(row - 1, col, index + 1)
            down = dfs(row + 1, col, index + 1)
            left = dfs(row, col - 1, index + 1)
            right = dfs(row, col + 1, index + 1)
            res = up or down or left or right
            # since we are no longer visiting that position, we don't visit that position again, so we can remove it
            visited.remove((row, col))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False