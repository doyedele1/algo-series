'''
    Explanation:
        Naive Solution
        - Can we consider the possible areas for each pair of heights?
        - For each pair, we check the area by multiplying the width to the height without spill over? The height is the bottleneck here and we need to consider the minimum height between the pair.
        
        
        Optimal Solution

'''

from typing import List
# Naive Solution
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_amount = 0
        
#         for i in range(len(height)):
#             for j in range(i + 1, len(height)):
#                 area_of_rectangle = (j - i) * (min(height[i], height[j]))
#                 max_amount = max(max_amount, area_of_rectangle)
                
#         return max_amount