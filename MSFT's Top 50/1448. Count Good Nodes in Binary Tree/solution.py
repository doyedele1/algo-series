'''
    Explanation I: PreOrder (DFS) Traversal - Recursive
        - From the root node, check if it is greater than the maximum value seen so far, increment result
        - Update the maximum value seen so far
        - Go to the left child next, check if it is greater than the maximum value seen so far by recursively calling the dfs function on the left subtree and passing the node.left and the maximum value seen so far
        - Go to the right child next, check if it is greater than the maximum value seen so far by recursively calling the dfs function on the right subtree and passing the node.right and the maximum value seen so far
        
        - TC: O(n) where n is the number of nodes
        - SC: O(n) where n is the height of the tree (worst case- tree with a single path)
        
        
        
        
    Explanation II: PreOrder (DFS) Traversal - Iterative
        - Works the same with the previous approach
        - stack = pair the nodes with the corresponding maximum value seen so far
        
        - Initialize stack and res
        - Executing DFS, while the stack is not empty, pop from the stack
        - If node.val is >= maxVal, increment res and push the children to the stack along with the maximum value between maxVal and node.val
        
        - TC: O(n) where n is number of nodes
        - SC: O(n) for the stack. Worst case is when the right child has 2 children and the left child has no children and vice-versa. The stack will contain at most N/2 nodes at maximum depth
        
    Explanation III: BFS Traversal
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def goodNodes(self, root: TreeNode) -> int: 
        def dfs(node, maxVal):
            nonlocal res
            if not node: return 0
            if maxVal <= node.val: res += 1
            maxVal = max(maxVal, node.val)
            if node.left: dfs(node.left, maxVal)
            if node.right: dfs(node.right, maxVal)
        
        res = 0   
        dfs(root, root.val)
        return res


class Solution2:
    def goodNodes(self, root: TreeNode) -> int: 
        stack = [(root, root.val)]
        res = 0
        
        while stack:
            node, maxVal = stack.pop()
            if maxVal <= node.val: res += 1
            
            if node.left: stack.append((node.left, max(maxVal, node.val)))
            if node.right: stack.append((node.right, max(maxVal, node.val)))
        return res