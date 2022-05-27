'''
    Explanation I: Brute-Force Solution
        - Find every possible triplet combination of the numbers in the array using three nested loops, sum every combination and check if it equals to the target
        
        TC: O(n^3)
        SC: O(1)

    Explanation II: Using sorting
'''

from typing import List

class Solution1:
    def tripletSum(nums, target) -> List[int]:
        res = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == target:
                        res.append((nums[i], nums[j], nums[k]))
        return res
        
print(Solution1.tripletSum([0, -1, 2, -3, 1], -2))

class Solution2:
    def tripletSum(nums, target) -> List[int]:
        res = []

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            diff = target - nums[i]
            while j < k:
                if nums[j] + nums[k] == diff:
                    res = print("Triplet is", nums[i], ", ", nums[j], ", ", nums[k])
                    return res
                elif nums[j] + nums[k] < diff: j += 1
                else: k -= 1

# print(Solution2.tripletSum([0, -1, 2, -3, 1], -2))