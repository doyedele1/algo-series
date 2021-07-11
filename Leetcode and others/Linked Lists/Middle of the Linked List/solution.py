# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Simpler solution
class Solution:
    def middleNode(self, head):
        
        slow = head
        fast = head
        
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

# Another solution  
# class Solution:
#     def findLength(self, ll):
#         length = 0
        
#         while(ll != None):
#             ll = ll.next
#             length += 1
#         return length
    
    
#     def middleNode(self, head):
#         slow = head
#         fast = head
    
#         while(fast.next != None and fast.next.next != None):
#                 slow = slow.next
#                 fast = fast.next.next
        
#         modulo = self.findLength(head)
#         modulo %= 2
#         if(modulo == 1):
#             return slow
#         else: return slow.next