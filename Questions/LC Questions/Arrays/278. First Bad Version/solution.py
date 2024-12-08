# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        res = n
        low, high = 1, n

        while low <= high:
            mid = low + ((high - low) // 2)
            if isBadVersion(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res