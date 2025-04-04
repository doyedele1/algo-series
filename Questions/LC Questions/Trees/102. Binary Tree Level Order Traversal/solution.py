from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC: O(n), SC: O(n)
class Solution:
    def levelOrder(self, root):
        res = []
        q = deque([root])
        
        if not root:
            return []
        
        while q:
            level_elements = []
            
            for _ in range(len(q)):
                curr = q.popleft()
                level_elements.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level_elements)
            
        return res