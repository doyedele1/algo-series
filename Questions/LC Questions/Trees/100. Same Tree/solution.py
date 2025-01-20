'''
    Explanation I: Recursive Solution
        - If p and q nodes are not none and their values are equal, do the same for the child nodes recursively

        - TC: O(p + q) => O(n)
        - SC: O(log n) for completely balanced tree, O(n) for completely unbalanced tree
    
    Explanation II: Iterative BFS Solution
        - Use a helper function to copy and save the nodes of p and q into an array
        - Call the helper function to check if the arrays are equal
    
    Explanation III: Improved Iterative BFS Solution
        - Use a queue which initially has the root
        - At each iteration, remove the current node from the deque and then run the checks in the base cases
        - If the checks are OK, push the child nodes

        TC: O(p + q) => O(n)
        SC: O(log n) for completely balanced tree, O(n) for completely unbalanced tree
'''

from collections import deque
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

class BfsIterative:
    def bfs(self, root):
        if not root:
            return 0
        
        q = deque([root])
        arr = [root.val]

        while q:
            size = len(q)

            for _ in range(size):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                    arr.append(curr.left.val)
                else:
                    arr.append(None)
                if curr.right:
                    q.append(curr.right)
                    arr.append(curr.right.val)
                else:
                    arr.append(None)
        return arr

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.bfs(p) == self.bfs(q)
    
class Solution3:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p and not q: 
                return True
            if (not p or not q) or (p.val != q.val): 
                return False
            else:
                return True
            
        queue = deque([(p, q)])
        while queue:
            nodeP, nodeQ = queue.popleft()
            if not helper(nodeP, nodeQ): return False
            if nodeP:
                queue.append((nodeP.left, nodeQ.left))
                queue.append((nodeP.right, nodeQ.right))
        return True