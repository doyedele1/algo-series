'''
    Explanation I:
        - Can we do a level order traversal? - to store the nodes at each level
        - When the queue is not empty at each level, we check if we are at the leftmost node in the level and we make the next pointer of that node to be the number next to the leftmost node.
                        1
                    2				3
            4		5		6		7
        - level 0: queue = ([1])
        - level 1: queue = ([2,3]). 2.next = 3
        - level 2: queue = ([4,5,6,7]). 4.next = 5, 5.next = 6, 6.next = 7
    
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
        while len(q) > 0:
            length = len(q)
            for i in range(length):
                head = q.popleft()
                if i < length - 1:
                    head.next = q[0]    
                if head.left != None:
                    q.append(head.left)
                if head.right != None:
                    q.append(head.right)
        return root

'''
    Explanation II:
        - When we establish the next pointers between the nodes, the nodes represent a linked list
        - So can we have access to the leftmost node at each level? Yes, we can. The leftmost node at each level will be our starting point
        - current = used to traverse all the nodes on the current level
        - previous = points to the node on the next level (left and/or right children)
        - Processing the leftmost node, when we have set the previous pointer the first time, we can then set the leftmost node to the previous node.
        
        TC - O(n)
        SC - O(1)
'''
class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        
        # the zeroth level --> the root node is the leftmost node
        leftmostNode = root
        
        while leftmostNode: # we need to process the next level
            current = leftmostNode # tracks the latest node on the current level
            previous = None # tracks the latest node on the next level
            leftmostNode = None # to clear the leftmostNode so the while loop doesn't keep running
            
            # process the current level
            while current:
                if current.left:
                    # We can set the leftmostNode pointer to the left child node since the left child node is the first node we encountered on the next level
                    if not leftmostNode:
                        leftmostNode = current.left
                    
                    # if we have a previous pointer or found one node on the next level, we can set the previous next pointer to the left child node
                    if previous:
                        previous.next = current.left
                        
                    previous = current.left
                        
                if current.right:
                    # We can set the leftmostNode pointer to the right child node since the right child node is the first node we encountered on the next level
                    if not leftmostNode:
                        leftmostNode = current.right
                    
                    # if we have a previous pointer or found one node on the next level, we can set the previous next pointer to the right child node
                    if previous:
                        previous.next = current.right
                        
                    previous = current.right
                
                # traverse to the next node
                current = current.next

        return root