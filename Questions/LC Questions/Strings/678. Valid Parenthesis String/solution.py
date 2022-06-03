'''
    Explanation:
    - Invalid can occur when ) is more than ( + *
    - Invalid can also occur when looping from right to left and we do not have any extra ( i.e. when ( is more than ) + *


    Here we know we have never been unbalanced parsing from left to right e.g. ')('
        We've also already substituted '*' either by '(' or by ')'
        So we only have 3 possible scenarios here:
            1. We had the same amount of '(' and ')'
            2. We had more '(' then ')' but enough '*' to substitute
            3. We had more ')' then '(' but enough '*' to substitute
        return True
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        balance = 0
        for i in range(len(s)):
            if s[i] == ")":
                balance -= 1
            else: 
                balance += 1
            if balance < 0: # Here, we have unbalanced parentheses
                return False
        
        # Check if parentheses are valid
        if balance == 0:
            return True
        
        balance = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                balance -= 1
            else: 
                balance += 1
            if balance < 0: # Here, we have unbalanced parentheses
                return False