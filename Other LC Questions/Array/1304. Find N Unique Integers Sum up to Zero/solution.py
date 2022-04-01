from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        divisor, remainder = n // 2, n % 2
        if remainder != 0: res = [0]
        else: res = []
        
        for i in range(1, divisor + 1):
            res.append(-i)
            res.append(i) 
        return res