from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        q = deque([root])
        
        while q:
            curr = q.popleft()
            
            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)
        return curr.val