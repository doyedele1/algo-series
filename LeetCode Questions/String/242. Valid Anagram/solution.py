def valid_anagram(s, t):
    if len(s) != len(t):
            return False
        
    dict_s = {}
    
    for i in s:
        if i in dict_s:
            dict_s[i] += 1
        else: 
            dict_s[i] = 1
            
    for x in t:
        if x in dict_s:
            dict_s[x] -= 1
        else: 
            return False
        
    for c in dict_s:
        if dict_s[c] != 0:
            return False
    return True

# print(valid_anagram("cat", "tac")) # return True
# print(valid_anagram("listen", "silent")) # return True
# print(valid_anagram("program", "function")) # return False