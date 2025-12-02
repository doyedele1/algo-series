'''
    Explanation:
        [3, 1, 4, 2]

        - Find the sum, if no remainder, return 0

        Total % p = remainder
        * when we remove a subarray, we need that subarray to have a remainder of the remainder value above

        - At every index, let's know the smallest subarray we need to remove.
        - Take index 2 for example,
            curr_sum = 8. But we don't care about this value, we only care about the remainder of the curr_sum. So curr_sum = 8 % 6 = 2
            But we want this remainder to be 4, so that we can remove it

        - This is the math: curr_sum - x = remainder where x is the prefix_sum_to_remove
        x = curr_sum - remainder
        - In our example, x = 2 - 4 = -2. That doesn't make sense. So we can offset this value by adding p. 
        x = curr_sum - remainder + p

        Next, how do we get those prefixes. We can use a hashmap (remainder of the prefix sums: last_index).
        

        TC: O(n) where n is the length of nums array
        SC: O(n). In the worst case, the hash map could store up to n different remainders
'''
from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p

        if remainder == 0:
            return 0

        res = len(nums)
        curr_sum = 0
        remainder_to_idx = {0: -1}

        for i, num in enumerate(nums):
            # prefix_sum_to_remove = curr_sum - remainder
            curr_sum = (curr_sum + num) % p # we added % to avoid integer overflow
            prefix_sum_to_remove = (curr_sum - remainder + p) % p # we added % to avoid integer overflow
            if prefix_sum_to_remove in remainder_to_idx:
                length = i - remainder_to_idx[prefix_sum_to_remove]
                res = min(res, length)
            remainder_to_idx[curr_sum] = i

        return -1 if res == len(nums) else res