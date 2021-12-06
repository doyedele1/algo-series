import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        if root == None:
            return sum
        
        q = collections.deque([root])
        
        while q:
            curr = q.popleft()
            
            if low <= curr.val <= high:
                sum += curr.val
                
            if curr.left and low <= curr.val:
                q.append(curr.left)
                
            if curr.right and high >= curr.val:
                q.append(curr.right)
                
        return sum