'''
    Explanation:
         r
        [4, 5, 3, 4, 2, 4, 2, 1]
         l

        First iteration: range_min = 4, range_max = 4, r = 1, l = 0 
        Second iteration: range_min = 4, range_max = 5, r = 2, l = 0
        Third iteration: range_min = 3, range_max = 5, r = 3, l = 0
        Fourth iteration: range_min = 3, range_max = 5, r = 4, l = 0
        window_size = 4 - 0 = 4, count = (4*5)//2 = 10
        Fifth iteration: range_min = 2, range_max = 5. Now range_max - range_min > 2, so we do the following:
            count = (window_size * (window_size + 1)) // 2 - to find the number of valid subarray count in the window
            Move l to where r is
                         r
            [4, 5, 3, 4, 2, 4, 2, 1]
                         l
            range_min = 2, range_max = 2

            - Move l backward
                         r
            [4, 5, 3, 4, 2, 4, 2, 1]
                      l
            nums[l] - nums[r] <= 2, so we are good. range_min = 2, range_max = 4

            - Move l backward again
                         r
            [4, 5, 3, 4, 2, 4, 2, 1]
                   l
            nums[l] - nums[r] <= 2, so we are good, range_min = 2, range_max = 4

            - If we try to move l backward again, nums[l] = 5, nums[r] = 2, which is invalid
            window_size = 4 - 2 = 2, count = (2*3)//2 = 3, so we deduct this from the count because we already counted subarray [3,4] the first time before we got an invalid case
            count = 10 - 3 = 7

            - Sixth iteration, range_min = 2, range_max = 4, r = 5, l = 2
            - Seventh iteration, range_min = 2, range_max = 4, r = 6, l = 2
            - Eigth iteration, range_min = 1, range_max = 4, r = 7, l = 2. Now range_max - range_min > 2, so we do the following:
                window_size = 5
                count = (5*6)//2 = 15, update count = 7 + 15 = 22

                Move l to where r is
                                      r
                [4, 5, 3, 4, 2, 4, 2, 1]
                                      l
                range_min = 1, range_max = 1

                - Move l backward
                                      r
                [4, 5, 3, 4, 2, 4, 2, 1]
                                   l
                nums[l] - nums[r] <= 2, so we are good. range_min = 1, range_max = 2

                - If we try to move l backward again, nums[l] = 4, nums[r] = 1, which is invalid
                window_size = 7 - 6 = 1, count = (1*2)//2 = 1, so we deduct this from the count
                count = 22 - 1 = 21

            -  Ninth iteration, r = 8, but we have run out of loop. However, we still need to count subarray [2, 1]
            window_size = 7 - 6 + 1 = 2
            count = (2*3)//2 = 3
            Update count = 21 + 3 = 24

        TC: O(n)
        SC: O(1)
'''
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        count = 0
        right = 0

        range_min = nums[right]
        range_max = nums[right]

        for right in range(n):
            range_min = min(range_min, nums[right])
            range_max = max(range_max, nums[right])

            if range_max - range_min > 2:
                win_size = right - left
                count += (win_size * (win_size + 1)) // 2

                left = right
                range_min = nums[right]
                range_max = nums[right]
                while left > 0 and abs(nums[right] - nums[left - 1]) <= 2:
                    left -= 1
                    range_min = min(range_min, nums[left])
                    range_max = max(range_max, nums[left])

                if left < right:
                    win_size = right - left
                    count -= (win_size * (win_size + 1)) // 2

        win_size = right - left + 1
        count += (win_size * (win_size + 1)) // 2

        return count