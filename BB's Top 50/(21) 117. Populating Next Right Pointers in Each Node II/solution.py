'''
    Explanation I:
        - Can we do a level order traversal?
        - When the queue is not empty at each level, we check if we are at the leftmost node in the level and we make the next pointer of that node to be the number next to the leftmost node.
                1
		2				    3
    4		5		    6		7
    level 0: queue = ([1])
    level 1: queue = ([2,3]). 2.next = 3
    level 2: queue = ([4,5,6,7]). 4.next = 5, 5.next = 6, 6.next = 7
    
    TC - O(n) where n is the total number of nodes
    SC - O(n/2 + 1) --> O(n)
'''
import collections
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        
        q = collections.deque([root])
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