'''
    Explanation:
        Naive Solution
            - Can we consider the possible areas for each pair of heights?
            - For each pair, we check the area by multiplying the width to the height without spill over? The height is the bottleneck here and we need to consider the minimum height between the pair.
            - TC: O(n-squared) --> (n(n-1))/2 for evaluating areas of each pair, SC: O(1)
        
        
        Optimal Solution
            - Can we reduce the number of times we find the possible areas for every pair of the heights which is caused by the minimum height in each pair?
            - Yes, we can. We can have two pointers at both endpoints and perform the area of the ractangle. When the height is minimum for a left pointer, we can move to the pointer to the right and when the height is minimum for a right pointer, we move the pointer to the left to the right. This is done to look for the next possible maximum height. 
            - TC: O(n), SC: O(1)
'''

# Naive Solution
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         ans = 0
        
#         for i in range(len(height)):
#             for j in range(i + 1, len(height)):
#                 area_of_rectangle = (j - i) * (min(height[i], height[j]))
#                 ans = max(ans, area_of_rectangle)
                
#         return ans

# Optimal Solution
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i = 0
        j = len(height) - 1
        
        while i < j:
            area_of_rectangle = (j - i) * (min(height[i], height[j]))
            ans = max(ans, area_of_rectangle)
            
            if height[i] < height[j]:
                i += 1
            else: j -= 1
                
        return ans