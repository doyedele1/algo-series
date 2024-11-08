from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)

        prefixXor = [0] * n
        prefixXor[0] = nums[0]

        for i in range(n):
            prefixXor[i] = prefixXor[i - 1] ^ nums[i]
        
        res = []
        mask = (1 << maximumBit) - 1

        for i in range(n - 1, -1, -1):
            res.append(prefixXor[i] ^ mask)
        return res