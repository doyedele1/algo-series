from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        tallest = 0
        res = []
        j = len(heights) - 1
        
        while j >= 0:
            if heights[j] > tallest:
                tallest = heights[j]
                res.append(j)
            j -= 1
            
        res.reverse()
        return res