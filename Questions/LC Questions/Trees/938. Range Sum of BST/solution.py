from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def range_sum_BST_bfs(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        if not root:
            return 0
        
        q = deque([root])
        
        while q:
            curr = q.popleft()
            
            if low <= curr.val <= high:
                res += curr.val
                
            if curr.left and curr.val > low:
                q.append(curr.left)
                
            if curr.right and  curr.val < high:
                q.append(curr.right)
                
        return res