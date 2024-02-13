'''
    Explanation: If length of linked list is even
        1 -> 2 -> 3 -> 4 -> 5 -> 6

        After first iteration:
            1 -> 2 -> 3 -> 4 -> 5 -> 6
                 s
                      f
        
        After second iteration:
            1 -> 2 -> 3 -> 4 -> 5 -> 6
                      s
                                f
        
        After third iteration:
            1 -> 2 -> 3 -> 4 -> 5 -> 6
                           s
                                            f
        
        Return slow pointer node = node of 4

        TC: O(n)
        SC: O(1)
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Faster solution on LeetCode
class Solution2:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findLength(ll):
            length = 0
            
            while ll:
                ll = ll.next
                length += 1
            return length
    
    
        slow = fast = head
    
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        modulo = findLength(head)
        modulo %= 2
        if modulo == 1:
            return slow
        else:
            return slow.next