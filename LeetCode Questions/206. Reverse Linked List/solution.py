# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        # Iterative Solution
        previous, current = None, head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
            
        return previous

        # Recursive solution to reverse a linked list
        if head is None or head.next is None:
            return head
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_head