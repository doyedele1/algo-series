'''
    Explanation I: Brute-Force Solution

    Explanation II: Using sorting
'''

from typing import List

class Solution1:
    def tripletSum(nums, target) -> List[int]:
    
        # Fix the first element as nums[i]
        for i in range(0, len(nums) - 2):
    
            # Fix the second element as nums[j]
            for j in range(i + 1, len(nums) - 1):
                
                # Now look for the third number
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == target:
                        print("Triplet is", nums[i], ", ", nums[j], ", ", nums[k])
                        return True
        
        # If we reach here, then no triplet was found
        return False

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

print(Solution2.tripletSum([0, -1, 2, -3, 1], -2))