'''
    Explanation:
        Let's make some observations:
            nums = [8,3], maxOperations = infinity: We can divide 8 and 3 any number of times to give [1,1,...1,1,1,1]. Maximum value here is 1
            nums = [8,3], maxOperations = 0: We don't need to do any division. Maximum value here is 8
            Then we can say our answer is in the range of 1 to max(nums)

            For example, nums = [8,3], maxOperations = 2,
            We can divide the array the first time as [5,3,3] and second time as [2,3,3,3], max is 3
            Again, we can divide the array the first time as [4,4,3] and second time as [2,2,4,3], max is 4
            Again, we can divide the array the first time as [5,3,3] and second time as [5,1,2,3], max is 5
            Here we can see a pattern, our answer will be in the range of 1 to 8, yes, but our answer can never be 1 or 2.

            With these observations, we can do a binary search on the possible range of values
            nums = [8,3,5], maxOperations = 3
            
            Can we find the number of operations it will take us to divide each element in the nums array and we will get the mid value as the maximum value?
            Formula for that: ceil((element - mid) / mid) only when element > mid
            Formula to find mid: mid = low + ((high - low) // 2) - to prevent overflow
            
            First iteration: nums = [8,3,5], low = 1, high = 8, res = infinity, mid = low + ((high - low) // 2) = 4
            noOfOperationsNeeded for element 8: element 8 >= mid 4, so ceil((8 - 4) / 4) = 1
            noOfOperationsNeeded for element 3: element 3 < mid 4, so zero number of operations
            noOfOperationsNeeded for element 5: element 5 >= mid 4, so ceil((5 - 4) / 4) = 1
            Total = 1 + 0 + 1 = 2 operations needed which is less than the maxOperations, so we can update res = mid and high = mid - 1

            Second iteration: nums = [8,3,5], low = 1, high = mid - 1 = 3, res = 4, mid = low + ((high - low) // 2) = 2
            noOfOperationsNeeded for element 8: element 8 >= mid 2, so ceil((8 - 2) / 2) = 3
            noOfOperationsNeeded for element 3: element 3 >= mid 2, so ceil((3 - 2) / 2) = 1
            noOfOperationsNeeded for element 5: element 5 >= mid 2, so ceil((5 - 2) / 2) = 2
            Total = 3 + 1 + 2 = 6 operations needed which is greater than the maxOperations (too high), so can never give us the result, but we can update low = mid + 1

            Third iteration: nums = [8,3,5], low = mid + 1 = 3, high = 3, res = 4, mid = low + ((high - low) // 2) = 3
            noOfOperationsNeeded for element 8: element 8 >= mid 3, so ceil((8 - 3) / 3) = 2
            noOfOperationsNeeded for element 3: element 3 >= mid 3, so ceil((3 - 3) / 3) = 0
            noOfOperationsNeeded for element 5: element 5 >= mid 3, so ceil((5 - 3) / 3) = 1
            Total = 2 + 0 + 1 = 3 operations needed which is equal to the maxOperations, so we can update res = mid and high = mid - 1

            Fourth iteration: nums = [8,3,5], low = 3, high = mid - 1 = 2, res = 3. Since low > high, then we can stop the loop and return res
            
        TC: O(nlogr) where n is the size of nums array and r is the maximum value in the nums array
        SC: O(1)
'''

import math
from typing import List

class Solution:
    def canAssign(self, nums, maxValueExpected, noOfOperationsNeeded) -> bool:
        count = 0
        for num in nums:
            if num > maxValueExpected:
                count += math.ceil((num - maxValueExpected) / maxValueExpected)
        return count <= noOfOperationsNeeded

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        res = float("inf")
        low, high = 1, max(nums)

        while low <= high:
            mid = low + ((high - low) // 2)
            if self.canAssign(nums, mid, maxOperations):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res