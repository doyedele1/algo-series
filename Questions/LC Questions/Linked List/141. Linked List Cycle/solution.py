'''
    Explanation I: Using a hashset
        - If we visit a node more than once, we have a cycle
        - Add to the hashset if node doesn't exist in the hashmap
        - If node exists, then return True since we have a cycle
        
        TC: O(n), SC: O(n)
        
    Explanation II: Floyd's Cycle Finding Algorithm (Tortoise and Hare)
        - slow = one step
        - fast = two steps
        
        Time Complexity Explanation: 
            case where linked list has no cycle = O(n)
            case where linked list has a cycle.
                When both slow and fast pointers are inside the cycle,
                                f
                            s
                    s to f = 1
                    f to s = K
                    Moving clockwise, for the fast pointer to catch up with the slow pointer, K + 1 - 2 = K - 1, so K iterations
        TC: O(n + K) = O(n)
        SC: O(1)
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head:
            if head in visited: 
                return True
            visited.add(head)
            head = head.next
        return False
    
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False