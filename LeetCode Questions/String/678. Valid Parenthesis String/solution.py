class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
            Explanation:
            - Invalid can occur when ) is more than ( + *
            - Invalid can also occur when looping from right to left and we do not have any extra ( i.e.
                - when ( is more than ) + *
        '''
        
        if len(s) == 0:
            return True
        
        balance = 0
        for i in range(len(s)):
            if s[i] == ")":
                balance -= 1
            else: 
                balance += 1
            if balance < 0: 
                return False
        if balance == 0:
            return True
        
        balance = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                balance -= 1
            else: 
                balance += 1
            if balance < 0:
                return False
        return True