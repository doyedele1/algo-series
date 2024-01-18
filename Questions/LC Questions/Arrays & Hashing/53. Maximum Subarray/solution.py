'''
    Explanation I: Brute-force solution
        - We sum every subarray elements and find the maximum sum
        
        TC: O(n^2), SC: O(n)

    Explanation II: Sliding Window
        - The trick is that if we find a negative currSum, we can reassign the currSum to 0. 
        Why? A negative value plus a positive number reduces the positive number and then we can just take the positive number as the currSum.
        [-2,1,-3,4,-1,2,1,-5,4] --> currSum = 0, maxSum = -2
        currSum = -2, maxSum = -2
        currSum = 0, currSum = 1, maxSum = 1
        currSum = -2, maxSum = 1
        currSum = 0, currSum = 4, maxSum = 4
        currSum = 3, maxSum = 4
        currSum = 5, maxSum = 5
        currSum = 6, maxSum = 6
        currSum = 1, maxSum = 6
        currSum = 5, maxSum = 6

        TC: O(n), SC: O(1)
    
    Explanation III: Kadane's Algorithm - we keep track of the maximum sum at every index
        - Initialize the maxSum and maxAtEveryIndex variables to be nums[0]
        - Loop from the 2nd number to the end of the list
            maxAtEveryIndex is the maximum of nums[i] and maxAtEveryIndex + nums[i]
            maxSum is the maximum of maxSum and maxAtEveryIndex
        - Return maxSum

        [-2,1,-3,4,-1,2,1,-5,4]
        maxAtEveryIndex = -2, maxSum = -2
        maxAtEveryIndex = 1, maxSum = 1
        maxAtEveryIndex = -2, maxSum = 1
        maxAtEveryIndex = 4, maxSum = 4
        maxAtEveryIndex = 3, maxSum = 4
        maxAtEveryIndex = 5, maxSum = 5
        maxAtEveryIndex = 6, maxSum = 6
        maxAtEveryIndex = 1, maxSum = 6
        maxAtEveryIndex = 5, maxSum = 6

        TC: O(n), SC: O(1)
'''

# It returns Time Limit Exceeded on LC
class Solution1:
    def maxSubArray(nums):
        maxSum = nums[0]

        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                maxSum = max(maxSum, currSum)
        return maxSum

class Solution2:
    def maxSubArray(nums):
        maxSum, currSum = nums[0], 0
        
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(maxSum, currSum)
        return maxSum

class Solution3:
    def maxSubArray(nums):
        maxSum = maxAtEveryIndex = nums[0]

        for i in range(1, len(nums)):
            maxAtEveryIndex = max(nums[i], maxAtEveryIndex + nums[i])
            maxSum = max(maxSum, maxAtEveryIndex)
        return maxSum





# print(maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
# print(maxSubArray2([1]))
# print(maxSubArray2([5,4,-1,7,8]))