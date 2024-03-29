'''
    Explanation I: Iterative Solution
        * Draw the prev, next and child node arrows, and use it to explain the code of the pointers change
        
        If curr has child, we append curr.next into the stack
        stack = [4,9]

        - TC: O(n)
        - SC: O(n). Space used by the stack data structure
    
    Explanation II: Recursive Solution
        - We will have a recursive helper (flatten_helper) function that takes in the head pointer 
            curr = head, tail = head
            - While curr is not null,
                - If no child,
                    next will point to next of current
                    current = next
                - If it has child,
                    We flatten the child. i.e. child_tail will be flatten_helper function called on child. Recursive function here
                    curr --> next = child
                    child_tail --> next = next
                    curr --> child = null
                    child --> prev = curr
                    - If next, 
                        next --> prev = child_tail
                    - If next is null, 
                        curr = tail
                    - If curr, tail = curr
            - return tail

        TC - O(n) where n is the number of nodes in the list, we visit each node once from beginning to end
        SC - O(n), the recursion call stack which can be of the order of n - O(n). In the worst case, the nodes are chained with each other only with the child pointers. In this case, the recursive calls would pile up and take n space in the function call stack
'''

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution1:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        curr = head
        
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                    curr.next.prev = None
            
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            
            if curr.next:
                curr = curr.next
            else:
                break
        
        while stack:
            curr.next = stack.pop()
            curr.next.prev = curr
            while curr and curr.next:
                curr = curr.next
        return head

class Solution2:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if head is there, i.e. the linked list is not empty
        if head: 
            self.flattenHelper(head)
        return head
    
    def flattenHelper(self, head):
        curr, tail = head, head

        while curr:
            child = curr.child
            nxt = curr.next # so that we can return the next of child_tail as the next we stored
            
            if child:
                child_tail = self.flattenHelper(child)
            
                child_tail.next = nxt
                if nxt: 
                    nxt.prev = child_tail
                    
                curr.next = child
                child.prev = curr
                
                curr.child = None
                
                curr = child_tail
            
            # if there is no child
            else: curr = nxt
                
            if curr: 
                tail = curr # tail cannot be null because tail will always be there because it is running when we have a child
                
        return tail