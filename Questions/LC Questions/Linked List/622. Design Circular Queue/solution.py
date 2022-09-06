'''
    enqueue: add element to the end of the queue
    dequeue: remove element from the front of the queue
    Explanation II: Using a doubly-linked list
'''

class ListNode:
    def __init__(self, value, nextNode, prevNode):
        self.value = value
        self.nextNode =  nextNode
        self.prevNode = prevNode
        
class MyCircularQueue:
    def __init__(self, k: int):
        self.head = ListNode(0, None, None)
        self.tail = ListNode(0, None, self.head)
        self.head.nextNode = self.tail
        self.space = k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        newNode = ListNode(value, self.tail, self.tail.prevNode)
        self.tail.prevNode.nextNode = newNode
        self.tail.prevNode = newNode
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.head.nextNode = self.head.nextNode.nextNode
        self.head.nextNode.prevNode = self.head
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.nextNode.value

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.prevNode.value

    def isEmpty(self) -> bool:
        return self.head.nextNode == self.tail

    def isFull(self) -> bool:
        return self.space == 0

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()