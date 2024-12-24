'''


    TC: O(nlogn) for sorting
    SC: O(n) for the sorted map
'''

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMinimumSwaps(self, arr: List[int]) -> int:
        n = len(arr)
        minSwaps = 0

        sortedMap = {value: i for i, value in enumerate(arr)}

        sortedArr = sorted(arr)
        visited = [False] * n

        for i in range(n):
            if visited[i] or sortedMap[sortedArr[i]] == i:
                continue

            cycleSize = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = sortedMap[sortedArr[j]]
                cycleSize += 1
            minSwaps += cycleSize - 1
        return minSwaps
    
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0

        while q:
            size = len(q)
            values = []

            for _ in range(size):
                curr = q.popleft()
                values.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            res += self.findMinimumSwaps(values)
        return res