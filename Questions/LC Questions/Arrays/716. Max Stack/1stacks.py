# Using one stack (nested array). [[stack, maxStack]] - not accepted on LC
class MaxStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack: self.stack.append([x, max(x, self.stack[-1][1])])
        else: self.stack.append([x, max(x, float("-inf"))])

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        maxValue = self.peekMax()
        buffer = []

        while self.stack[-1][0] != maxValue:
            buffer.append(self.stack.pop()[0])

        self.stack.pop()

        while buffer:
            self.push(buffer.pop())
        return maxValue

# Using two separate stacks - not accepted on LC
class MaxStack:
    def __init__(self):
        self.stack, self.maxStack = [], []

    def push(self, x: int) -> None:
        self.stack.append(x)

        if self.maxStack: x = max(x, self.maxStack[-1])
        else: x = x
        self.maxStack.append(x)

    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        maxValue = self.peekMax()
        buffer = []

        while self.top() != maxValue:
            buffer.append(self.pop())

        self.pop()

        while buffer:
            self.push(buffer.pop())
        return maxValue

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()