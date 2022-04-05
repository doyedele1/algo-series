'''
    Explanation I: Iterative Approach
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
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
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