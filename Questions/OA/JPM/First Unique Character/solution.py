from collections import Counter

def solution(s):
        count = Counter(s)
        
        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx + 1     
        return -1