'''
    Explanation:
        We can generate subarrays of size n-squared
        We are doing a ton of repeated work by getting the sum of all the single subarrays

        We will use a hashmap where the key is the prefix_sum and the value is the count of how many times that prefix_sum occurs
        - If currSum is k at any point, then we will increment the count as we have found a subarray with sum equals to k
        - Also, if currSum - k is in the hashmap, then it means we have found a subarray with sum equals to k

        Example: [1,-1,1,1,1,1], k = 1

        First iteration:
            currSum = 1
            diff = 0
            count = 1
            prefixSum = {1: 1}

        Second iteration:
            currSum = 0
            diff = -1
            count = 1
            prefixSum = {1: 1, 0: 1}

        Third iteration:
            currSum = 1
            diff = 0
            count = 3
            prefixSum = {1: 2, 0: 1}
        
        Fourth iteration:
            currSum = 2
            diff = 1
            count = 5
            prefixSum = {1: 2, 0: 1, 2: 1}
        
        Fifth iteration:
            currSum = 3
            diff = 2
            count = 6
            prefixSum = {1: 2, 0: 1, 2: 1, 3: 1}
        
        Sixth iteration:
            currSum = 4
            diff = 3
            count = 7
            prefixSum = {1: 2, 0: 1, 2: 1, 3: 1, 4: 1}

        TC: O(n)
        SC: O(n)
'''

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = defaultdict(int)
        count = currSum = 0

        if n == 0:
            return 0

        for i in range(n):
            currSum += nums[i]

            if currSum == k:
                count += 1
            
            diff = currSum - k
            if diff in prefixSum:
                count += prefixSum[diff]

            prefixSum[currSum] += 1
        
        return count