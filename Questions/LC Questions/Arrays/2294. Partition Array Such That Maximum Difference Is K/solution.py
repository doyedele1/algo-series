from typing import List

# TC: O(nlogn), SC: O(1)
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        start_of_valid_subsequence = nums[0]
        count = 1

        for i in range(1, n):
            if nums[i] - start_of_valid_subsequence > k:
                start_of_valid_subsequence = nums[i]
                count += 1
        return count