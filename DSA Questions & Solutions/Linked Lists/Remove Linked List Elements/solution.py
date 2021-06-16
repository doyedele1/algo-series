# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        while(head != None and head.val == val):
            head = head.next
        
        temp = head
        while(temp != None and temp.next != None):
            if(temp.next.val == val):
                temp.next = temp.next.next
            else: 
                temp = temp.next
        return head