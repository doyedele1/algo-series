'''
    TC - O(n), SC - O(1)
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        
        # We could use collections.Counter to create the hashmap
        # dict = collections.Counter(s) or use object in Python
        for char in s:
            if char in dict:
                dict[char] += 1
            else: dict[char] = 1
                
        for index, char in enumerate(s):
            if dict[char] == 1:
                return index
        return -1