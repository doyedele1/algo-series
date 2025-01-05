from typing import List

# TC: O(k) where k is the size of ops, SC: O(1)
class Solution:
    def max_count(self, m: int, n: int, ops: List[List[int]]) -> int:
        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])
        return m * n