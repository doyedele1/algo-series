'''
    TC - O(n) where n is the number of nodes in the binary tree
    SC - O(n) because the maximum amount of space utilized by the recursion stack would be n where n could be the height of a skewed binary tree
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def search(node, p, q):
            if node == None:
                return None
            
            leftSearch = search(node.left, p, q)
            rightSearch = search(node.right, p, q)
            current = node == p or node == q
            
            if (leftSearch and rightSearch) or (current and leftSearch) or (current and rightSearch):
                self.ans = node
                return self.ans
            return leftSearch or rightSearch or current
        
        return search(root, p, q)