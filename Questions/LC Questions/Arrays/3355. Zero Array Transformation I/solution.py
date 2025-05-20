'''
    Explanation:
        nums = [1, 0, 2, 1, 2], queries = [[0, 2], [1, 3], [0, 4], [4, 4]]

        Instead of decrementing the values, can we increment the values instead?
        So we can start from [0, 0, 0, 0, 0] and increment based on the queries

        First iteration: [0, 2]
        [1, 1, 1, 0, 0]

        Second iteration: [1, 3]
        [1, 2, 2, 1, 0]

        Third iteration: [0, 4]
        [2, 3, 3, 2, 1]

        Fourth iteration: [4, 4]
        [2, 3, 3, 2, 2]

        Now, to know if we will have a zero array, we need to check if final value at every index is greater than or equal to the nums at the index
        final value = [2, 3, 3, 2, 2]
        nums = [1, 0, 2, 1, 2]
        2 is greater than or equal to 1
        3 is greater than or equal to 0
        3 is greater than or equal to 2
        2 is greater than or equal to 1
        2 is greater than or equal to 2
        
        Hence we can return true

        TC: O(QN), SC: O(N)
        This could throw a TLE, since Q can be 10^5 and N can be 10^5. QN = 10^10 which is greater than 10^8

        So we should think about another solution
        Let's see if we can use a difference array

        nums = [1, 0, 2, 1, 2]
        diff = [0, 0, 0, 0, 0, 0] last number is a dummy value

        Condition:
        Query: increase (i, j, val), then
        diff[i] += val
        diff[j + 1] -= val
        
        val in our case is 1

        Dry run:
        nums = [1, 0, 2, 1, 2], queries = [[0, 2], [1, 3], [0, 4], [4, 4]]
        diff = [0, 0, 0, 0, 0, 0]

        First iteration: [0, 2]
        [1, 0, 0, -1, 0, 0]

        Second iteration: [1, 3]
        [1, 1, 0, -1, -1, 0]

        Third iteration: [0, 4]
        [2, 1, 0, -1, -1, -1]

        Fourth iteration: [4, 4]
        [2, 1, 0, -1, 0, -2]

        We can get the actual array by finding the cumulative of the diff array
        diff = [2, 3, 3, 2, 2, 0] -> again, the last 0 is a dummy value

        We can observe that the diff array is the same as the final value we got in the first solution
        Then we can do the comparisons to see if we can form a zero array

        TC: O(Q + N), SC: O(N)
'''

from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)

        diff = [0] * (n + 1)

        for query in queries:
            i = query[0]
            j = query[1]

            diff[i] += 1
            diff[j + 1] -= 1
        
        cumulative = 0
        for i in range(n):
            cumulative += diff[i]
            if cumulative < nums[i]:
                return False
        return True