from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # start from the end and compare the two numbers there to find the decreasing sequence
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # we have found the decreasing number. We need to swap the numbers. j >= 0 so as not to go out of the bounds
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
            - Here, we can observe that, looking at the array from behind, anytime our number in array decreases is where we can get the next permutation
        Hence, the following steps will be taken to get our output for input array [1,1,5,4,1]
        1. Find the point of change = 1
        2. Find the number for substitution to the right, which is going to be the next highest number after the point of change number in the remaining array = 4
            - Then, swap the numbers - Point of change and next highest number in the remaining array --> [1,4,5,1,1]
        3. Rearrange the numbers to make the remaining part minimum. We could sort or reverse the remaining part
        4. We then get the next permutation

        TC - O(n) where n is the size of the array
        SC - O(1) as we are not using any extra space

        1 1 5 4 6 --> 1 1 5 6 4
        1 1 5 4 1 --> 1 4 1 1 5
'''