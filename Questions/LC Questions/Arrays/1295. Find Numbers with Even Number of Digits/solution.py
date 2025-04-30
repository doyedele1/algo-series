from typing import List

# TC: O(N⋅logM), SC: O(1) where M is the maximum number of digits in nums which will be in the maximum number
class Solution1:
    def hasEvenDigitCount(self, num: int) -> bool:
        digit_count = 0

        while num:
            digit_count += 1
            num //= 10
        return digit_count & 1 == 0

    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if self.hasEvenDigitCount(num):
                count += 1
        return count

# TC: O(N), SC: O(1)
class Solution2:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if (num >= 10 and num <= 99) or (num >= 1000 and num <= 9999) or num == 100000:
                count += 1

        return count