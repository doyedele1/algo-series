class Solution:
    def isValid(self, s: str) -> bool:
        valid = True
        stack = []
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")":
                if not stack or stack.pop() != "(":
                    valid = False
                else: valid
            elif char == "]":
                if not stack or stack.pop() != "[":
                    valid = False
                else: valid
            elif char == "}":
                if not stack or stack.pop() != "{":
                    valid = False
                else: valid
        if valid and not stack: return True
        else: return False