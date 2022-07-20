from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p = deque(preorder)
        n = len(preorder)
        
        # building a hashmap to store value and its index
        lookup = {}
        for i, v in enumerate(inorder):
            lookup[v] = i
        
        
        def helper(start, end):
            # if there are no elements to construct the tree
            if start > end:
                return None
            else:
                cand = p.popleft()
                root = TreeNode(cand)
                middle = lookup[cand]
                # building left and right subtree excluding the root
                root.left = helper(start, middle - 1)
                root.right = helper(middle + 1, end)
                
                return root
            
        return helper(0, n-1)
    
    
    '''
        TC - O(n) to build the lookup hashmap and the tree
        SC - O(n) for the memory used by the lookup hashmap and the tree storage
    '''