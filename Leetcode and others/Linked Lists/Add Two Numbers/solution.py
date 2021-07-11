# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyNode = ListNode(-1)
        temp = dummyNode
        sum = 0
        carry = 0
        
        while(l1 or l2):
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            sum = val1 + val2 + carry
            
            if(sum > 9):
                sum -= 10
                carry = 1
            else: carry = 0
                
            temp.next = ListNode(sum)
            temp = temp.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        if(carry == 1):
            temp.next = ListNode(carry)
        
        return dummyNode.next
            