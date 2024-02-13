'''
    Explanation:
        Step 1: Find the middle of the linked list. If even length, return the second middle node
            1 -> 2 -> 3 -> 4 -> 5 -> 6
            return 4

        Step 2: Reverse the second part of the list
            4 -> 5 -> 6 becomes 6 -> 5 -> 4
            
            curr = 4

            next_node = 5
            4.next = None
            prev = 4
            curr = 5

            next_node = 6
            5.next = 4
            prev = 5
            curr = 6

            next_node = None
            6.next = 5
            prev = 6
            curr = None

            List becomes = 1 -> 2 -> 3 and 6 -> 5 -> 4

        Step 3: Merge the two halfs
            1 -> 2 -> 3 and 6 -> 5 -> 4
            
            List becomes 1 -> 6 -> 2 -> 5 -> 3 -> 4

        TC: O(n)
        SC: O(1)
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        # find the middle of the linked list. If even length, return the second middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second part of the list
        prev, curr = None, slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # merge the two halfs
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2