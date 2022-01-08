class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        open_ = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                open += 1
            elif s[i] == ")":
                if open:
                    open -= 1
                else: s[i] = ""
        
        close = 0
        for i in reversed(range(len(s))):
            if s[i] == ")":
                close += 1
            elif s
                
#         stack = []
#         str_arr = []
        
#         for i, char in enumerate(s):
#             if char == "(":
#                 stack.append(char)
#             elif char == ")":
#                 if len(stack) != 0:
#                     stack.pop()
#                 else:
#                     s[i] = ""
        
#         for ind in stack:
#             str_arr[ind] == ""
        
#         return "".join(str_arr)

    
    
            
                
        