# TC: O(n + m), SC: O(1) since we will only be storing at most 4 characters in the mismatches array
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        n = len(s1)
        mismatch = []

        for i in range(n):
            if s1[i] != s2[i]:
                mismatch.append(s1[i])
                mismatch.append(s2[i])
        
        return len(mismatch) == 4 and mismatch[0] == mismatch[3] and mismatch[1] == mismatch[2]