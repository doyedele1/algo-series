'''
    Explanation:
        - Initialize a dummy node
        - And save your dummy node in a temp node
        - Loop through the two lists when both are not null
            - If list1 < list2, add list1 to the temp node and move list1 pointer
            - Else, add list2 and move list2 pointer
            - Move your temp node pointer 
        - If list2 is not null, add list2 to the temp node
        - If list1 is not null, add list1 to the temp node

        TC: O(n + m) where n + m is the sum of the lengths of the two lists
        SC: O(1). The iterative approach only allocates a few pointers, so it has a constant overall memory footprint. newNode output is returning the head, not the entire list
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        temp = dummyNode
        
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else: 
                temp.next = list2
                list2 = list2.next
            temp = temp.next
            
        # if list2: temp.next = list2
        # else: temp.next = list1
        temp.next = list1 or list2 # the two commented lines could be replaced with this line
        
        return dummyNode.next