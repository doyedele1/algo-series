'''
    dem(i(l)a)de)

    Explanation I: Stack Solution
        - Initialize an empty stack; make the input string a list and iterate through it
        - If character in the string is a (, append its index to the stack
        - When we encounter ),
            - If the stack is not empty, pop the top of the stack
            - If the stack is empty and we still have extra closing parentheses, change its character in the list to an empty string
        - In case of extra opening parentheses, change the remaining parentheses into an empty string
        - Return the string which is balanced

        TC: O(n) where n is the length of the input string since pushing to a stack and popping from a stack is O(1)
        SC: O(n) where n is the length of the input string for stack and list_conversion, each of which require n characters

    Explanation II: Non-Stack Solution
        Do the same as explanation I, but instead of stack, use two variables open_ and close

        In case of extra opening parentheses "))((", iterate from the back of the string and change the parentheses into an empty string, 

        TC: O(n)
        SC: O(1)
'''

class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                # extra closing bracket - "dem(i(l)a)de)""
                else:
                    s[i] = ""
        
        # extra opening bracket - "))(("
        while stack:
            s[stack.pop()] = ""
        return "".join(s)
    
class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        
        open_ = 0
        for i in range(len(s)):
            if s[i] == "(":
                open_ += 1
            elif s[i] == ")":
                if open_:
                    open_ -= 1
                else: 
                    s[i] = ""
        
        close = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")":
                close += 1
            elif s[i] == "(":
                if close:
                    close -= 1
                else: 
                    s[i] = ""
        
        return "".join(s)