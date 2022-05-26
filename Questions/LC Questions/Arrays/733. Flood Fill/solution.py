'''        
        TC - O(n)
        SC - O(n)
'''

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(i, j, newColor, starting_point):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != starting_point or starting_point == newColor:
                return
            
            image[i][j] = newColor

            dfs(i, j-1, newColor, starting_point) # bottom
            dfs(i, j+1, newColor, starting_point) # top
            dfs(i-1, j, newColor, starting_point) # left
            dfs(i+1, j, newColor, starting_point) # right
    
        if not image: return None
        
        starting_point = image[sr][sc]        
        dfs(sr, sc, newColor, starting_point)
        return image