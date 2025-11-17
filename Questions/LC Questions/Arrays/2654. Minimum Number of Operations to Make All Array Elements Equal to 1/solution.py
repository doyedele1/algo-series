'''
    Explanation:
        Observations:
            * When we replace, we should replace the bigger number with the smaller number (the gcd)
            * gcd(x, 1) = 1. gcd of any number and 1 is 1. So that means to perform the operation, we need a 1 somewhere. 
            Either in nums or a gcd is 1
            * gcd(0, 5) is 5

        Case 1: We have at least a 1 in nums
            nums = [2, 1, 2, 2, 1, 2]
            First operation: Replace nums[0] with gcd(nums[0], nums[1]) = 1, nums = [1, 1, 2, 2, 1, 2]
            Second operation: Replace nums[2] with gcd(nums[1], nums[2]) = 1, nums = [1, 1, 1, 2, 1, 2]
            Third operation: Replace nums[3] with gcd(nums[3], nums[4]) = 1, nums = [1, 1, 1, 1, 1, 2]
            Fourth operation: Replace nums[5] with gcd(nums[4], nums[5]) = 1, nums = [1, 1, 1, 1, 1, 1]

            Minimum number of operations = 4

            This is equivalent to: nums_length - count_of_ones

        Case 2: No 1 in nums
            One thing we need to understand is gcd is associative just like multiplication. (a * b) * c = a * (b * c)
            With this observation, if the gcd of all the elements is not equal to 1, then we can't perform the operation. Hence, we return -1

            [2, 6, 3, 4]
            We need to find the number of operations it takes to form a gcd of 1
            Then, we return operations + (nums_length - 1)
            Example: assume after one operation, [1, 6, 3, 4]. operations = 1. We can then return 1 + (4 - 1) = 4

            But now, how can we get the number of operations?
            We can find the minimum subarray such that the gcd is 1 and then, we can conclude:
                the number of operations = length of minimum subarray - 1
            
            [2, 6, 3, 4]
            Subarray = [2, 6], gcd = 2
            Subarray = [2, 6, 3], gcd = 1, break the loop there

            Subarray = [6, 3], gcd = 3
            Subarray = [6, 3, 4], gcd = 1, break the loop there

            Subarray = [3, 4], gcd = 1

            the minimum_subarray with gcd of 1 is [3, 4]. number of operations = 2 - 1 = 1
            Return: operations + (nums_length - 1) = 1 + (4 - 1) = 4

        Complexities analysis:
            For each subarray: TC: O(n-squared)
            Computing the gcd at each subarray = TC: O(log M) where M is any of the numbers
            TC: O(n-squared log M)
            SC: O(1)
'''

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b):
            while a and b:
                a = a % b
                b, a = a, b
            return max(a, b)

        n = len(nums)
        one_count = 0
        curr_gcd = 0

        for num in nums:
            if num == 1:
                one_count += 1
            curr_gcd = gcd(curr_gcd, num)

        if one_count > 0:
            return n - one_count
        if curr_gcd != 1:
            return -1

        min_sub_len = float("inf")
        for l in range(n):
            curr_gcd = 0
            for r in range(l, n):
                curr_gcd = gcd(curr_gcd, nums[r])
                if curr_gcd == 1:
                    min_sub_len = min(min_sub_len, r - l + 1)
                    break
        return (min_sub_len - 1) + n - 1        