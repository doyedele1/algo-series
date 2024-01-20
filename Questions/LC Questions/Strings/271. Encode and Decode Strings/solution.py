'''
    Explanation:
        ["Hello", "World"]
        encode: "5#Hello5#World"
        decode:
            - Get the length of each string with the delimiter
                - We know the length comes first and then the #
            - Add the string of that length to res array

        TC: O(n) where n is the total number of characters in the input string
        SC: O(k) where k is the number of strings. For each word, we are using some space for the length and delimiter #
'''

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Use j to find the delimeter
            j = i
            while s[j] != '#':
                j += 1
                
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            # Move the index to the start of the next length
            i = j + 1 + length
            
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))