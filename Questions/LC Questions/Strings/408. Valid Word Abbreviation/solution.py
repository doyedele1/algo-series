'''
    Explanation:

        TC: O(n)
        SC: O(1)
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordPointer, abbrPointer = 0, 0

        while wordPointer < len(word) and abbrPointer < len(abbr):
            if abbr[abbrPointer].isdigit():
                if abbr[abbrPointer] == "0":
                    return False
    
                steps = 0

                while abbrPointer < len(abbr) and abbr[abbrPointer].isdigit():
                    steps = steps * 10 + int(abbr[abbrPointer])
                    abbrPointer += 1
                wordPointer += steps
            
            else:
                if word[wordPointer] != abbr[abbrPointer]:
                    return False
                
                wordPointer += 1
                abbrPointer += 1
        
        return wordPointer == len(word) and abbrPointer == len(abbr)