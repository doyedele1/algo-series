# TC: O(n), SC: O(1)
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        consecutive = 0

        for char in s:
            if char == "1":
                consecutive += 1
                # res += consecutive or use below since res can be very large
                res = (res + consecutive) % MOD
            else:
                consecutive = 0
        return res