# Simple solution without considering edge cases
def valid_palindrome1(str):
    reversed_str = str[::-1]

    if (str == reversed_str):
        return True
    return False

# print("Simple solution: " +str(valid_palindrome1("Algorithms")))

# Ignoring other characters and white spaces
def valid_palindrome(str):
    l = 0
    r = len(str) - 1
    lowerCaseStr = str.lower()

    while (l <= r):
        if(not(lowerCaseStr[l] >= 'a' and lowerCaseStr[l] <= 'z')):
            l += 1

        elif(not(lowerCaseStr[r] >= 'a' and lowerCaseStr[r] <= 'z')):
            r -= 1

        elif lowerCaseStr[l] == lowerCaseStr[r]:
            l += 1
            r -= 1

        else:
            return False

    return True


# print(valid_palindrome("level"))
# print(valid_palindrome("algorithm"))
# print(valid_palindrome("A man, a plan, a canal: Panama."))