'''
    Explanation I: Recursive Solution
        If p and q nodes are empty or null, return True
        If p is not empty, but q is empty, return False
        If p and q values are not equal, return False

        Call isSameTree on the left subtree of p and left subtree of q
        Call isSameTree on the right subtree of p and right subtree of q
        Both must return True, so you can use 'and' for that

        TC: O(p + q) => O(n)
        SC: O(logn) for completely balanced tree, O(n) for completely unbalanced tree
    
    Explanation II: Iterative BFS Solution
        - Use a helper BFS function to copy and save the nodes of p and q into an array
        - Call the function to check if the arrays are equal
    
    Explanation III: Improved Iterative BFS Solution
        - Use a queue which initially has the root of both p and q
        - At each iteration, remove the current node from the deque and then run the checks in the base cases in the recursive solution
        - If the checks are OK, push the child nodes

        TC: O(p + q) => O(n)
        SC: O(logn) for completely balanced tree, O(n) for completely unbalanced tree
'''

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DfsSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        if (not p or not q) or (p.val != q.val): 
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class BfsIterativeSolution:
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
    
class BfsImprovedIterativeSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p and not q: 
                return True
            if (not p or not q) or (p.val != q.val): 
                return False
            else:
                return True
            
        q = deque([(p, q)])

        while q:
            nodeP, nodeQ = q.popleft()
            if not helper(nodeP, nodeQ): 
                return False
            if nodeP:
                q.append((nodeP.left, nodeQ.left))
                q.append((nodeP.right, nodeQ.right))
        return True