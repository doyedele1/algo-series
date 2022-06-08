class Solution:
    def findTheDifference(s, t):
        xor = 0
        for char in s: xor ^= ord(c)
        for char in t: xor ^= ord(c)          
        return chr(xor)

# print(Solution.findTheDifference('foobar', 'barfoot'))