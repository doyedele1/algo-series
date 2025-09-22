from typing import List

# One pass - Hashmap. TC: O(n), SC: O(n)
class Solution1:
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

# Using an array as the frequency counter. TC: O(n), SC: O(1)
class Solution2:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_freq = [0] * 101
        for num in nums:
            nums_freq[num] += 1

        max_freq = 0
        for freq in nums_freq:
            max_freq = max(max_freq, freq)

        total_freq = 0
        for freq in nums_freq:
            if freq == max_freq:
                total_freq += freq
        return total_freq