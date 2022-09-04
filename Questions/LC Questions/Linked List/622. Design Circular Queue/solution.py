'''
    Explanation: Using singly-linked list
        - 
        
        - TC: O(1) for all methods
        - SC: O(n) for the linked list we are forming
'''

class Node:
    def __init__(self, value = None):
        self.next = None
        self.value = value
        
class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.counter = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        if self.counter == 0:
            newNode = Node(value)
            self.head, self.tail = newNode, newNode
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = self.tail.next
        self.counter += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.head = self.head.next
        self.counter -= 1
        return True

    def Front(self) -> int:
        if self.counter == 0: return -1
        return self.head.value

    def Rear(self) -> int:
        if self.counter == 0: return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.counter == 0

    def isFull(self) -> bool:
        return self.counter == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()