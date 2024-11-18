'''
    [5, 7, 1, 4], k = 3


'''

from typing import List

class Solution1:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        
        if k == 0:
            return res
        
        for i in range(n):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                    res[i] += code[j % n]
            elif k < 0:
                for j in range(i - 1, i - 1 - abs(k), -1):
                    res[i] += code[j % n]
        return res
    
class Solution2:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        
        if k == 0:
            return res

        l = 0
        currSum = 0
        for r in range(n + abs(k)):
            currSum += code[r % n]

            if r - l + 1 > abs(k):
                currSum -= code[l % n]
                l = (l + 1) % n

            if r - l + 1 == abs(k):
                if k > 0:
                    res[(l - 1) % n] = currSum
                elif k < 0:
                    res[(r + 1) % n] = currSum

        return res