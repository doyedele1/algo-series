'''
    Explanation I: Brute-Force Solution
        - Find every possible triplet combination of the numbers in the array using three nested loops, sum every combination and check if it equals to the target
        
        TC: O(n^3)
        SC: O(1)

    Explanation II: Sorting Method
        [12, 3, 4, 1, 6, 9]
        - Sort the array --> [1, 3, 4, 6, 9, 12]
        - Take the three pointers. i starts from the first element, j starts from the next element after i, k starts at the end of the array
            [1, 3, 4, 6, 9, 12]
            i   j           k
            - Sum nums[j] + nums[k] except where j = k
                - If sum is less than target, increment j
                - If sum is greater than target, decrement k
                - If sum is equal to target, print the triplet
        - Move the i pointer

        TC: O(n^2)
        SC: O(1)
    
    Explanation III: Hashing Method
        - Start pointer i from 0 to len(nums) - 2
        - Create an empty hash map
        - Traverse from j = i + 1 to len(nums) - 1
        - Declare sum = arr[i] + arr[j]
            - If target - sum is present in the hash map,
                - Return arr[i], arr[j] and target - sum as the combination
            - Else, insert arr[j] in the hash map and proceed
        
        [12, 3, 4, 1, 6, 9]
        i    j
        hashmap = {0: 3, 1: 4, 2: 1, 3: 6, 4: 9, 5: 12}

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
        
# print(Solution1.tripletSum([0, -1, 2, -3, 1], -2))

class Solution2:
    def tripletSum(nums, target) -> List[int]:
        res = []
        nums.sort()

        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    res.append((nums[i], nums[j], nums[k]))
                    return res # not printing out all combinations
                elif nums[i] + nums[j] + nums[k] < target: j += 1
                else: k -= 1
        return False

print(Solution2.tripletSum([0, -1, 2, -3, 1], -2))