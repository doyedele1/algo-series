# Brute force solution: T(C) - O(n-squared), SC - O(n)
def is_unique(s):
    s = s.lower()

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if(s[i] == s[j]):
                return False
    return True

# Optimal solution: T(C) - O(n), S(C) - O(n)
def is_unique(s):
    s = s.lower()
    seen = set()

    for char in s:
        if char in seen:
            return False
        else:
            seen.add(char)
    return True

# Follow up solution: T(C) - O(nlogn), S(C) - O(n)
def is_unique(s):
    s = sorted(s.lower())

    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

# Another optimized follow up solution: T(C) - O(n), S(C) - O(1)
# def is_unique(s):
#     s = sorted(s.lower())

#     for i in range(0, len(s)-1):
#         if s[i] == s[i+1]:
#             return False
#     return True


print(is_unique("heLlo")) # print false
print(is_unique("hey")) # print true