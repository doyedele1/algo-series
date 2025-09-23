# TC: O(n + m), SC: O(n + m) where n is the length of version1 and m is the length of version2
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split(".")
        revisions2 = version2.split(".")
        
        len1, len2 = len(revisions1), len(revisions2)
        max_len = max(len1, len2)

        for i in range(max_len):
            r1 = int(revisions1[i] if i < len1 else 0)
            r2 = int(revisions2[i] if i < len2 else 0)

            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1
        return 0