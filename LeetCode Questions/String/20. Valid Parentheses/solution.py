import collections

class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        valid = True
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    valid = False
                else: valid
            elif char == "]":
                if len(stack) == 0 or stack.pop() != "[":
                    valid = False
                else: valid
            elif char == "}":
                if len(stack) == 0 or stack.pop() != "{":
                    valid = False
                else: valid
                    
        if valid and len(stack) == 0:
            return True
        return False