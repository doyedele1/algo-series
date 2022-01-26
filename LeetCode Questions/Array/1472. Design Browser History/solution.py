class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        while len(self.history) - 1 > self.pointer:
            self.history.pop()
        self.history.append(url)
        self.pointer += 1

    def back(self, steps: int) -> str:
        while self.pointer > 0 and steps > 0:
            self.pointer -= 1
            steps -= 1
        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        while self.pointer < len(self.history) - 1 and steps > 0:
            self.pointer += 1
            steps -= 1
        return self.history[self.pointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)