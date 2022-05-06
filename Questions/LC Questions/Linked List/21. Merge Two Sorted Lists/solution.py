'''
    Explanation:
        - Initialize a dummy new node
        - Save the new node in a temp node
        - Loop through the two lists until both have null values
            # if l1 < l2, add l1 to the temp node and move l1 pointer
            # else add l2 and move l2 pointer
            # move the temp node pointer 
        - If l2 is not null, add l2 to the temp node
        - If l1 is not null, add l1 to the temp node

        Time complexity : O(n + m)O(n+m)

Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of iterations equal to the sum of the lengths of the two lists. All other work is constant, so the overall complexity is linear.

Space complexity : O(1)O(1)

The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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
        
        if l2: temp.next = l2
        else: temp.next = l1
        
        return newNode.next