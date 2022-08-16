# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reversing the sum linked list
class Solution1:
    def reverseList(self, head):
        previous, current = None, head
        
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous
    
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
        
        return self.reverseList(dummy.next)

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
            '''
                print(sum, temp.next)
                    7807 None
                    780 ListNode{val: 7, next: None}
                    78 ListNode{val: 0, next: ListNode{val: 7, next: None}}
                    7 ListNode{val: 8, next: ListNode{val: 0, next: ListNode{val: 7, next: None}}}
                    0 ListNode{val: 7, next: ListNode{val: 8, next: ListNode{val: 0, next: ListNode{val: 7, next: None}}}}
            '''
            
            temp.next = ListNode(sum % 10, temp.next) 
            sum //= 10
        return dummy.next