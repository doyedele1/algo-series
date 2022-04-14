'''
    Explanation I: 
        - The idea is to use a hashmap to store the characters in the sentence.
        - If the sentence is a pangram, then all the characters in the alphabet (26) should be in the hashmap.
        - TC: O(n), SC: O(n)
    
    Explanation II:
        - The idea is to use a fixed size array to store the characters in the sentence. Size = 26
        - Loop through the sentence and increment the count of each character in the array.
        - Loop through the array and check the count of any character
            - If the count is less than 1, return False
        - Return True
        - TC: O(n), SC: O(1)
'''


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