'''
    Explanation:
        - Initialize a dummy new node
        - And save your new node in a temporary node
        - Loop through the two lists until both have null values
            - If l1 < l2, add l1 to the temp node and move l1 pointer
            - Else add l2 and move l2 pointer
            - Move your temp node pointer 
        - If l2 is not null, add l2 to the temp node
        - If l1 is not null, add l1 to the temp node

        - TC: O(n + m) where n + m is the sum of the lengths of the two lists
        - SC: O(1). The iterative approach only allocates a few pointers, so it has a constant overall memory footprint. newNode output is returning the head, not the entire list
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode(-1)
        temp = newNode
        
        while l1 and l2: # while both l1 and l2 are not null
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else: 
                temp.next = l2
                l2 = l2.next
            temp = temp.next
            
        # if l2: temp.next = l2
        # else: temp.next = l1
        temp.next = l1 or l2 # the two commented lines could be replaced with this line
        
        return newNode.next