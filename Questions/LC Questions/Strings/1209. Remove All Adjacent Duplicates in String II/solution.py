'''
    Explanation:
        - deeedbbcccbdaa
        [[d,1], [e,3]]
        [[d,2]]

        TC - O(2n) = O(n) where n is the size of the input string
        SC - O(n)
'''

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if s == "": return ""
        if k == 0 or k > len(s): return s

        # stack --> [character, count]
        stack = [[s[0], 1]]
        
        for char in s[1:]:
            if stack and stack[-1][0] == char: stack[-1][1] += 1
            else: stack.append([char, 1])
            if stack[-1][1] == k: stack.pop()
                
        res = ""
        for char, num in stack:
            res += char * num
        return res
        # return "".join([char * num for char, num in stack])