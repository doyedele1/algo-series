# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(root):
            nonlocal res
            
            if root == None: return -1 # returning the height if root is null
            left = dfs(root.left)
            right = dfs(root.right)
            
            res = max(res, 2 + left + right)
            
            return 1 + max(left, right)
        
        dfs(root)
        return res
        
        
        '''
            Brute-force solution:
                - Take every single node in the tree and consider it as the topmost node in that diameter.
                - Find the max diameter running through each node in the tree
                - T(C) - O(n-squared)
                
            Optimal solution: Bottom-up approach, to cut out the repeated work
                - What we need --> Diameter, Height
                - If no left or right node, left_height or right_height is -1
                    - Diameter = left_height + right_height + 2, running through the node
                    - Height = 1 + max(left_height, right_height), from the node and below
                - T(C) - O(n)
        '''