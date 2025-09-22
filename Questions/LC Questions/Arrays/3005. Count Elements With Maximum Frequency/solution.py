from typing import List

# One pass - Hashmap. TC: O(n), SC: O(n)
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_freq = {}
        max_freq = 0
        total_freq = 0

        for num in nums:
            nums_freq[num] = nums_freq.get(num, 0) + 1
            freq = nums_freq[num]

            if freq > max_freq:
                max_freq = freq
                total_freq = freq
            elif freq == max_freq:
                total_freq += freq
        return total_freq