class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        
        s = s.split(" ")

        for i in range(len(s)):
            s[i] = s[i][::-1]
            
        return " ".join(s)