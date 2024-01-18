'''
    Explanation: Doubly Linked List + Hashmap
        - removeNode()
            - Get the previous and next values of the node to be removed
            - The new previous.next becomes the old next
            - The new next.previous becomes the old previous
            - TC: O(1)
            
        - addNode()
            - Get the current node
            # 1--2--4, we want to insert 3
            - Find the correct position to insert node to # the correct position is at node 4
            - When you get the correct position, 
                - The new previous node becomes the current.previous. i.e. the new previous of 3 is 2
                - 3's next is the current node which is 4
                - The new 4.previous becomes the new node to be inserted which is 3
                - 3's previous becomes the old previous which is 2
                - 2's next becomes the new node which is 3
            - TC: O(n). The linked list is in an ascending order
        
        - addScore()
            - If playerId exists in the hashmap, 
                - Remove node from the dll
                - Add score of the playerId
            - If the playerId doesn't exist, create a node for it
            - Add the node to the dll
            - Update the score in the hashmap
            - TC: O(n)

        - top()
            - Get the top k nodes before tail and add the scores to the res variable
            - TC: O(k). Or O(n) depending on the value of k
            
        - reset()
            - Remove node from the dll
            - Remove playerId entry from the hashmap
            - TC: O(1)
'''

class Node:
    def __init__(self, value = None):
        self.previous = None
        self.next = None
        self.value = value
        
class Leaderboard:
    def __init__(self):
        self.scores = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.previous = self.head

    def removeNode(self, node):
        previous, nxt = node.previous, node.next
        previous.next = nxt
        nxt.previous = previous
        
    def addNode(self, node):
        curr = self.head.next
        while curr.value != None and node.value > curr.value:
            curr = curr.next
        previous = curr.previous
        node.next = curr
        curr.previous = node
        node.previous = previous
        previous.next = node
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            node = self.scores[playerId]
            self.removeNode(node)
            node.value += score
        else: node = Node(score)
            
        self.addNode(node)
        self.scores[playerId] = node

    def top(self, K: int) -> int:
        res = 0
        curr = self.tail.previous
        while K > 0:
            res += curr.value
            curr = curr.previous
            K -=1
        return res
            
    def reset(self, playerId: int) -> None:
        node = self.scores[playerId]
        self.removeNode(node)
        self.scores.pop(playerId)

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)