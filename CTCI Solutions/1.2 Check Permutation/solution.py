# Brute force solution: T(C) - O(nlogn), SC - O(n)
def check_permutation(s1, s2):
    if(len(s1) != len(s2)):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2

# Optimal solution: T(C) - O(n), S(C) - O(n)
def check_permutation(s1, s2):
    dict1 = {}
    dict2 = {}

    for char in s1:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    for char in s2:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1
    
    for key in dict1:
        if key not in dict1:
            return False
        if dict1[key] != dict2[key]:
            return False
    return True


print(check_permutation("wazup bro", " orbpuwaz"))
print(check_permutation("hiiiya", "hiya"))