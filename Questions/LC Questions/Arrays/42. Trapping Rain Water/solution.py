'''
    Explanation:
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        
        l = 0, r = 11, lMax = 0, rMax = 0, res = 0
        
        first iteration:
            l = 1, r = 11, lMax = 0, rMax = 0, res = 0
        second iteration:
            l = 1, r = 10, lMax = 0, rMax = 1, res = 0
        third iteration:
            l = 2, r = 10, lMax = 1, rMax = 1, res = 0
        fourth iteration:
            l = 3, r = 10, lMax = 1, rMax = 1, res = 1
        3 9 1 2 1
        3 8 1 2 2
        3 7 1 2 2
        4 7 2 2 2
        5 7 2 2 3
        6 7 2 2 5
        7 7 2 2 6
'''

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = 0, 0
        res = 0
        
        while l < r:
            # Get the lowest bounded height from the two pointers indexes
            if height[l] < height[r]:
                if height[l] >= lMax: lMax = height[l]
                else: res += lMax - height[l]
                l += 1
            else:
                if height[r] >= rMax: rMax = height[r]
                else: res += rMax - height[r]
                r -= 1
        
        return res