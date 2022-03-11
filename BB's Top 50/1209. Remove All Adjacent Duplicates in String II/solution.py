class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # create  a stack with [character, count]
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                
            else: 
                stack.append([char, 1])
                
            if stack and stack[-1][1] == k:
                stack.pop()
                
        # char * num prints the char in num times
        return "".join([char * num for char, num in stack])
        
        '''
            Explanation:
            - deeedbbcccbdaa
            [[d,1], [e,3]]
            [[d,2]]
        '''