from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        greaterThanK = set()

        for num in nums:
            if num < k:
                return -1
            elif num > k:
                greaterThanK.add(num)
        return len(greaterThanK)