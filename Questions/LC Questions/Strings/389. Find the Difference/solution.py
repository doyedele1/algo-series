'''
    Explanation:
        - If we do xor of 0101 and 0101, we get 0 because they cancel each other out

        - For string "a", 
            -The ASCII equivalent is 97. 0 xor 97 = 97
        - For string "ab", (we do the xor character wise and add to the xor variable)
            - The ASCII equivalent of the first character is 97. 97 xor 97 = 0.
            - The second character is 98. 0 xor 98 = 98 which is our difference.

        - TC: O(n)
        - SC: O(1)
'''

class Solution:
    def findTheDifference(s, t):
        xor = 0
        for char in s: xor ^= ord(char)
        for char in t: xor ^= ord(char)          
        return chr(xor)

# print(Solution.findTheDifference('foobar', 'barfoot'))