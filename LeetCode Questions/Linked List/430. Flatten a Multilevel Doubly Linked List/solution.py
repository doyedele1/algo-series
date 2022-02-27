'''
    Explanation:
        - We will have a recursive helper (flatten_helper) function that takes in the head pointer (curr = head, tail = head)
        - While curr is not null,
            - Here we can store curr, next and tail on the first node (head)
            - If no child,
                current = next and next will point to next of current
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

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


from typing import Optional

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head: # if head is there, i.e. the linked list is not empty
            self.flatten_helper(head)
        return head
    
    def flatten_helper(self, head):
        curr, tail = head, head
        while curr:
            child = curr.child
            next = curr.next # so that we can return the next of child_tail as the next we stored
            
            if child: # if there is child
                child_tail = self.flatten_helper(child)
                
                child_tail.next = next
                if next: next.prev = child_tail
                    
                curr.next = child
                child.prev = curr
                
                curr.child = None
                
                curr = tail   
            
            else: # if there is no child
                curr = next
                
            if curr: tail = curr # tail cannot be null because tail will always be there because it is running when we have a child
                
        # return the tail of the flatten list
        return tail