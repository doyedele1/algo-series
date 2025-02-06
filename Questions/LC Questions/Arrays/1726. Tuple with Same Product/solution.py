'''
    Explanation:
        Observation I:
            If given [2, 9, 3, 6], to find the number of valid tuples, we check how many valid tuples we have:
            
            We know we can get 8 different valid tuples because 2 * 9 = 3 * 6 which is a * b = c * d and this can be arranged 8 times.
            (2, 9) and (3, 6)                   (3, 6) and (2, 9)
            (2, 9) and (6, 3)                   (6, 3) and (2, 9)
            (9, 2) and (3, 6)                   (3, 6) and (9, 2)
            (9, 2) and (6, 3)                   (6, 3) and (9, 2)

        Observation II:
            If given a larger nums array, [1, 2, 9, 6, 3, 18], to find the number of valid tuples,
            
            For value 18, we have 3 valid pairs:
            [1, 18], [2, 9] and [6, 3]
            Now, we know that to find the valid tuples, we only need to pick 2 pairs and not 3.
            So we find the number of ways to pick 2 pairs from possible 3 and that is 3C2 which is 3.

            Hence, we know we can get 8 * 3 different valid tuples = 24

        Observation III:
            Now that we have those two observations, how can we know the number of valid pairs from the nums array
            We create a frequency count for the product of each num in nums and track the count

            For [2, 9, 6, 3],
            product                 count
            2*9=18                    1
            2*6=12                    1
            2*3=6                     1
            9*6=54                    1
            9*3=27                    1
            6*3=18                    2

            If count = 1, then that means we can't form 2 pairs that will make a * b = c * d.
            Mathemetically, we need count to be at least 2

            In the example of [2, 9, 6, 3], count > 1 just once.
            So the number of ways to arrange [2, 9, 6, 3] in valid pairs is 8 * 2C2 = 8

            And that is the solution.

        TC: O(n-squared) for creating the frequency count hash table
        SC: O(n-squared) because the hash table contains the product of every num in nums
'''

from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)

        productFreq = defaultdict(int)
        tuples = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                productFreq[product] += 1

        for count in productFreq.values():
            if count > 1:
                tuples += 8 * (count * (count - 1) // 2)
        return tuples