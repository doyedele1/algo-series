class Solution:
    def findTheDifference(s, t):
        xor = 0
        for c in s: xor ^= ord(c)
        print(xor)
        for c in t: xor ^= ord(c)
        print(xor)           
        return chr(xor)

print(Solution.findTheDifference('foobar', 'barfoot'))