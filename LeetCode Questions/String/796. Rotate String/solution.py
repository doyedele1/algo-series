'''
    Explanation:
        - Create an empty temp string
        - If len(s) and len(goal) are different, return False
        - Concatenate s twice and store in temp
        - If goal is in temp, return True
        - Else, return False
        - TC: O(n-squared), SC: O(n)
'''

class Solution1:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = ""
        
        if(len(s) != len(goal)):
            return False
        
        temp = s + s
        if(temp.count(goal) > 0):
            return True
        return False

class Solution2:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s