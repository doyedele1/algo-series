'''
    Explanation: Using an array
        visit:   [leetcode, google]
        visit: [leetcode, google, facebook]
        visit: [leetcode, google, facebook, youtube]
        urlPointer:                   i
        
        visit: [leetcode, google, facebook, linkedin]
        urlPointer:                            i
        
        visit: pop out all urls after the urlPointer, append the url to history array and move the urlPointer
        
        - history:   [leetcode, youtube, facebook, google], steps = 2
        - urlPointer:               i
        back and forward --> you don't want to go out of bound because of the steps
        
        TC - O(n) for all functions
        SC - O(n) for all functions --> to store the browserHistory
'''


class BrowserHistory1:
    def __init__(self, homepage: str):
        self.browserHistory = [homepage]
        self.urlPosition = 0

    def visit(self, url: str) -> None:
        while self.urlPosition < len(self.browserHistory) - 1:
            self.browserHistory.pop()
        self.browserHistory.append(url)
        self.urlPosition += 1

    def back(self, steps: int) -> str:
        while self.urlPosition > 0 and steps > 0:
            self.urlPosition -= 1
            steps -= 1
        return self.browserHistory[self.urlPosition]

    def forward(self, steps: int) -> str:
        while self.urlPosition < len(self.browserHistory) - 1 and steps > 0:
            self.urlPosition += 1
            steps -= 1
        return self.browserHistory[self.urlPosition]

class BrowserHistory2:
    def __init__(self, homepage: str):
        self.browserHistory = [homepage]
        self.urlPosition = 0
        self.size = 1

    def visit(self, url: str) -> None:
        if self.urlPosition + 1 == len(self.browserHistory):
            self.browserHistory.append(url)
        else: self.browserHistory[self.urlPosition + 1] = url
        self.urlPosition += 1
        self.size = self.urlPosition + 1

    def back(self, steps: int) -> str:
        self.urlPosition = max(0, self.urlPosition - steps)
        return self.browserHistory[self.urlPosition]

    def forward(self, steps: int) -> str:
        self.urlPosition = min(self.size - 1, self.urlPosition + steps)
        return self.browserHistory[self.urlPosition]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)