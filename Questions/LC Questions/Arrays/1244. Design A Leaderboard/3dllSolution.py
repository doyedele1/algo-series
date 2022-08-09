class Node:
    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.val = value
        
class Leaderboard:
    def __init__(self):
        self.scores = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def addNode(self, node):
        cur = self.head.next
        while cur.val != None and node.val > cur.val:
            cur = cur.next
        prev = cur.prev
        node.next = cur
        cur.prev = node
        node.prev = prev
        prev.next = node
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            node = self.scores[playerId]
            self.removeNode(node)
            node.val += score
        else:
            node = Node(score)
        self.addNode(node)
        self.scores[playerId] = node

    def top(self, K: int) -> int:
        result = 0
        cur = self.tail.prev
        while K > 0:
            result += cur.val
            cur = cur.prev
            K -=1
        return result
            
    def reset(self, playerId: int) -> None:
        node = self.scores[playerId]
        self.removeNode(node)
        self.scores.pop(playerId)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
# 3 4 7 8 
# list - sort nlogn
# heap - klogn
# a-b-c-d-e - O(k)
# linkedList or Heap
# H <--> T