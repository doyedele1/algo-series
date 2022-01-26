from typing import Optional

# Definition for a Node
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head != None: 
            self.flatten_helper(head)
        return head
    
    def flatten_helper(self, head):
        curr, tail = head, head
        while curr != None:
            child = curr.child
            next = curr.next
            if child != None:
                _tail = self.flatten_helper(child)

                _tail.next = next
                if next != None: next.prev = _tail

                curr.next = child
                child.prev = curr

                curr.child = None

                curr = tail   
            else:
                curr = next
            if curr != None: tail = curr
                
        # return the tail of the flatten list
        return tail
        
        '''
            Explanation:
                We will have a recursive (flatten_helper) function that takes in the head pointer and checks for child on current
                    - If no child,
                        current = next and next will point to next of current
                    - If it has child, 
                        We flatten the child. i.e. tail will be flatten_helper function called on child. Recursive function here
                        curr --> next = child
                        tail --> next = next
                        curr --> child = null
                        child --> prev = curr
                    - If next, 
                        next --> prev = tail
                    - curr = tail
                    - return tail
                    
                TC - O(n) where n is the number of nodes in the list
                SC - O(1), except the recursion call stack which can be of the order of n - O(n). In the worst case, the binary tree might be unbalanced. i.e. nodes are chained with each other only with the child pointers. In this case, the recursive calls would pile up and take n space in the function call stack
        '''