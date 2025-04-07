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

    Explanation III: Binary Search
        We need a list of list that represents the increasing subsequences of different lengths
        We need a list that represents the longest increasing subsequence

        - Then, we need to greedily append the new element to an increasing subsequence which will maximize the length of increasing subsequence
        - If two lists turn out to be of the same length, we can discard the list with a higher end value

        Dry run: [8, 10, 9, 4, 2, 6, 3, 5, 9, 5]
        listOfList = [[8]]
        lis = [8]

        listOfList = [[8], [8, 10]]
        lis = [8, 10]

        listOfList = [[8], [8, 9]]
        lis = [8, 9]

        listOfList = [[4], [8, 9]]
        lis = [4, 9]

        listOfList = [[2], [8, 9]]
        lis = [2, 9]

        listOfList = [[2], [2, 6]]
        lis = [2, 6]

        listOfList = [[2], [2, 3]]
        lis = [2, 3]

        listOfList = [[2], [2, 3], [2, 3, 5]]
        lis = [2, 3, 5]

        listOfList = [[2], [2, 3], [2,3, 5], [2, 3, 5, 9]]
        lis = [2, 3, 5, 9]

        listOfList = [[2], [2, 3], [2, 3, 5], [2, 3, 5, 9]]
        lis = [2, 3, 5, 9]

        We can then return the length of lis

        We are applying binary search lower_bound to find the index with the value greater than the number we want to append

        TC: O(nlogn), SC: O(n)
'''

from typing import List
from bisect import bisect_left

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = 1 + dp[j]
        return max(dp)
    
class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for num in nums:
            idx = bisect_left(lis, num)
            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num
        return len(lis)