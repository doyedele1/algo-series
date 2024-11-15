from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n - 1

        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1
        
        res = r
        while l < r:
            while r < n and arr[l] > arr[r]:
                r += 1

            res = min(res, r - l - 1)

            l += 1
            if arr[l] < arr[l - 1]:
                break
        return res