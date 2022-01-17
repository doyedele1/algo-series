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
            Explanation:
                STACK SOLUTION
                    - Initialize an empty stack
                    - Make the input string a list and iterate through it
                    - If character in the string is a (, append its index to the stack
                    - When we encounter ), we check if the stack is not empty and pop the current matching parenthesis out of the stack
                        - We also change its character in the list to an empty string
                    - We can then change the remaining unbalanced parentheses into an empty string
                    - We are then left with the balanced string

                    - TC - O(n) where n is the length of the input string since pushing to a stack and popping from a stack is O(1)
                    - SC - O(n) where n is the length of the input string for stack and list_conversion, each of which require n characters



                NON-STACK SOLUTION
        '''