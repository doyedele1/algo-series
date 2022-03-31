class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = ""
        
        if(len(s) != len(goal)):
            return False
        
        temp = s + s
        if(temp.count(goal) > 0):
            return True
        return False