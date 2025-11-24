'''
    Explanation I: Traversal
        Number of operations required to increase num to the next multiple of 3 is 3 - (num % 3)
        Number of operations required to decrease num to the nearest multiple of 3 is (num % 3)

        Then choose the option that requires fewer operations

        TC: O(n), SC: O(1)

    Explanation II:
        [1, 2, 3, 4]
        For 1, we need one operation to make it 0 (subtract) which is divisible by 3
        For 2, we need one operation to make it 3 (add) which is divisible by 3
        For 3, zero operation is required since 3 is divisible by 3
        For 4, we need one operation to make it 3 (subtract) which is divisible by 3

        Hence, all we need to check is if num has any remainder (1 or 2), then we increment the number of operations.
        If no remainder (already divisible by 3), we do nothing

        TC: O(n), SC: O(1)
'''
from typing import List

class Solution1:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res += min(num % 3, 3 - num % 3)
        return res
    
class Solution2:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if num % 3:
                res += 1
        return res