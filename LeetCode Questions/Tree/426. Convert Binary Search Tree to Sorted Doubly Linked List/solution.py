from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        def inorder(node):
            nonlocal head, tail
            
            if not node:
                return
            
            inorder(node.left)
            
            if tail:
                tail.right = node
                node.left = tail
            else:
                head = node
            tail = node
            
            inorder(node.right)
            
        head = None
        tail = None
        
        inorder(root)
        
        head.left = tail
        tail.right = head
        
        return head
        
        '''
            Explanation:
                - Ways to convert to a DLL
                    - BFS
                    - DFS inorder traversal
                - Recursively call the left child
                    - Have a terminating condition for if not node, retunr nothing
                - Initialize head and tail pointers for the linked list
                    - If no head, let head and tail point to your current node
                    - Next current node, does the ll have a tail already? It does. tail.next = current, current.prev = tail, tail = current
                - After we are done with the treenodes, take head.previous = tail and tail.next = head
                
                TC - O(n) where n is the number of nodes
                SC - O(n) space taken by the recursion call stack in the worst case for unbalanced tree. Call stack size max in Python = 997. Optimizing, you can rewrite solution in iterative form.
        '''