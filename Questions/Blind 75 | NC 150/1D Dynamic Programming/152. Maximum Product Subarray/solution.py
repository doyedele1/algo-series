from typing import List

'''
    Explanation I: Brute-Force Solution - not accepted on LeetCode
        - We can go through each element and for each element, we accumulate the products of contiguous subarrays starting from that element to subsequent elements as we iterate through them.
        - We need to multiply the current number with the accumulated product to get the product of numbers up to the current number.
        
        - TC: O(n^2), SC: O(1)
    
    Explanation II: Dynamic Programming
        - Let's look at these patterns:
            - [1, 2, 3] all positive numbers --> our product will keep increasing
            - [-1, -2, -3] all negative numbers --> the sign will keep alternating. i.e. -1, 2, -6. However, we know that (-2, -3) subarray is our solution which gives 6.
            - We need to keep track of the minimum as well as the maximum at every index
                - [-1, -2, -3]
                    - Maximum product subarray of (-1, -2) is 2 and the minimum is -2
                    - Maximum product subarray of (-1, -2, -3) is 6 and the minimum is -6
                    - Now if we add -4 to the array, maximum product subarray is 24 and the minimum is -24
                    - Now if we replace -4 with +4 in the array, maximum product subarray = 24 and the minimum is -24
                    
            - Edge case: If we have a zero number in the array. -6 * 0 = 0, 6 * 0
                - Every time we get a zero value, we can reset the max and min to 1
                
        - Another example:
            [2,3,-2,4], maxProduct = 2, maxAtEveryIndex = 2, minAtEveryIndex = 2
            temp = 2, maxAtEveryIndex = 6, minAtEveryIndex = 3, maxProduct = 6
            temp = 6, maxAtEveryIndex = -2, minAtEveryIndex = -12, maxProduct = 6
            temp = -2, maxAtEveryIndex = 4, minAtEveryIndex = -48, maxProduct = 6
        
        - TC: O(n), SC: O(1)
'''

class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        maxProduct = nums[0]
        
        for i in range(len(nums)):
            accumulator = 1
            for j in range(i, len(nums)):
                accumulator *= nums[j]
                maxProduct = max(maxProduct, accumulator)
                
        return maxProduct
class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = maxAtEveryIndex = minAtEveryIndex = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            # if num == 0: --> no need for this condition
            #     maxAtEveryIndex, minAtEveryIndex = 1, 1
            #     continue
            
            temp = num * maxAtEveryIndex
            maxAtEveryIndex = max(num, max(num * maxAtEveryIndex, num * minAtEveryIndex))
            
            minAtEveryIndex = min(num, min(temp, num * minAtEveryIndex))
            
            maxProduct = max(maxProduct, maxAtEveryIndex)
            
        return maxProduct

# print(maxProduct([2,3,-2,4]))
# print(maxProduct([-2,0,-1]))