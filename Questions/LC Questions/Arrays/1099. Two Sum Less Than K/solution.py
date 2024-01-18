'''
    Solution 1:
        TC - O(nlogn)
        SC - O(n) or O(log n)

    Solution 2:
        [34,23,1,24,75,33,54,8]
        60
        
        TC - O(m + n) where m is the range of values in the nums array while n is the size of the nums array
        SC - O(m) where m helps to count each value in the nums array
'''

from typing import List

# Naive solution
class Solution1:
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


# Optimal solution
class Solution2:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        res = -1
        low = 1
        high = 1000
        count_freq = [0] * 1001
        for num in nums:
            count_freq[num] += 1
            
        while low <= high:
            if low + high >= k or count_freq[high] == 0:
                high -= 1
            else:
                if count_freq[low] > (0 if low < high else 1):
                    res = max(res, low + high)
                low += 1
        return res