from typing import List
from collections import Counter

# TC: O(N), SC: O(K) - to store K results
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits_count = Counter(digits)
        res = []

        for num in range(100, 999, 2):
            hundred = num // 100
            ten = (num // 10) % 10
            unit = num % 10

            required_counts = Counter([hundred, ten, unit])

            possible = True
            for digit, required_count in required_counts.items():
                if digits_count[digit] < required_count:
                    possible = False
                    break
            
            if possible:
                res.append(num)
        return res