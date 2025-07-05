from typing import List
from collections import Counter

# TC: O(n), SC: O(n)
class Solution1:
    def findLucky(self, arr: List[int]) -> int:
        arrCount = Counter(arr)
        res = -1

        for num, freq in arrCount.items():
            if num == freq:
                res = max(res, num)
        return res

# TC: O(n), SC: O(C) where C = 501
class Solution2:
    def findLucky(self, arr: List[int]) -> int:
        freq = [0] * 501
        for num in arr:
            freq[num] += 1

        for i in range(500, 0, -1):
            if freq[i] == i:
                return i
        return -1