def reverseInt(num):
    res = 0

    while num > 0:
        res =  res * 10 + num % 10
        num //= 10
    return res

def validPalindrome(num):
    return num == reverseInt(num)

def solution(num):
    while num <= 4294967295:
        if validPalindrome(num):
            return num

        num += reverseInt(num)
        if num > 4294967295: return -1

# print(solution(195))