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
        SC - O(n/2 + 1) -> O(n)
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
                # This condition ensures we don't establish next pointers beyond the end of a level
                if i < length - 1: curr.next = q[0]
                if curr.left != None: q.append(curr.left)
                if curr.right != None: q.append(curr.right)
        return root

'''
    Explanation II:
        There are two connections we need to establish.
            Connection 1: The two children nodes of a parent node can be connected together since they have a common parent
                curr.left.next = curr.right

            Connection 2: Nodes 5 and 6 need to be connected, but they have different parents. However, since we know that the next node of 2 is 3 from the previous level traversal, then we can create the connection we need
                On levels 1 and 2: curr.right.next = curr.next.left
                       curr 1
                nxt 2				3
               4		5		6		7
        
        TC - O(n)
        SC - O(1)
'''
class Solution2:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr, nxt = root, root.left if root else None

        while curr and nxt:
            curr.left.next = curr.right
            if curr.next: curr.right.next = curr.next.left

            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
        return root