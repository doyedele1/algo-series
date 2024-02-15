'''
    Explanation:
        1 -> 2 -> 3 -> 4 -> 5, n = 2

        - Let's use two pointers left and right
            1 -> 2 -> 3 -> 4 -> 5
        l
            r
        
        - Move the right pointer to allow both points be exactly separated by n nodes apart
            First iteration
                1 -> 2 -> 3 -> 4 -> 5
            l
                    r
            n = 1

            Second iteration
                1 -> 2 -> 3 -> 4 -> 5
            l
                          r
            n = 0

        - Move both left and right pointers while right is not None to allow the left pointer get to the node we want to delete
            First iteration
                1 -> 2 -> 3 -> 4 -> 5
                l
                               r
            Second iteration
                1 -> 2 -> 3 -> 4 -> 5
                     l
                                    r
            Third iteration
                1 -> 2 -> 3 -> 4 -> 5
                          l
                                         r
        
        - We have a next pointer which is the nth node from the end that is to be deleted
            l.next = l.next.next
            then just return dummy.next

        TC: O(n), SC: O(1)            
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        left = dummyNode
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummyNode.next