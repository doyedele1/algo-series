'''
    Explanation:
        - maxLeft = height[left], maxRight = height[right]
        
        - If maxLeft < maxRight:
            - Move left pointer and update the maxLeft and res
        - Else:
            - Move right pointer and update the maxRight and res

        TC: O(n) where n is the size of the height array
        SC: O(1), no extra data structure is used
'''

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        res, left, right = 0, 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
        return res