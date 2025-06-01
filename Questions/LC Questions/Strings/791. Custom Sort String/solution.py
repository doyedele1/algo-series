'''
    Explanation:
        Original Question:
            s = "babcz", order = "cba"

            Brute force solution: Two for loops
                Iterate through order (cba).
                First, we see a c. Iterate through s and look for a c. If it is present, add to the result. res = "c"
                Second, we see a b. Iterate through s and look for a b. If it is present, add to the result. res = "cbb"
                Third, we see an a. Iterate through s and look for an a. If it is present, add to the result. res = "cbba"

                After, we iterate through s and check for the remaining characters we have not added to s, and then add to res. res = "cbbaz"

                Note: There could be two edge cases.
                Case 1: A character in order does not exist in s. order can be "cbad". Since d does not exist in s, we don't add to res
                Case 2: This is what we have seen already. A character in s does not exist in order. If s = "babcz", z does not exist in order, but we need to add to res in any position creating different permutations

                TC: O(s*order) = O(s-squared)
                SC: O(s)

            Optimal Solution: Hashmap
                In previous solution, we are going through our string s to find character we have seen in order. We are doing this multiple times. Why not look for the character once?
                So, we can use a hashmap that is a frequency counter of s

                s = "babcz", order = "cba"
                freq = {a: 1, b: 2, c: 1, z: 1}

                Iterate through the order.
                
                First iteration: We see a c. We can then check freq for c. If it's there, we add it to our res and have the count as 0. 
                res = "c", freq = {a: 1, b: 2, c: 0, z: 1}
                
                Second iteration: We see a b. We can then check freq for b. If it's there, we add it to our res and have the count as 0. 
                res = "cbb", freq = {a: 1, b: 0, c: 0, z: 1}
                
                Third iteration: We see an a. We can then check freq for a. If it's there, we add it to our res and have the count as 0. 
                res = "cbba", freq = {a: 0, b: 0, c: 0, z: 1}

                When we are done iterating through order, we then check freq for any char with count greater than 0, and add it to res
                res = "cbbaz"

                TC: O(s)
                SC: O(26). O(s) if we count auxiliary space variables like res

        Follow-up Question: Optimize your solution - use an array/list, instead of a hashmap
            If we use a hashmap, it can suffer from collisions

            TC: O(s)
            SC: O(1)

        Variant Question: Different Order Parameter
            order is now an array of characters, rather than a string

            TC: O(s)
            SC: O(1)
'''
from collections import Counter
from typing import List

class OriginalSolution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = []

        for ch in order:
            if ch in freq:
                res.extend([ch] * freq[ch])
                freq[ch] = 0
        
        for ch, count in freq.items():
            if count > 0:
                res.extend([ch] * count)
        
        return "".join(res)
    
class FollowUpSolution:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0] * 26
        res = ""

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for ch in order:
            if ch in freq:
                res += ch * freq[ord(ch) - ord('a')]
                freq[ord(ch) - ord('a')] = 0
        
        for i in range(26):
            res += chr(i + ord('a')) * freq[i]
        
        return res

# Same solution as the OriginalSolution
class VariantSolution:
    def customSortString(self, order: List[str], s: str) -> str:
        freq = Counter(s)
        res = []

        for ch in order:
            if ch in freq:
                res.append(ch * freq[ch])
                del freq[ch]
        
        for ch, freq in freq.items():
            res.append(ch * freq)
        
        return ''.join(res)