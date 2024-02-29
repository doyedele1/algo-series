from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# TC: O(n), SC: 0(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        dummy_A = headA
        dummy_B = headB
        
        while dummy_A != dummy_B:
            if not dummy_A:
                dummy_A = headB
            else:
                dummy_A = dummy_A.next
            
            if not dummy_B:
                dummy_B = headA
            else:
                dummy_B = dummy_B.next
        return dummy_B