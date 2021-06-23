# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # A more optimized solution. TC - O(n), SC - 0(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if(headA == None or headB == None): return None
        
        dummy_A = headA
        dummy_B = headB
        
        while(dummy_A != dummy_B):
            if(dummy_A == None):
                dummy_A = headB
            else:
                dummy_A = dummy_A.next
            
            if(dummy_B == None):
                dummy_B = headA
            else:
                dummy_B = dummy_B.next
        return dummy_B