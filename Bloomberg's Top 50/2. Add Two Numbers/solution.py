'''
    TC - O(max(m,n)) where m is the length of l1 and n is the length of l2
    SC - O(max(m,n)) --> the length of the new linked list is at most max(m,n) + 1
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        sum = carry = 0
        dummy = ListNode(-1)
        temp = dummy
        
        while l1 is not None or l2 is not None:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            
            sum = val1 + val2 + carry
            
            if sum > 9:
                sum -= 10
                carry = 1
            else: carry = 0
                
            temp.next = ListNode(sum)
            temp = temp.next
            
            if l1 is not None:
                l1 = l1.next
                
            if l2 is not None:
                l2 = l2.next
                
        if carry > 0:
            temp.next = ListNode(carry)
        
        return dummy.next            
