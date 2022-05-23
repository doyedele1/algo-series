'''
    Explanation I: Brute-force solution
        We sum every subarray elements and find the maximum sum
        TC: O(n^2), SC: O(n)
    
    Explanation II: Kadane's algorithm - we keep track of the maximum sum at every index
        Initialize the maxSum and maxAtEveryIndex variables to be nums[0]
        Loop from the 2nd number to the end of the list
            maxAtEveryIndex is the maximum of nums[i] and maxAtEveryIndex + nums[i]
            maxSum is the maximum of maxSum and maxAtEveryIndex
        Return maxSum
        
        TC: O(n), SC: O(1)

        [-2,1,-3,4,-1,2,1,-5,4]
        maxSum = -2, maxAtEveryIndex = -2
        maxSum = 1, maxAtEveryIndex = 1
        maxSum = 1, maxAtEveryIndex = -2
        maxSum = 4, maxAtEveryIndex = 4
        maxSum = 4, maxAtEveryIndex = 3
        maxSum = 5, maxAtEveryIndex = 5
        maxSum = 6, maxAtEveryIndex = 6
        maxSum = 6, maxAtEveryIndex = 1
        maxSum = 6, maxAtEveryIndex = 5
'''

class Solution1:
    def maxSubArray(nums):
        maxSum = 0

        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                maxSum = max(maxSum, sum)
        return maxSum

class Solution2:
    def maxSubArray(nums):
        maxSum = maxAtEveryIndex = nums[0]

        for i in range(1, len(nums)):
            maxAtEveryIndex = max(nums[i], maxAtEveryIndex + nums[i])
            maxSum = max(maxSum, maxAtEveryIndex)
        return maxSum


# print(maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
# print(maxSubArray2([1]))
# print(maxSubArray2([5,4,-1,7,8]))