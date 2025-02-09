'''
    Explanation:
        Bad pairs = Total pairs - Good pairs
        
        Total pairs = n(n - 1) / 2

        Good pair definition:
        i < j
        (j - i) = nums[j] - nums[i]
        Hence, j - nums[j] = i - nums[i]

        Dry run:
        [1, 2, 4, 5, 3]

        Use a hashmap. key is i - nums[i] and value is the frequency that i - nums[i] has occured

        First iteration,
        i - nums[i] = -1
        good_pair = 0
        freqCount = {-1: 1}

        Second iteration,
        i - nums[i] = -1
        good_pair = 1
        freqCount = {-1: 2}

        Third iteration,
        i - nums[i] = -2
        good_pair = 1
        freqCount = {-1: 2, -2: 1}

        Fourth iteration,
        i - nums[i] = -2
        good_pair = 2
        freqCount = {-1: 2, -2: 2}

        Fifth iteration,
        i - nums[i] = 1
        good_pair = 2
        freqCount = {-1: 2, -2: 2, 1: 1}

        Total pairs = n(n - 1) / 2 = 5(5 - 1) / 2 = 10
        Good pairs = 2

        Bad pairs = 10 - 2 = 8

        TC: O(n)
        SC: O(n)
'''
from typing import List
from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        freqCount = defaultdict(int)
        good_pairs = 0
        
        for i, num in enumerate(nums):
            key = i - num
            if key in freqCount:
                good_pairs += freqCount[key]
            freqCount[key] += 1
        
        bad_pairs = n * (n - 1) // 2 - good_pairs
        return bad_pairs