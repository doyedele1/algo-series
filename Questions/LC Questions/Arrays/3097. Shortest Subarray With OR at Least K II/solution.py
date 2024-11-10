from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def updateFreq(bitFreq, number, val):
            for i in range(32):
                if number & (1 << i):
                    bitFreq[i] += val

        def getNumber(bitFreq):
            number = 0
            pow = 1
            for i in range(32):
                if bitFreq[i] > 0:
                    number += pow
                pow *= 2
            return number

        if k == 0:
            return 1

        n = len(nums)
        shortest = float('inf')
        left = 0
        right = 0
        currOR = 0
        bitFreq = [0] * 32

        while right < n:
            updateFreq(bitFreq, nums[right], 1)
            currOR |= nums[right]

            # Resize window
            while left <= right and currOR >= k:
                shortest = min(shortest, right - left + 1)
                updateFreq(bitFreq, nums[left], -1)
                currOR = getNumber(bitFreq)
                left += 1
            right += 1

        return -1 if shortest == float('inf') else shortest