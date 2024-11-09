'''
    Explanation:
    [2,3,4,7] maximumBit = 3

    2^3^4^7^k
    2^3^4^k
    2^3^k
    2^k
    We don't know the values of k in the four queries, but we know k has to be a value that will make each query return the maximum number (all 1s)

    The maximum number = 2^maximumBit - 1 or (1<<maximumBit) - 1
    When maximumBit is 3, maximumNumber = 7 = 111
    When maximumBit is 2, maximumNumber = 3 = 11

    So, for the first query, 2^3^4^7^7 = 5 (and this is the correct answer for k)
    For the second query, 2^3^4^7 = 2
    For the third query, 2^3^7 = 6
    For the fourth query, 2^7 = 5
    So, we return [5,2,6,5]

    We can calculate the prefixXor and store it in an array or calculate the xor as we go through the numbers in nums
    We are iterating from the end of nums, because the first query has xor that is calculated after iterating through all the numbers 2^3^4^7^7

    TC: O(n + m). O(n) for calculating the prefixXor, and O(m) for iterating through the numbers to find k
    SC: O(n) for solution1 and O(1) for solution2
'''

from typing import List

class Solution1:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)

        prefixXor = [0] * n
        prefixXor[0] = nums[0]
        for i in range(n):
            prefixXor[i] = prefixXor[i - 1] ^ nums[i]
        
        res = []
        mask = (1<<maximumBit) - 1
        for i in range(n-1, -1, -1):
            res.append(prefixXor[i] ^ mask)
        return res
    
class Solution2:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefixXor = 0
        for n in nums:
            prefixXor ^= n
        
        res = []
        mask = (1<<maximumBit) - 1
        for n in reversed(nums):
            res.append(prefixXor ^ mask)
            prefixXor ^= n
        return res