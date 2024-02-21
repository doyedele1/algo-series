'''
    Explanation:
        word = "internationalization", abbr = "i12iz4n"

        - Use two pointers for word and abbr

        - If abbr[abbrPointer] is number,
            - Check if abbr[abbrPointer] is zero (0). Return false if it is
            - Find the steps it would take for 12 characters to be viewed in word, then move the wordPointer by steps time

        - Else: abbr[abbrPointer] is letter,
            - Then check if both word[wordPointer] and abbr[abbrPointer],
                return false if they are not equal, else move both pointers once at a time

        - If the wordPointer = len(word) and the abbrPointer = len(abbr), that means we've reached the end of the process and we can return True

        TC: O(n). Worst case -> when the word and abbr are the same. i.e. no substitution has been done
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