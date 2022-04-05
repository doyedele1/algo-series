'''
    Explanation:
        cache --> using memory to speed up the computer algorithms
        * all the key values are positive so we can return something that won't clash with -1 when the key is not found in the cache
        - We could use OrderedDict library in Python which remembers the order in which elements are inserted
        
        - Get or put requires us to delete or insert at different positions. We can use a doubly linked list because deletion and insertions are constant time, but we also need the linked list for proper ordering.
        - When we delete things, we pop it off the right (most recent used)
        left <-> [1,1] <-> [2,2] <-> right
        lru                          mru
        
        
        capacity = 2
        Put [1,1] to the cache --> {1: 1}
        Put [2,2] to the cache --> {1: 1, 2: 2}
        Get [1] from the cache --> {2:2, 1:1}
        Put [3,3] to the cache --> {1:1, 3:3}
        Get [2] from the cache --> -1
        Put [4,4] to the cache --> {3:3, 4:4}
        Get [1] from the cache --> -1
        Get [3] from the cache --> 3
        Get [4] from the cache --> 4
        
        TC - O(1) for both get and put operations
        SC - O(capacity) for the hashmap and doubly linked list which contain at most capacity + 1 elements
'''

class Node:
    def __init__(self, key, value):
        # the map has a key, value pair
        self.key = key
        self.value = value
        self.previous = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        # Create a hash map to map the keys to nodes. Key = the node's key, Value = the node reference
        self.node_map = {}
        self.cache_capacity = capacity
        
        # The left pointer is for the LRU, while the right pointer is for the MRU
        self.left = Node(0,0)
        self.right = Node(0,0)
        
        # We want the nodes to be connected to each other. If we are inserting a node, we want it to be between these left and right pointers
        self.left.next = self.right
        self.right.previous = self.left
        
    # Insert node at the right
    def insert(self, node):
        previous_node = self.right.previous
        next_node = self.right
        
        previous_node.next = node
        next_node.previous = node
        
        node.next = next_node
        node.previous = previous_node
        
    # Remove the node from linked list - O(1)
    def remove(self, node):
        previous_node = node.previous
        next_node = node.next
        
        previous_node.next = next_node
        next_node.previous = previous_node
        
    def get(self, key: int) -> int:
        if key in self.node_map:
            self.remove(self.node_map[key])
            self.insert(self.node_map[key])
            return self.node_map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self.remove(self.node_map[key])
        self.node_map[key] = Node(key, value)
        self.insert(self.node_map[key])
        
        if len(self.node_map) > self.cache_capacity:
            # Evict from the linked list and delete the LRU from the hash map
            lru = self.left.next
            self.remove(lru)
            del self.node_map[lru.key]
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)