from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        for target in [tops[0], bottoms[0]]:
            missingTop, missingBottom = 0, 0

            for i in range(n):
                if not (tops[i] == target or bottoms[i] == target):
                    break
                if tops[i] != target:
                    missingTop += 1
                if bottoms[i] != target:
                    missingBottom += 1
                if i == n - 1:
                    return min(missingTop, missingBottom)
        return -1