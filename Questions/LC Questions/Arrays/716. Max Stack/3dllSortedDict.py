# Accepted on LC, but sortedcontainers library is only available on LC
from sortedcontainers import SortedDict

class Node:
    def __init__(self, val, prev=None, nxt=None):    
        self.val = val
        self.prev = prev
        self.next = nxt
                
class DoubleLinkedList:
    def __init__(self):
        self.tail = Node(0)
        self.head = Node(0, None, self.tail)
        self.tail.prev = self.head
        
    def add(self, val):
        new_node = Node(val, None, self.tail)
        new_node.prev = self.tail.prev        
        self.tail.prev.next = new_node        
        self.tail.prev = new_node
        return new_node
    
    def peek(self): return self.tail.prev.val
    
    def unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
        
    def pop(self):
        return self.unlink(self.tail.prev).val
                                            
class MaxStack:
    def __init__(self):
        self.list = DoubleLinkedList()
        self.max = SortedDict()
                
    def push(self, x: int) -> None: 
        node = self.list.add(x)        
        if x not in self.max: self.max[x] = []            
        self.max[x].append(node)
    
    def top(self) -> int: 
        return self.list.peek()
        
    def peekMax(self) -> int:
        return self.max.peekitem()[0]
        
    def pop(self) -> int:
        val = self.list.pop()
        self.max[val].pop()
        if not self.max[val]: del self.max[val]
        return val
        
    def popMax(self) -> int:
        val, addr = self.max.peekitem()
        self.list.unlink(addr.pop())        
        if not addr: del self.max[val]            
        return val