'''
    Explanation I: Iterative Solution
        - 1 -> 2 -> 3 -> 4 -> 5
        - Use two pointers: current that is set to head and previous that is set to null
        - Reverse the node by making current.next to be the previous node
        - Move both pointers. current = next, previous = current
        - Save we broke the current.next link, we save the link before we end up breaking it
        - We stop the iteration when current is null
        
        - TC: O(n), SC: O(1)
        
    Explanation II: Recursive Solution
        - 1 -> 2 -> 3 -> 4 -> 5
        - Call function on 2,3,4 and 5, we get the sublist reversed.
        - We can then add the sublist to head of 1 to get 5 -> 4 -> 3 -> 2 <- 1
        - We need to change the next pointer of head (1). 
            - head.next.next = head. i.e. 2.next = 1 where 2 was head.next
            - head.next = null. i.e. 1.next = null
        - Base case:
            - If we call reverseList(null) when the list is of length 0, it should return null or the head
            - If we call reverseList(head) when the list is of length 1, it should also return head since it has no sublist
        - TC: O(n), SC: O(n)
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if list is of length 0 or 1
        if not head or not head.next: return head
        
        reversedSublist = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return reversedSublist

# recursive solution similar to the iterative solution
class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(previous, current):
            if current == None: return previous

            temp = current.next
            current.next = previous
            return helper(current, temp)
        
        return helper(None, head)