class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        
        for char in s:
            if char in dict:
                dict[char] += 1
            else: dict[char] = 1
        print(dict)
                
        for index, char in enumerate(s):
            if dict[char] == 1:
                return index
        return -1

        # TC - O(n), SC - O(1)