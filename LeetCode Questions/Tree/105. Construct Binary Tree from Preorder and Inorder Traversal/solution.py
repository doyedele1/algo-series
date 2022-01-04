import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        p = collections.deque(preorder)
        n = len(preorder)
        
        lookup = {v:i for i, v in enumerate(inorder)}
        
        def helper(start, end):
            if start > end:
                return None
            else:
                cand = p.popleft()
                root = TreeNode(cand)
                middle = lookup[cand]
                root.left = helper(start, middle - 1)
                root.right = helper(middle + 1, end)
                return root
            
        return helper(0, n-1)
    
    
    '''
        TC - O(n)
        SC - O(n) for the lookup
    '''