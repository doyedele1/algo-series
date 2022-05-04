'''
    Explanation I: Iterative solution
        - 1 -> 2 -> 3 -> 4 -> 5
        - Use two pointers: current that is set to head and previous that is set to null
        - Reverse the node by making current.next to be the previous node
        - Move both pointers. current = next, previous = current
        - Save we broke the current.next link, we save the link before we end up breaking it
        - We stop the iteration when current is null
        
        - TC: O(n), SC: O(1)
'''


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversed_head

class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(previous, current):
            if current == None: return previous

            temp = current.next
            current.next = previous
            return helper(current, temp)
        
        return helper(None, head)