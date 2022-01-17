from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
            
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]: 
                j -= 1
            self.swap(nums, i, j)
            
        self.reverse(nums, i+1)
            
            
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, start):
        end = len(nums) - 1

        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

'''
    Explanation:
        # Brute-force solution:
            - Find out all possible permutations formed by the numbers in the given array
            - Find out which is larger than the given one

            - TC - O(n!) for total possible permutations
            - SC - O(n) since an array is used to store the permutations


        # Most optimal approach - Single Pass Approach
        Pattern to look for
                - If we have input [1,1,5,4,6], res = [1,1,5,6,4]
                - If we have input array [1,1,5,4,1], res = [1,4,1,1,5]
                - Here, we can observe that, looking at the array from behind, anytime our number in array decreses is where we can get the next permutation
        Hence, the following steps will be taken to get our output
        1. Find the point of change
        2. Find the number for substitution, which is going to be the next highest number in the remaining array
            - Then, swap the numbers. Point of change and next highest number in the remaining array
        3. Rearrange the numbers to make the remaining part minimum. We could sort or reverse the remaining part
        4. We then get the next permutation

        TC - O(n)
        SC - O(1)
'''