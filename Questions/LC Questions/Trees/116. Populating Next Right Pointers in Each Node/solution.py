'''
    Explanation I:
        Can we do a level order traversal (BFS)? - to store the nodes at each level
        When the queue is not empty at each level, we check if we are at the leftmost node in the level and we make the next pointer of that node to be the number next to the leftmost node.
                            1
                    2				3
               4		5		6		7
            level 0: queue = ([1])
            level 1: queue = ([2,3]); 2.next = 3
            level 2: queue = ([4,5,6,7]). 4.next = 5, 5.next = 6, 6.next = 7
    
        TC - O(n) where n is the total number of nodes
        SC - O(n/2 + 1) --> O(n)
'''
# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        q = deque([root])

        while q:
            length = len(q)
            for i in range(length):
                curr = q.popleft()
                if i < length - 1: curr.next = q[0]
                if curr.left != None: q.append(curr.left)
                if curr.right != None: q.append(curr.right)
        return root

'''
    Explanation II:
        When we already establish the next pointers of the nodes at the next level when we are currently on the current level, we can traverse the nodes as a linked list
        So can we have access to the leftmost node at each level? Yes, we can. The leftmost node at each level will be our starting point. At node 1 level 0, the leftmost node is 1. The current node is 1, and the previous node is 2
            current = used to traverse all the nodes on the current level starting from the leftmost node
            previous = points to the leftmost node on the next level (no child, left and/or right children)
        Processing the leftmost node, when we have set the previous pointer the first time, we can then set the leftmost node to the previous node.
            
        TC - O(n)
        SC - O(1)
'''
class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        
        leftmostNode = root
        
        # to process the next level
        while leftmostNode:
            current = leftmostNode
            previous = None
            leftmostNode = None # to clear the leftmostNode so the while loop doesn't keep running
            
            while current:
                if current.left:
                    if not leftmostNode:
                        leftmostNode = current.left
                    
                    if previous:
                        previous.next = current.left
                        
                    previous = current.left
                
                if current.right:
                    if not leftmostNode:
                        leftmostNode = current.right
                    
                    if previous:
                        previous.next = current.right
                        
                    previous = current.right
                
                current = current.next

        return root