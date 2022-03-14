'''
    Explanation:
        - history:   [leetcode, youtube, facebook, google]
        - urlPosition:               i
        visit: pop out all urls after the urlPosition, append the url to visit and move the urlPosition
        
        - history:   [leetcode, youtube, facebook, google], steps = 2
        - urlPosition:               i
        back and forward --> you don't want to go out of bound because of the steps
        
        TC - O(n) for all functions
        SC - O(n) for all functions --> to store the browserHistory
'''


class BrowserHistory:

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

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)