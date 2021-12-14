import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if root == None: return res
        
        next_level = collections.deque([root])
        
        while next_level:
            curr_level = next_level
            next_level = collections.deque()
            
            while curr_level:
                node = curr_level.popleft()
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            res.append(node.val)
    
        return res