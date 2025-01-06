from typing import List

# We want this prefixSum [17, 14, 9]
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        m = len(shifts)

        prefixSum = [0] * m
        prefixSum[0] = sum(shifts)

        for i in range(1, m):
            prefixSum[i] = prefixSum[i - 1] - shifts[i - 1]

        res = []
        for i in range(n):
            shift = prefixSum[i]

            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            res.append(new_char)
        return ''.join(res)