# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reversing the sum linked list
class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
            
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
            
        sum = num1 + num2
        
        dummy = ListNode(0)
        temp = dummy
        
        if sum == 0: return dummy
        
        while sum > 0:
            temp.next = ListNode(sum % 10)
            temp = temp.next
            sum //= 10
            
        previous = None
        temp = dummy.next
        while temp:
            nxt = temp.next
            temp.next = previous
            previous = temp
            temp = nxt
        return previous

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
            
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
            
        sum = num1 + num2
        
        dummy = ListNode(0)
        temp = dummy
        
        if sum == 0: return dummy
        
        while sum > 0:
            temp.next = ListNode(sum % 10, temp.next) 
            sum //= 10
        return dummy.next