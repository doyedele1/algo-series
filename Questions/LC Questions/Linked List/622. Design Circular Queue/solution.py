'''
    enqueue: add element to the end of the queue
    dequeue: remove element from the front of the queue

    Explanation I: Using array
    Explanation II: using a singly linked list
    Explanation II: Using a doubly-linked list

    TC: O(1) for all solutions
'''

class MyCircularQueue1:
    def __init__(self, k: int):
        self.q = [None] * k
        self.headIndex, self.tailIndex = 0, 0
        self.counter = 0
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        self.q[self.tailIndex] = value
        self.tailIndex = (self.tailIndex + 1) % self.k
        self.counter += 1
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.headIndex = (self.headIndex + 1) % self.k
        self.counter -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.headIndex]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.tailIndex - 1]

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

class ListNode1:
    def __init__(self, value):
        self.value = value
        self.next =  None
        
class MyCircularQueue2:
    def __init__(self, k: int):
        self.head, self.tail = None, None
        self.k = k
        self.counter = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        newNode = ListNode1(value)
        if self.counter == 0:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.counter += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = self.head.next
        self.counter -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.value

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.counter == 0

    def isFull(self) -> bool:
        return self.counter == self.k

class ListNode2:
    def __init__(self, value, nxt, previous):
        self.value = value
        self.next =  nxt
        self.previous = previous
class MyCircularQueue3:
    def __init__(self, k: int):
        self.head = ListNode2(0, None, None)
        self.tail = ListNode2(0, None, self.head)
        self.head.next = self.tail
        self.space = k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        newNode = ListNode2(value, self.tail, self.tail.previous)
        self.tail.previous.next = newNode
        self.tail.previous = newNode
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.head.next = self.head.next.next
        self.head.next.previous = self.head
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.next.value

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.previous.value

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def isFull(self) -> bool:
        return self.space == 0