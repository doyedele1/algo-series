'''
    Explanation:
        Observation: We don't care about the order of each domino
        domino [1, 2] is equivalent to domino [2, 1]

        With this observation, we can do the following:
        - Convert each domino to a canonical form (10a + b). This way, we can easily know which dominoes are equal
        - We can use a hashmap or dictionary to then calculate the count of equal domino pairs
        - Or we can use an array of length 100. Since the largest number is 9, then (10*9 + 9) = 99

        TC: O(n)
        SC: O(100) which is O(1)
'''

from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = [0] * 100
        res = 0

        for domino in dominoes:
            val1 = domino[0]
            val2 = domino[1]

            if val1 <= val2:
                canonical_val = (10 * val1) + val2
            else:
                canonical_val = (10 * val2) + val1
            
            res += counts[canonical_val]
            counts[canonical_val] += 1

        return res