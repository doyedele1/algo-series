from typing import List

# TC: O(n), SC: O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(2):
            for n in nums:
                res.append(n)
        return res

        # or just do this -> return 2 * nums