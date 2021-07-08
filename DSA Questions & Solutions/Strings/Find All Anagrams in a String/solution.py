class Solution:
    def findAnagrams(self, s: str, p: str):
        s_len = len(s)
        p_len = len(p)
        
        s_hash = [0]*26
        p_hash = [0]*26
        
        result = []
        
        left = 0
        right = 0
        
        if p_len > s_len:
            return result
        
        
        while(right < p_len):
            p_hash[ord(p[right]) - ord('a')] += 1
            s_hash[ord(s[right]) - ord('a')] += 1
            
            right += 1
        
        right -= 1
        while(right < s_len):
            if(s_hash == p_hash):
                result.append(left)
            right += 1
            if(right != s_len):
                s_hash[ord(s[right]) - ord('a')] += 1
            s_hash[ord(s[left]) - ord('a')] -= 1
            left += 1
        
        return result