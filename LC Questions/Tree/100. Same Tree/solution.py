import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive solution
        def helper(p, q):
            if not p and not q:
                return True
            elif (p and not q) or (q and not p) or (p.val != q.val):
                return False
            return helper(p.left, q.left) and helper(p.right, q.right)
        return helper(p, q)
        
        
        
        # Iterative solution
#         def helper(root):
#             if not root:
#                 return 0

#             q = collections.deque([root])
#             res = [root.val]

#             while q:
#                 for i in range(len(q)):
#                     curr = q.popleft()
#                     if curr.left:
#                         q.append(curr.left)
#                         res.append(curr.left.val)
#                     else: res.append(None)
#                     if curr.right:
#                         q.append(curr.right)
#                         res.append(curr.right.val)
#                     else: res.append(None)
#             return res

#         return helper(p) == helper(q)


    '''
        For both recursive and iterative solutions
            TC - O(n)
            SC - memory used by the queue- O(log n) for complete balanced tree, O(n) for complete unbalanced tree
    '''