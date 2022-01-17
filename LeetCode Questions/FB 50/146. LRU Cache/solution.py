class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.previous = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        # Create a hash map to map the keys to nodes
        self.node_map = {}
        self.cache_capacity = capacity
        
        # The left pointer is for the LRU, while the right pointer is for the MRU
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.previous = self.left
        
    def get(self, key: int) -> int:
        if key in self.node_map:
            self.remove(self.node_map[key])
            self.insert(self.node_map[key])
            return self.node_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self.remove(self.node_map[key])
        self.node_map[key] = Node(key, value)
        self.insert(self.node_map[key])
        
        if len(self.node_map) > self.cache_capacity:
            # Remove from the list and delete the LRU from the hash map
            lru = self.left.next
            self.remove(lru)
            del self.node_map[lru.key]
    
    # Insert at the rightmost position right before the right pointer
    def insert(self, node):
        previous_node = self.right.previous
        next_node = self.right
        previous_node.next = node
        next_node.previous = node
        node.next = next_node
        node.previous = previous_node
        
    # Remove node from linked list
    def remove(self, node):
        previous_node = node.previous
        next_node = node.next
        
        previous_node.next = next_node
        next_node.previous = previous_node
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
    Explanation:
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
'''