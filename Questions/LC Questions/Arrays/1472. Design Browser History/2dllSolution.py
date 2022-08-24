class Node:
    def __init__(self, value = None):
        self.value = value
        self.previous = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.previous = self.head
        node = Node(homepage)
        self.urlPosition = self.head
        self.insertNode(node)
    
    def insertNode(self, node):
        self.urlPosition.next = node
        node.previous = self.urlPosition
        self.tail.previous = node
        node.next = self.tail
        self.urlPosition = self.urlPosition.next

    def visit(self, url: str) -> None:
        self.insertNode(Node(url))

    def back(self, steps: int) -> str:
        while steps > 0 and self.urlPosition.previous and self.urlPosition.previous.previous:
            self.urlPosition = self.urlPosition.previous
            steps -= 1
        return self.urlPosition.value

    def forward(self, steps: int) -> str:
        while steps > 0 and self.urlPosition.next and self.urlPosition.next.next:
            self.urlPosition = self.urlPosition.next
            steps -= 1
        return self.urlPosition.value
    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)