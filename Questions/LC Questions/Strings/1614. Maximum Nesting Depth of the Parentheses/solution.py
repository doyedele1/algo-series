'''
    NOTE: The depth of any character in the VPS is the ( number of left brackets before it ) - ( number of right brackets before it )
'''

# TC: O(n), SC: O(n)
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res = 0
        
        for char in s:
            if char == ")":
                stack.pop()
            if char == "(":
                stack.append(char)
                res = max(res, len(stack))
        return res