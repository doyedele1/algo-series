class Solution:
    def findTheDifference(s, t):
        xor = 0
        for char in s: xor ^= ord(char)
        for char in t: xor ^= ord(char)          
        return chr(xor)

# print(Solution.findTheDifference('foobar', 'barfoot'))