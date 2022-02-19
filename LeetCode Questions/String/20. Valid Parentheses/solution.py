'''
    Explanation: 
        "()[]{}"
        stack = "("
        stack = ""
        stack = "["
        stack = ""
        stack = "{"
        stack = ""
        
        Since len(stack) == 0, return True
'''

import collections

class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.appendleft(char)
            elif char == ")":
                if len(stack) < 1 or stack[0] != "(":
                    return False
                else: stack.popleft()
            elif char == "]":
                if len(stack) < 1 or stack[0] != "[":
                    return False
                else: stack.popleft()
            elif char == "}":
                if len(stack) < 1 or stack[0] != "{":
                    return False
                else: stack.popleft()
                    
        if len(stack) > 0:
            return False
        else:
            return True