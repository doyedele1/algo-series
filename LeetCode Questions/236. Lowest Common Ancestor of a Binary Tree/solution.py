# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
        
        self.ans = None
        return search(root, p, q)

    '''
    Explanation:
    - Perform a postorder traversal on the tree and assign true and false boolean variables to current node that doesn't have the p and q
    - If after our traversal, any of the nodes have at least two true variables, then it means the current node is the lowest common ancestor we are looking for.
    - Remember, a node can be a lca of itself
        T(C) - O(n)
        S(C) - O(n)
    '''