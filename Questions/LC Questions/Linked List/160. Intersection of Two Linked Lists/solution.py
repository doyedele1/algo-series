from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# TC: O(n + m), SC: 0(m)
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        
        while headB:
            seen.add(headB)
            headB = headB.next
        
        while headA:
            if headA in seen:
                return headA
            headA = headA.next
        return None

# TC: O(n + m), SC: 0(1)
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        dummyA = headA
        dummyB = headB
        
        while dummyA != dummyB:
            dummyA = headB if dummyA is None else dummyA.next
            dummyB = headA if dummyB is None else dummyB.next
        return dummyB