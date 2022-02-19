'''
    Explanation:
        - history:   [leetcode, youtube, facebook, google]
        - urlPointer:               i
        visit: pop out all urls after the urlPointer, append the url to visit and move the urlPointer
        
        - history:   [leetcode, youtube, facebook, google], steps = 2
        - urlPointer:               i
        back and forward --> you don't want to go out of bound because of the steps
        
        TC - O(n) for all functions
        SC - O(n) for all functions --> to store the browserHistory
'''

class BrowserHistory:

    def __init__(self, homepage: str):
        self.browserHistory = [homepage]
        self.urlPointer = 0

    def visit(self, url: str) -> None:
        while len(self.browserHistory) - 1 > self.urlPointer:
            self.browserHistory.pop()
        self.browserHistory.append(url)
        self.urlPointer += 1

    def back(self, steps: int) -> str:
        while self.urlPointer > 0 and steps > 0:
            self.urlPointer -= 1
            steps -= 1
        return self.browserHistory[self.urlPointer]

    def forward(self, steps: int) -> str:
        while self.urlPointer < len(self.browserHistory) - 1 and steps > 0:
            self.urlPointer += 1
            steps -= 1
        return self.browserHistory[self.urlPointer]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)