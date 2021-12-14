# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def search(node):
            if node == None: return None
            if p == None or q == None: return None
            
            leftSearch = search(node.left)
            rightSearch = search(node.right)
            current = node == p or node == q
            
            if (current and leftSearch) or (current and rightSearch) or (leftSearch and rightSearch):
                self.ans = node
                return
            return current or leftSearch or rightSearch
        
        search(root)
        return self.ans
        