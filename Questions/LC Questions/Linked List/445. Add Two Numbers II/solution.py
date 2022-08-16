from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reversing the sum linked list
class Solution1:
    def convertToNums(self, ll):
        num = 0
        while ll:
            num = num * 10 + ll.val
            ll = ll.next
        return num

    def reverseList(self, head):
        previous, current = None, head
        
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.convertToNums(l1)
        num2 = self.convertToNums(l2)
            
        sumOfNums = num1 + num2
        
        dummy = ListNode(0)
        temp = dummy
        
        if sumOfNums == 0: return dummy
        
        while sumOfNums > 0:
            temp.next = ListNode(sumOfNums % 10)
            temp = temp.next
            sumOfNums //= 10
        
        return self.reverseList(dummy.next)

class Solution2:
    def convertToNums(self, ll):
        num = 0
        while ll:
            num = num * 10 + ll.val
            ll = ll.next
        return num

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.convertToNums(l1)
        num2 = self.convertToNums(l2)
            
        sumOfNums = num1 + num2
        
        dummy = ListNode(0)
        temp = dummy
        
        if sumOfNums == 0: return dummy
        
        while sumOfNums > 0:
            '''
                print(sumOfNums, temp.next)
                    7807 None
                    780 ListNode{val: 7, next: None}
                    78 ListNode{val: 0, next: ListNode{val: 7, next: None}}
                    7 ListNode{val: 8, next: ListNode{val: 0, next: ListNode{val: 7, next: None}}}
                    0 ListNode{val: 7, next: ListNode{val: 8, next: ListNode{val: 0, next: ListNode{val: 7, next: None}}}}
            '''
            
            temp.next = ListNode(sumOfNums % 10, temp.next) 
            sumOfNums //= 10
        return dummy.next