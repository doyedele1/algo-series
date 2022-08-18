# Using a nested array - not accepted on LC
class MaxStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        curmax = max(x, self.stack[-1][1] if self.stack else float("-inf"))
        self.stack.append([x, curmax])

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        temp = []
        curmax = self.peekMax()
        while curmax != self.stack[-1][0]:
            temp.append(self.stack.pop()[0])
        self.stack.pop()
        while temp:
            x = temp.pop()
            self.stack.append([x, max(x, self.stack[-1][1] if self.stack else float("-inf"))])
        return curmax

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.max_stack) == 0:
            self.max_stack.append(x)
            return
        if self.max_stack[-1] > x:
            self.max_stack.append(self.max_stack[-1])
        else:
            self.max_stack.append(x)

    def pop(self) -> int:
        if len(self.stack) != 0:
            self.max_stack.pop(-1)
            return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        if len(self.max_stack) != 0:
            return self.max_stack[-1]

    def popMax(self) -> int:
        val = self.peekMax()
        buff = []
        while self.top() != val:
            buff.append(self.pop())
        self.pop()
        while len(buff) != 0:
            self.push(buff.pop(-1))
        return val

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

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()