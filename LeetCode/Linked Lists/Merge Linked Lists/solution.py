# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
# Initialize a new node
# And save your new node in a temporary node
# Loop through the two lists until both have null values
    # if li < l2, add l1 to the temp node and move l1 pointer
    # else add l2 and move l2 pointer
    # move your temp node pointer 
# If l2 is not null, add l2 to the temp node
# If l1 is not null, add l1 to the temp node

        newNode = ListNode(-1)
        temp = newNode
        
        while(l1 != None and l2 != None):
            if(l1.val < l2.val):
                temp.next = l1
                l1 = l1.next
            else: 
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        
        
        if(l2 != None):
            temp.next = l2
        else: temp.next = l1
        # print(temp)
        
        return newNode.next
        
        
        
