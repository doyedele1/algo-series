'''
    Explanation:
        cache --> using memory to speed up the computer algorithms
        * all the key values are positive so we can return something that won't clash with -1 when the key is not found in the cache
        - We could use OrderedDict library in Python which remembers the order in which elements are inserted
        
        
        - Get or put requires us to delete or insert at different positions. We can use a doubly linked list because deletion and insertions are constant time, but we also need linked list for proper ordering.
        - When we delete things, we pop it off the right (most recent used)
        left <-> [1,1] <-> [2,2] <-> right
        lru                          mru
        
        
        capacity = 3
        Put [1,1], [2,2], [3,3] to the cache -->
            {
                1: 1,
                2: 2,
                3: 3
            }
        Put [4,4] to the cache
            {
                2: 2,
                3: 3,
                4: 4
            }
        Get [2] from the cache
            {
                3: 3,
                4: 4,
                2: 2
            }
            
            TC - O(1) for both get and put operations
            SC - O(capacity) for the hashmap and doubly linked list which contain at most capacity + 1 elements
'''

class Node:
    def __init__(self):
        # the map has a key, value pair
        self.key = 0
        self.val = 0
        self.previous = None
        self.next = None
        
class LRUCache:
    # Insert node right after the head
    def insert_node(self, node):
        node.previous = self.left
        node.next = self.left.next
        
        self.left.next.previous = node
        self.left.next = node
        
    # Remove the first added node (an existing node) from linked list - O(1)
    def remove_node(self, node):
        previous_node = node.previous
        next_node = node.next
        
        previous_node.next = next_node
        next_node.previous = previous_node
        
    # Add node in between to the right
    def insert_to_right(self, node):
        self.remove_node(node)
        self.insert_node(node)
        
    # Remove the current left
    def remove_left(self):
        result = self.right.previous
        self.remove_node(result)
        return result
    
    def __init__(self, capacity: int):
        # Create a hash map to map the keys to nodes
        self.node_map = {}
        self.len_node_map = 0
        self.cache_capacity = capacity
        
        # The left pointer is for the LRU, while the right pointer is for the MRU
        self.left = Node()
        self.right = Node()
        
        # We want the nodes to be connected to each other. If we are inserting a node, we want it to be between these left and right pointers
        self.left.next = self.right
        self.right.previous = self.left
        
    def get(self, key: int) -> int:
        node = self.node_map.get(key, None)
        
        if not node:
            return -1
        
        # Move the node to the right
        self.insert_to_right(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.node_map.get(key)
        
        if not node:
            newNode = Node()
            newNode.key = key
            newNode.val = value
            
            self.node_map[key] = newNode
            self.insert_node(newNode)
            
            self.len_node_map += 1
        
            if self.len_node_map > self.cache_capacity:
                # Evict from the linked list and delete the LRU from the hash map
                lru = self.remove_left()
                del self.node_map[lru.key]
                self.len_node_map -= 1
        
        else:
            # Update the value in the linked list
            node.val = value
            self.insert_to_right(node)
        
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)