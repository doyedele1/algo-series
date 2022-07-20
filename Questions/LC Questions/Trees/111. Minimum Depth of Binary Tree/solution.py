'''
    Explanation I: Recursive Post-Order (DFS) Traversal
        - base case: if no children, i.e. we are at the leaf node: return 1
        - traverse through the children, set min_depth as the minimum between min_depth and recursive min_depth on children
        - return min_depth + 1
        
        - TC: O(n), SC: O(n) worst case, O(log n) best case
        
    Explanation II: Iterative Post-Order (DFS) Traversal
        - Initialize a stack with root and the corresponding depth which is 1
        - Iterate through the stack, pop the current node and push the child nodes to the stack
        - The min_depth is updated at each leaf node
    
        - TC: O(n), SC: O(n)
    
    Explanation III: Iterative BFS
        - Traverse level by level, the first leaf we encounter gives us the minimum depth
        - We do not need to iterate all through the nodes to find all the depths
        - TC: worst case, in a balanced tree, we visit the nodes level by level excluding the bottom level. We visit n/2 nodes. O(n/2) = O(n)
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        children = [root.left, root.right]
        if not any(children): return 1
        
        min_depth = float("inf")
        for child in children:
            if child:
                min_depth = min(min_depth, self.minDepth(child))
        return min_depth + 1

class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        else:
            stack = [(1, root)]
            min_depth = float("inf")
            
        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            
            if not any(children): min_depth = min(depth, min_depth)
            for child in children:
                if child: stack.append((depth + 1, child))
        
        return min_depth


class Solution3:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        else:
            q = deque([(1, root),])
            
        while q:
            depth, root = q.popleft()
            children = [root.left, root.right]
            
            if not any(children): return depth
            for child in children:
                if child: q.append((depth + 1, child))