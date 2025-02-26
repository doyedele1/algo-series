from typing import List

# TC: O(n), SC: O(1)
class Solution1:
    def maxSubarrSum(self, nums: List[int]) -> int:
        n = len(nums)
        currSum = 0
        maxSum = float("-inf")

        for i in range(n):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
            if currSum < 0:
                currSum = 0
        return maxSum

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSubarrSum = self.maxSubarrSum(nums)
        minSubarrSum = self.maxSubarrSum([-num for num in nums])
        return max(maxSubarrSum, minSubarrSum)
    
# TC: O(n), SC: O(1)
class Solution2:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        currSum = maxPrefixSum = minPrefixSum = 0

        for i in range(n):
            currSum += nums[i]
            maxPrefixSum = max(maxPrefixSum, currSum)
            minPrefixSum = min(minPrefixSum, currSum)
        return maxPrefixSum - minPrefixSum