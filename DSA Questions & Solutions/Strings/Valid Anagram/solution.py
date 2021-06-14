def valid_anagram(str1, str2):
    if(len(str1) != len(str2)):
        return False
    
    freqCounter1 = {}
    freqCounter2 = {}

    for char in str1:
        if(char in freqCounter1):
            freqCounter1[char] += 1 
        else:
            freqCounter1[char] = 1

    for char in str2:
        if(char in freqCounter2):
            freqCounter2[char] += 1
        else:
            freqCounter2[char] = 1

    for key in freqCounter1:
        if(key not in freqCounter2):
            return False
        if(freqCounter1[key] != freqCounter2[key]):
            return False
    return True

print(valid_anagram("cat", "tac")) # return True
print(valid_anagram("listen", "silent")) # return True
print(valid_anagram("program", "function")) # return False