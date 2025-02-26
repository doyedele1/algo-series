'''
    Explanation:
        Let's observe some things:
        
        If we have [, , , , o] where o is for the count of odd subarray summing to that index, to get the total odd count,
        it is the odd count at that index + the odd count before that index

        If we have [, , , , e] where e is for the count of even subarray summing to that index, to get the total odd count,
        it is just the even count before that index

        With this little observation, we can run through an example:
        [3, 2, 4, 1, 2, 5]

        First iteration:
            prefixSum = 3
            totalOddCount = 1
            evenCount = 1
            oddCount = 1
        
        Second iteration:
            prefixSum = 5
            totalOddCount = 2
            evenCount = 1
            oddCount = 2

        Third iteration:
            prefixSum = 9
            totalOddCount = 3
            evenCount = 1
            oddCount = 3
        
        Fourth iteration:
            prefixSum = 10
            totalOddCount = 6
            evenCount = 2
            oddCount = 3

        Fifth iteration:
            prefixSum = 12
            totalOddCount = 9
            evenCount = 3
            oddCount = 3
        
        Sixth iteration:
            prefixSum = 17
            totalOddCount = 12
            evenCount = 3
            oddCount = 4

        TC: O(n)
        SC: O(1)
'''
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        prefixSum = totalOddCount = oddCount = 0
        evenCount = 1

        for i in range(n):
            prefixSum += arr[i]

            if prefixSum % 2:
                totalOddCount = (totalOddCount + evenCount) % MOD
                oddCount += 1
            else:
                totalOddCount = (totalOddCount + oddCount) % MOD
                evenCount += 1
        return totalOddCount