'''
    Explanation I: Recursive Solution
        - If p and q nodes are not none and their values are equal, do the same for the child nodes recursively

        - TC: O(p + q) => O(n)
        - SC: O(log n) for completely balanced tree, O(n) for completely unbalanced tree
    
    Explanation II: Iterative BFS Solution
        - Use a helper function to cop and save the nodes of p and q into an array
        - Call the helper function to check if the arrays are equal
    
    Explanation III: Improved Iterative BFS Solution
        - Use a queue which initially has the root
        - At each iteration, remove the current node from the deque and then run the checks in the base cases
        - If the checks are OK, push the child nodes

        - TC: O(p + q) => O(n)
        - SC: O(log n) for completely balanced tree, O(n) for completely unbalanced tree
'''

import collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases
        if not p and not q: return True
        if (not p or not q) or (p.val != q.val): return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root: return 0
            
            q = collections.deque([root])
            res = [root.val]
            
            while q:
                for i in range(len(q)):
                    curr = q.popleft()
                    if curr.left:
                        q.append(curr.left)
                        res.append(curr.left.val)
                    else: res.append(None)
                    if curr.right:
                        q.append(curr.right)
                        res.append(curr.right.val)
                    else: res.append(None)
            return res
        
        return helper(p) == helper(q)

class Solution3:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p and not q: return True
            if (not p or not q) or (p.val != q.val): return False
            return True
            
        queue = collections.deque([(p, q)])
        while queue:
            nodeP, nodeQ = queue.popleft()
            if not helper(nodeP, nodeQ): return False
            if nodeP:
                queue.append((nodeP.left, nodeQ.left))
                queue.append((nodeP.right, nodeQ.right))
        return True