'''
    ["eat","tea","tan","ate","nat","bat"]
    
    Explanation I:
        result hashmap = {
            ('a', 'e', 't'): ["eat", "tea", "ate"],
            ('a', 'b', 't'): ["bat"],
            ('a', 'n', 't'): ["nat", "tan"]
        }

        TC: O(m * nlog n) where m is the length of strs and n is the maximum length of a string in strs
        SC: O(m * n) which is the total information content stored in res

    Explanation II:
        - Create a hashmap
            key -> {e: 1, a: 1, t: 1} or (1,0,0,0,1,0,0,...,1...0). key is going to be of length 26 
            value -> all anagram strings of the key = ["eat", "tea", "ate"]

        TC: O(m * n * 26) where m is the length of strs and n is the maximum length of a string in strs
        SC: O(m * n) which is the total information content stored in res
'''

import collections
from typing import List

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        
        for word in strs:
            res[tuple(sorted(word))].append(word)
        return res.values()
    
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(word)
        return res.values()