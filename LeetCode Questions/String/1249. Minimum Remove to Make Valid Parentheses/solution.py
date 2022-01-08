class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Solution with the stack
        stack = []
        s = list(s)
        
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        
        while stack:
            s[stack.pop()] = ""
        
        return "".join(s)
    
    
    
    
    
        # Non-stack solution
        '''
        s = list(s)
        
        open_ = 0
        for i in range(len(s)):
            if s[i] == "(":
                open_ += 1
            elif s[i] == ")":
                if open_:
                    open_ -= 1
                else: s[i] = ""
        
        close = 0
        for i in reversed(range(len(s))):
            if s[i] == ")":
                close += 1
            elif s[i] == "(":
                if close:
                    close -= 1
                else: s[i] = ""
        
        return "".join(s)
        '''