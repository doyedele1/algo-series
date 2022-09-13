'''
    Explanation:
        3[a2[c]]
        - Number in front of a character shows how many times that character will be multiplied
        - 3 applies to everything in the bracket
        - acc * 3 ==> accaccacc
        
        - We will have to solve the inner brackets before the outer brackets --> recursive solution
        
        54[ab6[cd]]
        stack = 5, 4, [, a, b, 6, [, c, d
                5, 4, [, a, b, 6
                We pop any integer after what we've popped which is 6 --> 6 * cd
                5, 4, [, a, b, 6*cd
                54, ab, 6*cd
                Take everything we pop and multiply by int before what we've popped --> 54 and add to the stack
                Return the stack after everything
                
        TC - O(maxK ^ countK * n) where maxK is the maximum value of K and countK is the count of nested k values and n is the maximum length of encoded string. For example:
        s = 20[a10[bc]], maxK = 20, countK = 2 as there are two nested K values (20 and 10). n = 2 as there are 2 encoded strings (a and bc).
        
        SC - O(sum(maxK ^ countK * n))) where maxK is the maximum value of K, countK is the count of nested K values and n is the maximum length of encoded string
        max stack size = sum of all decoded strings in the form -> maxK[nmaxK[n]]
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]": stack.append(s[i])
            else:
                substr = ""
                # we want to keep popping until we encounter an open square bracket
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                # pop the open square bracket
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * substr)
                
        return "".join(stack)