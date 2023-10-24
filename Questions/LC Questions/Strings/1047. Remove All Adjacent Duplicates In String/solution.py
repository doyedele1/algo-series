'''
    Explanation:
        - We will have a stack to keep track of the characters.
        - We will iterate through the string and check if the current character is already in the stack.
            - If it is, we will pop the last character from the stack.
            - If it is not, we will append the current character to the stack.
        - We will return the string after joining the stack.

        "abbaca"
        stack = [a]
        stack = [ab]
        stack = [a]
        stack = []
        stack = [c]
        stack = [ca]

        TC - O(n) where n is the length of the string
        SC - O(n-d) where d is the total length of all duplicates
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1] == char: stack.pop()
            else: stack.append(char)
        return "".join(stack)