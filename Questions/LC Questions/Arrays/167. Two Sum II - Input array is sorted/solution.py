from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            twoSum = numbers[l] + numbers[r]
            if twoSum == target:
                return [l + 1, r + 1]
            elif twoSum < target:
                l += 1
            else:
                r -= 1
        # in case no solution
        return [-1, -1]