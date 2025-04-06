'''
    Explanation I: Brute-force -> Backtracking
        nums = [5, 8, 7, 1, 9]
        We can either choose any number to be part of the subsequence since:
        [5] can be the longest subsequence
        [8] can be the longest subsequence
        [7] can be the longest subsequence
        [1] can be the longest subsequence
        [9] can be the longest subsequence

        With this, we can then generate all the subsequences and filter out the subsequences who are in increasing order

        TC: O(2^n), SC: O(n)

    Explanation II: Dynamic Programming
        nums = [5, 8, 7, 1, 9]

        We can create a dp array that represents the length of the increasing subsequence
        dp = [1, 1, 1, 1, 1]

        With this dp array, we can come to an observation that:
        When i = 1 and j = 0
        if nums[i] > nums[j] and dp[i] <= dp[j]:
            dp[i] = 1 + dp[j]
        
        Why will this condition work?
        It will work because for nums[i] > nums[j] and dp[i] <= dp[j], it means we have an increasing subsequence
        If at any index, dp = 2, then it means we can form only two increasing subsequence at that index

        At the end of the iterations, the dp array will have the longest increasing subsequence which is the maximum value in the dp array

        Added knowledge for follow-up:
        If we want to find the subsequence that gives us the longest increasing subsequence, we use the dp array
        dp = [1, 2, 2, 1, 3]
        - We loop from the end of the array and find the number at the index that gives the longest length which is 3. number 9
        - then we check for the next biggest number in the dp array which is 2. number 7
        - then we check for the next biggest number in the dp array which is 1. number 5
        [5, 7, 9] is that subsequence!

        TC: O(n-squared), SC: O(n)
'''
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = 1 + dp[j]
        return max(dp)