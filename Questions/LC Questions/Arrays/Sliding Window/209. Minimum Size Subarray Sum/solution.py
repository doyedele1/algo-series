'''
    Explanation: Sliding Window
        [1, 3, 2, 2, 3], target = 7
         l
         r
        Observation: Since we have positive integers, we know that the sum will keep increasing
        
        We do two things:
            - Keep moving r until sum >= target
            - Then, compress the window by moving l until sum < target or sum >= target
        When you are done with this, then you can find the subarray len by doing (r - l + 2)

        [1, 3, 2, 2, 3], target = 7
         l
         r
        First iteration: sum = 1
        Second iteration: sum = 4
        Third iteration: sum = 6
        
        Fourth iteration: sum = 8. Now sum is greater than or equal to 7, We compress the window. Sum becomes 7
        Sum is still greater than or equal to 7. We compress the window. Sum becomes 4
        After the fourth iteration, r = 4, l = 2
    
        Fifth iteration: sum = 7. Now sum is greater than or equal to 7. We compress the window. Sum becomes 5
        After the fifth iteration, r = 5, l = 3
    
        TC: O(n)
        SC: O(1)
'''

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        sum = 0
        res = float("inf")

        # Empty array, then return 0
        if n == 0:
            return 0

        while r < n:
            sum += nums[r]

            if sum >= target:
                while sum >= target:
                    sum -= nums[l]
                    l += 1
                res = min(res, r - l + 2)
            r += 1

        return 0 if res == float("inf") else res