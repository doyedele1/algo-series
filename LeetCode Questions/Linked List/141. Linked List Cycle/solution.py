'''
    Explanation I: Using hashmaps
        - If we visit a node twice or more, we have a cycle
        - Add to the hashmap if pointer doesn't exist in the hashmap
        - If pointer exists, then return True since we've concluded we have a cycle
        - TC: O(n), SC: O(n)
        
    Explanation II: Floyd's Cycle Finding Algorithm (Tortoise and Hare)
    - slow = one step
    - fast = two steps
    
    traverse while fast != None and fast.next != None
    - TC: case where linked list has no cycle O(n)
        case where linked list has a cycle.
            - The slow pointer is about to enter the cycle , O(n)
            - Both pointers are in the cycle, it takes distance between the two runners/speed difference loops for the fast runner to catch up with the slow runner again. O(m)
            worst case: O(n+m), where n = total # of nodes, m = # of nodes in cycle
    - SC: O(1)
'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head:
            if head in visited: return True
            visited.add(head)
            head = head.next
        return False
    
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False