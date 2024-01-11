'''
    Explanation:
        - Create an hash map that maps closed bracket to the open one
        - Create a stack to hold all open brackets
        - Loop through the string, push current char into stack if it is not in map
        - Else check if current char maps is equal to char at the top of stack
            - Pop top off
        - Return false if it does not map
        - Once loop is done, return true if stack is empty, else false

        "()[]{}"
        stack = "("
        stack = ""
        stack = "["
        stack = ""
        stack = "{"
        stack = ""
        Since len(stack) == 0, return True

        Other examples: "(())", "([{}])"

        TC: O(n)
        SC: O(n) for the stack. Worst case is when we have all opening brackets, then we need to push all the opening brackets in the stack
'''

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = [] # could also use collections.deque()

        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if len(stack) > 0 and mapping[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0