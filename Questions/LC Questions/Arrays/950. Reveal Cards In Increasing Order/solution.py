'''
    Explanation: Fill and Skip Approach
        2      3       5       7       11      13      17
        
        0      1       2       3        4       5       6
        2      s       3       s        5       s       7
        2      s       3       11       5       s       7
        2      13      3       11       5       s       7
        2      13      3       11       5       17      7

        TC: O(nlogn), SC: O(n)
'''

from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        deck.sort()
        q = deque(range(N))
        res = [0] * N

        for num in deck:
            i = q.popleft()
            res[i] = num
            if q:
                q.append(q.popleft())
        return res