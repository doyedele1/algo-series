'''
    Explanation I: Brute-Force Solution
        - We go through every single combination of binary codes of length k and then check every substring of s with these codes
        TC: (2^k * n * k)
        
    Explanation II: Using hash set
        "00110110"
        00110
        For first iteration, s[i:i+k] = 00
        - We can find the occurences of every code of length k in the string
        - We create a hashset to store the occurences of the code, so we don't repeat it
        - We loop from index 0 to where we can possibly stop due to k not going out of bound
            - We check the substring of length k if it's in the set
                - If it's there, do nothing
                - If it's not there, add the substring of length k to the hash set
        - We know we've found the occurences of code of length k, if length of the hash set is the same as 2 ^ k
        
        TC: O(nk) --> O(n) to iterate the string, O(k) to calculate each substring and add to the hash set
        SC: O(nk). If we check the hashset, there are at most n strings with length of k in the set
'''

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        uniqueCodeForK = set()
        
        for i in range(len(s) - k + 1):
            temp = s[i:i+k]
            if temp not in uniqueCodeForK:
                uniqueCodeForK.add(temp)
            print(uniqueCodeForK)
            
        return len(uniqueCodeForK) == 2 ** k