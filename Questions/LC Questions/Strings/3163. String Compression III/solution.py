'''
    abcde
'''

class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        pos = 0

        while pos < len(word):
            count = 0
            curr = word[pos]

            while (pos < len(word) and count < 9 and word[pos] == curr):
                count += 1
                pos += 1
            comp.append(str(count))
            comp.append(curr)
        return "".join(comp)