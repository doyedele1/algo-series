class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for char in s:
            if len(stack) > 0 and stack[-1] == char:
                stack.pop()
            else: stack.append(char)
        return "".join(stack)
    
        # "abbaca"
        
        # TC - O(n), SC - O(n-d) where d is the total length of all duplicates