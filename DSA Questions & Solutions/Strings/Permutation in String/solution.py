class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        
        s1_hash = [0]*26
        s2_hash = [0]*26
        
        left = 0
        right = 0
        
        if s1_len > s2_len:
            return False
        
        while(right < s1_len):
            s1_hash[ord(s1[right]) - ord('a')] += 1
            s2_hash[ord(s2[right]) - ord('a')] += 1
            
            right += 1
        
        right -= 1
        while(right < s2_len):
            if(s1_hash == s2_hash):
                return True
            right += 1
            if(right != s2_len):
                s2_hash[ord(s2[right]) - ord('a')] += 1
            s2_hash[ord(s2[left]) - ord('a')] -= 1
            left += 1
        
        return False