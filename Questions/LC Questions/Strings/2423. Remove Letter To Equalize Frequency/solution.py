'''
    Explanation I: Brute-Force
        Try to delete each letter in the word, and check if the remaining unique letters have same frequencies
        TC: O(n-squared), SC: O(n)

    Explanation II
        Case 1: single unique character ("aaaaa", "aa")
            Return true
        
        Case 2: Non-single unique characters
            2.1: Single unique frequency ("ab", "abcd")
                Return true
            
            2.2: Non-single unique frequencies
                2.2.1: More than two unique frequencies ("abbccc", "aabbbcccc")
                    Return false
                2.2.2: Two unique frequencies, m = min(freq), M = max(freq)
                    2.2.2.1: m = 1, and it appears only once ("abbbb", "abbbbcccc")
                        Return true
                    2.2.2.2: M - m = 1 and there is only one unique letter with frequency M ("aabbccc")
                        Return true

        TC: O(n), SC: O(n)
'''

from collections import Counter

class Solution1:
    def equalFrequency(self, word: str) -> bool:
        for char in word:
            wordFreq = Counter(word)
            wordFreq[char] -= 1

            if wordFreq[char] == 0:
                del wordFreq[char]
            if(len(set(wordFreq.values()))) == 1:
                return True
        return False
    
class Solution2:
    def equalFrequency(self, word: str) -> bool:
        charCount = Counter(word)
        freqCount = Counter(charCount.values())
        
        # Case aaaa
        if len(charCount) == 1:
            return True
        
        N = len(freqCount)
        if N == 1:
            # case abcd
            for freq in charCount.values():
                return freq == 1

        # case abbccc
        if N > 2:
            return False

        m, M = min(charCount.values()), max(charCount.values())
        # case abbbb
        if m == 1 and freqCount[m] == 1:
            return True
        # case aabbccc
        if M - m == 1 and freqCount[M] == 1:
            return True
        return False