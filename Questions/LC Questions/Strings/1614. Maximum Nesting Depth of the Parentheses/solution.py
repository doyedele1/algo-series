'''
    NOTE: The depth of any character in the VPS is the (number of left brackets before it) - (number of right brackets before it)
'''

# TC: O(n), SC: O(n)
class Solution:
    def maxDepth(self, s: str) -> int:
        stack, res = [], 0
        
        for char in s:
            if stack and char == ")": stack.pop()
            if char == "(":
                stack.append(char)
                res = max(res, len(stack))
        return res

# TC: O(n), SC: O(1)
class Solution2:
    def maxDepth(self, s: str) -> int:
        res = count = 0
        
        for char in s:
            if count and char == ")":
                count -= 1
                res = max(res, count + 1)
            elif char == "(": count += 1
        return res