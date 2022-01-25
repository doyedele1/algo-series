class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # First solution
        # return len(set(sentence)) == 26

        # Another solution
        flag = [0] * 26
        
        for char in sentence:
            flag[ord(char) - 97] += 1
            
        for i in flag:
            if i < 1:
                return False
        return True