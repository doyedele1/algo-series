def findWinner(s):
    w=0
    b=0
    for i in range(len(s)-2):
        if s[i:i+3]=='www':
            w+=1
        if s[i:i+3]=='bbb':
            b=b+1

    if w>b:
        return('wendy')
    else:
        return('bob')

print(findWinner("wwwwb"))


# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num == 0: return 0
#         if num % 9 == 0: return 9
#         else: return num % 9