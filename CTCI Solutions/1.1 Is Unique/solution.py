# Brute force solution
def is_unique(s):
    s = s.lower()

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if(s[i] == s[j]):
                return False
    return True

# Optimal solution
# def is_unique(s):
#     s = s.lower()
    
#     for i1, char1 in enumerate(s):
#         for i2, char2 in enumerate(s):
#             print(char1, char2)
#             if(i1 == i2):
#                 continue
#             if(char1 == char2):
#                 return False
#     return True


print(is_unique("heLlo")) # print false
print(is_unique("hey")) # print true