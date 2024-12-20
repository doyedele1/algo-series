from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseArr(self, arr):
        i, j = 0, len(arr) - 1

        while i < j:
            arr[i].val, arr[j].val = arr[j].val, arr[i].val
            i += 1
            j -= 1
        return arr

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        level = 0

        while q:
            n = len(q)
            level_nodes = []

            for _ in range(n):
                curr = q.popleft()
                level_nodes.append(curr)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            if level % 2 == 1:
                self.reverseArr(level_nodes)
            
            level += 1

        return root