'''
    Explanation:
        - Store the occurence of characters in s in a hashmap or array
        - Reduce the occurence of each character seen in s in t by 1
        - If the frequency of a character is more than 0, i.e. the characters left are stopping the two strings becomes anagram of each other,
            - Then add the counts together
            
        - "bab", "aba"
            counts = {b: 2, a: 1}
            - Checking t,
                First character: counts = {b: 2, a: 0}
                Second character: counts = {b: 1, a: 0}
                Third character: counts = {b: 1, a: -1}
            - count of b is 1, so res += 1 which is finally 1
            
        - TC: O(n)
        - SC: O(n) for the hashmap solution and O(1) for the array solution
'''

# Using a fixed array of size 26
class Solution1:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        counts = [0] * 26
        
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        
        for count in counts:
            if count > 0: res += count
        return res

# Using a hashmap
class Solution2:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        counts = dict()
        
        for char in s:
            if char in counts: counts[char] += 1
            else: counts[char] = 1
        
        for char in t:
            if char in counts and counts[char] > 0: counts[char] -= 1
            else: res += 1
        return res