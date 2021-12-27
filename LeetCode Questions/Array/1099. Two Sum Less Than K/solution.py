from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        # [1,8,23,24,33,34,54,75]
        res = -1
        left = 0
        right = len(nums) - 1
        
        while left < right:
            sum = nums[left] + nums[right]
            if sum < k:
                res = max(sum, res)
                left += 1
            else:
                right -= 1
        return res
    
    '''
        TC - O(nlogn)
        SC - O(n) or O(log n)
    '''