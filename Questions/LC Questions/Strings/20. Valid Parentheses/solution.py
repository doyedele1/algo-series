'''
    Explanation I: 
        "()[]{}"
        stack = "("
        stack = ""
        stack = "["
        stack = ""
        stack = "{"
        stack = ""
        
        Since len(stack) == 0, return True

        "(())"


        "([{}])"

        TC - O(n) where n is the length of the input string
        SC - O(n) for the extra data structure. Worst case is when we have all opening brackets, then we need to keep track of all the opening brackets in the stack
'''

import collections

class Solution1:
    def isValid(self, s: str) -> bool:  
        stack = collections.deque()
        
        for char in s:
            if char == "(" or char == "[" or char == "{": stack.appendleft(char)
            elif char == ")":
                # If there is nothing in the stack, then we want to check the length of the current stack and return False
                if len(stack) < 1 or stack[0] != "(": return False
                else: stack.popleft()
            elif char == "]":
                if len(stack) < 1 or stack[0] != "[": return False
                else: stack.popleft()
            elif char == "}":
                if len(stack) < 1 or stack[0] != "{": return False
                else: stack.popleft()           
        return not stack

class Solution2:
    def isValid(self, s: str) -> bool:  
        stack = [] # We could also use collections.deque()
        mapping = { ")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping: # Checking for closing parentheses
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else: return False
            else: stack.append(char) # Append all opening parentheses
        return not stack