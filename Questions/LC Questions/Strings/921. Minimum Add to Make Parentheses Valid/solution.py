class Solution1:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if stack and stack[-1] == '(': 
                    stack.pop()
                else: 
                    stack.append(char)
        return len(stack)
    
class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        lCount, rCount, res = 0, 0, 0

        for char in s:
            if char == "(":
                lCount += 1
            else:
                if lCount > rCount:
                    rCount += 1
                else:
                    res += 1
        res += lCount - rCount
        return res