'''
    Explanation I: Iterative Approach (O(n) space)
        - We could have created a clone with next pointers, but the random pointers introduce the difficulty for this question
        - Two passes (loops):
            1. Create the clone of the linked list nodes and map every original node to the cloned node to a hashmap
            2. Use the hashmap and add the pointers of the original linked list to the cloned linked list
        - Traverse the linked list from the head
            - Store the reference of the new created node in a hashmap
        - Random Pointer
            - If the random pointer of the current node i points to the node j and the clone of j exists in the hashmap, we want to use the cloned node reference from the hashmap
            - If the random pointer of the current node i points to the node j has not been created yet, we want to create a new node corresponding to j and add it to the hashmap
        - Next Pointer
            - If the next pointer of the current node i points to the node j and the clone of j exists in the hashmap, we want to use the cloned node reference from the hashmap
            - If the next pointer of the current node i points to the node j has not been created yet, we want to create a new node corresponding to j and add it to the hashmap
            
            - TC: O(n) where n is the number of nodes in the original linked list
            - SC: O(n) for the hashmap containing mapping from the original linked list nodes to the cloned linked list nodes
            

    Explanation II: Iterative Approach (O(1) space)
        - Instead of using a hashmap to map the original node to the cloned node, can we tweak the original linked list and keep every cloned node next to its original node?
        
        - Traverse the original list: 
            - Clone the nodes as we place the cloned node next to its original node
                clone.next = original.next
                original.next = clone
            
            - Weaving: 
                clone.random = original.random.next
            
            - Unweaving:
                original.next = clone.next
                clone.next = other_original.next
                
        - TC: O(n)
        - SC: O(1)
'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional


class Solution1:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_clone = { None: None }
        
        curr = head
        while curr:
            # creating a clone of the nodes
            clone = Node(curr.val)
            # putting the clone into the hashmap. key = curr, value = the cloned node
            original_to_clone[curr] = clone
            curr = curr.next
        
        curr = head
        while curr:
            clone = original_to_clone[curr]
            # set the pointers of the cloned nodes
            clone.next = original_to_clone[curr.next] # when curr.next is None, return None
            clone.random = original_to_clone[curr.random] # when curr.random is None, return None
            curr = curr.next
        
        return original_to_clone[head]


class Solution2:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        curr = head
        while curr:
            clone = Node(curr.val, None, None)
            # place the cloned node next to its original node
            clone.next = curr.next
            curr.next = clone
            curr = clone.next
            
        curr = head
        # weaving
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        
        # unweaving
        curr_original_list = head
        curr_clone_list = head.next
        head_clone = head.next
        while curr_original_list:
            curr_original_list.next = curr_original_list.next.next
            curr_clone_list.next = curr_clone_list.next.next if curr_clone_list.next else None
            curr_original_list = curr_original_list.next
            curr_clone_list = curr_clone_list.next
        return head_clone